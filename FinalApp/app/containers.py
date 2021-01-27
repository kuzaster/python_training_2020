import os
import re
import time

import docker
import yaml

config_path = os.path.join(os.path.dirname(__file__), "config-file.yaml")
copy_path = os.path.join(os.path.dirname(__file__), "copy-config-file.yaml")


def get_all_containers(path=config_path):
    with open(path) as conf:
        return yaml.safe_load(conf)


def get_cont_by_name(name):
    for cont in get_all_containers():
        if cont["name"] == name:
            return cont


def update_timestamp(new_stamp):
    with open(os.path.join(os.path.dirname(__file__), "timestamp.txt"), "w") as stamp:
        stamp.write(str(new_stamp))


def update_config(new_data, path=copy_path):
    with open(path, "w") as conf:
        yaml.dump(new_data, conf)


def check_dock_path(dock_path):
    if dock_path.startswith("https://github"):
        dock_path = dock_path[8:]
        return dock_path
    return dock_path


def start_containers():
    client = docker.from_env()
    conts = client.containers
    containers = get_all_containers()
    watch_file_update()
    for container in containers:
        if "options" not in container:
            container["options"] = {}
        cont_name = container["name"]
        options, dock_path = container["options"], container["docker_path"]
        port, pub_url = container["port"], container["public_url"]
        if not conts.list(all=True, filters={"name": cont_name}):
            run_cont = run_container(cont_name, options, dock_path, port, pub_url)
            update_config(containers, config_path)
            update_config(containers, copy_path)
        elif conts.get(cont_name).status != "running":
            try:
                conts.get(cont_name).start()
                print(f"Container {cont_name} started!")
            except docker.errors.APIError as er:
                conts.get(cont_name).remove()
                raise er
        else:
            print(f"Container {cont_name} is running!")


def change_container(old_name, new_name, new_opts, new_path, new_port, new_url):
    containers = get_all_containers()
    client = docker.from_env()
    for cont in containers:
        if cont["name"] == old_name:
            container = client.containers.get(old_name)
            container.stop()
            container.remove()
            run_cont = run_container(new_name, new_opts, new_path, new_port, new_url)
            cont["name"] = new_name
            cont["options"], cont["docker_path"] = new_opts, new_path
            cont["port"], cont["public_url"] = new_port, new_url
            update_config(containers, config_path)
            update_config(containers)
            update_timestamp(os.stat(config_path).st_mtime)
            return run_cont


def check_ports(options, port, host_port):
    if "ports" not in options:
        options["ports"] = {port: host_port}
        return options
    if (
        isinstance(options["ports"][port], list)
        and host_port not in options["ports"][port]
    ):
        options["ports"][port].append(host_port)
        return options
    if not isinstance(options["ports"][port], list) and host_port not in [
        options["ports"][port]
    ]:
        options["ports"][port] = [options["ports"][port]]
        options["ports"][port].append(host_port)
        return options
    return options


def run_container(cont_name, options, dock_path, port, pub_url):
    client = docker.from_env()
    imgs = client.images
    conts = client.containers
    host_port = int(re.search(r"http://localhost:(\d*)", pub_url).group(1))
    options["detach"] = True
    options["name"] = cont_name
    options = check_ports(options, port, host_port)
    # build image
    cont_image = imgs.build(path=check_dock_path(dock_path))[0]
    # create container
    container = conts.run(image=cont_image, **options)
    print(f"Container {container.name} run!")
    return container


def add_container(cont_name, options, dock_path, port, pub_url):
    cont_config = {
        "name": cont_name,
        "options": options,
        "docker_path": dock_path,
        "port": port,
        "public_url": pub_url,
    }
    run_cont = run_container(cont_name, options, dock_path, port, pub_url)
    containers = get_all_containers()
    containers.append(cont_config)
    update_config(containers, config_path)
    update_config(containers)
    update_timestamp(os.stat(config_path).st_mtime)
    return run_cont


def remove_container(name):
    client = docker.from_env()
    container = client.containers.get(name)
    container.stop()
    container.remove()
    containers = get_all_containers()
    containers.remove(get_cont_by_name(name))
    update_config(containers, config_path)
    print(f"Container {name} stopped and removed")
    update_config(containers)
    update_timestamp(os.stat(config_path).st_mtime)


def find_changed_cont_and_update():
    changed_conts = get_all_containers()
    old_conts = get_all_containers(copy_path)
    client = docker.from_env()
    conts = client.containers
    config_timestamp = os.stat(config_path).st_mtime
    if len(changed_conts) == len(old_conts):
        for ind, cont in enumerate(old_conts):
            if changed_conts[ind] != cont:
                container = conts.get(cont["name"])
                container.stop()
                container.remove()
                if "options" not in changed_conts[ind]:
                    changed_conts[ind]["options"] = {}
                new_name = changed_conts[ind]["name"]
                new_opts, new_path = (
                    changed_conts[ind]["options"],
                    changed_conts[ind]["docker_path"],
                )
                new_port, new_url = (
                    changed_conts[ind]["port"],
                    changed_conts[ind]["public_url"],
                )
                run_cont = run_container(
                    new_name, new_opts, new_path, new_port, new_url
                )
                print(f"Container {cont['name']} changed and re-run!")
                update_config(changed_conts, config_path)
                update_config(changed_conts, copy_path)
                update_timestamp(config_timestamp)
    elif len(changed_conts) > len(old_conts):
        update_timestamp(config_timestamp)
        start_containers()
    else:
        for cont in old_conts:
            if cont not in changed_conts:
                container = conts.get(cont["options"]["name"])
                container.stop()
                container.remove()
                update_config(changed_conts, copy_path)
                update_timestamp(config_timestamp)
    update_timestamp(config_timestamp)


def watch_file_update():
    time_path = os.path.join(os.path.dirname(__file__), "timestamp.txt")
    if not os.path.exists(copy_path):
        with open(copy_path, "x") as copy_conf:
            yaml.dump(get_all_containers(), copy_conf)
    while True:
        time.sleep(1)
        if os.path.exists(time_path):
            with open(time_path) as stamp:
                timestamp = float(stamp.read().strip())
                file_stamp = os.stat(config_path).st_mtime
                if timestamp != file_stamp:
                    print("They are different")
                    find_changed_cont_and_update()
                    return True
                print("No changes!")
                return False
        else:
            with open(time_path, "w") as stamp:
                stamp.write(str(os.stat(config_path).st_mtime))


def check_port_in_pub_url(cont_name, port):
    client = docker.from_env()
    conts = client.containers
    for container in conts.list(all=True, filters={"publish": port}):
        if container.name != cont_name:
            raise docker.errors.APIError(
                f"Port {port} is already allocated. Please, choose another port"
            )


def check_port_in_options(cont_name, options):
    if "ports" not in options:
        return
    ports = options["ports"].values()
    for port in ports:
        if isinstance(port, list):
            for p in port:
                check_port_in_pub_url(cont_name, p)
        check_port_in_pub_url(cont_name, port)
