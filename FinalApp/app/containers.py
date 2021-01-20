import json
import os
import time

import docker
import yaml

# with open(os.path.join(os.path.dirname(__file__), "config-file.json")) as conf:
#     copy_config_file = json.load(conf)
config_path = os.path.join(os.path.dirname(__file__), "config-file.yaml")
copy_path = os.path.join(os.path.dirname(__file__), "copy-config-file.yaml")


def get_all_containers(path=config_path):
    with open(path) as conf:
        return yaml.safe_load(conf)


def get_cont_by_name(name):
    for cont in get_all_containers():
        if cont["options"]["name"] == name:
            return cont


def start_containers():
    client = docker.from_env()
    imgs = client.images
    conts = client.containers
    for container in get_all_containers():
        options, dock_path = container["options"], container["docker_path"]
        name = options["name"]
        if not conts.list(all=True, filters={"name": name}):
            run_container(options, dock_path)
        elif conts.get(name).status != "running":
            conts.get(name).start()
            print(f"Container {name} started!")
        else:
            print(f"Container {name} is running!")


def change_container(old_name, new_opts, new_path, new_port, new_url):
    containers = get_all_containers()
    client = docker.from_env()
    for cont in containers:
        if cont["options"]["name"] == old_name:
            container = client.containers.get(old_name)
            container.stop()
            container.remove()
            run_container(new_opts, new_path)
            cont["options"], cont["docker_path"] = new_opts, new_path
            cont["port"], cont["public_url"] = new_port, new_url
            update_copy(containers)
            with open(config_path, "w") as conf:
                yaml.dump(containers, conf)
            update_timestamp(os.stat(config_path).st_mtime)
            break


def run_container(options=None, dock_path=None):
    client = docker.from_env()
    imgs = client.images
    conts = client.containers
    # if conf_cont:
    #     options, dock_path, port, pub_url = conf_cont.values()
    # name = int(pub_url[17:])
    # build image
    cont_image = imgs.build(path=dock_path)[0]
    # create container
    conts.run(image=cont_image, **options)
    print(f"Container {options['name']} run!")


def add_container(options, dock_path, port, pub_url):
    cont_config = {
        "options": options,
        "docker_path": dock_path,
        "port": port,
        "public_url": pub_url,
    }

    containers = get_all_containers()
    containers.append(cont_config)
    with open(config_path, "w") as conf:
        yaml.dump(containers, conf)
    run_container(options, dock_path)
    update_copy(containers)
    update_timestamp(os.stat(config_path).st_mtime)


def remove_container(name):
    client = docker.from_env()
    container = client.containers.get(name)
    container.stop()
    container.remove()
    containers = get_all_containers()
    containers.remove(get_cont_by_name(name))
    with open(config_path, "w") as conf:
        yaml.dump(containers, conf)
    print(f"Container {name} stopped and removed")
    update_copy(containers)
    update_timestamp(os.stat(config_path).st_mtime)


def update_timestamp(new_stamp):
    with open(os.path.join(os.path.dirname(__file__), "timestamp.txt"), "w") as stamp:
        stamp.write(str(new_stamp))


def update_copy(new_data):
    with open(copy_path, "w") as conf:
        yaml.dump(new_data, conf)


def find_changed_cont_and_update():
    changed_conts = get_all_containers()
    old_conts = get_all_containers(copy_path)
    client = docker.from_env()
    conts = client.containers
    config_timestamp = os.stat(config_path).st_mtime
    if len(changed_conts) == len(old_conts):
        for ind, cont in enumerate(old_conts):
            if changed_conts[ind] != cont:
                container = conts.get(cont["options"]["name"])
                container.stop()
                container.remove()
                new_opts, new_path = (
                    changed_conts[ind]["options"],
                    changed_conts[ind]["docker_path"],
                )
                run_container(new_opts, new_path)
                print(f"Container {cont['options']['name']} changed and re-run!")
                update_copy(changed_conts)
                update_timestamp(config_timestamp)
    elif len(changed_conts) > len(old_conts):
        start_containers()
        update_copy(changed_conts)
        update_timestamp(config_timestamp)
    else:
        for cont in old_conts:
            if cont not in changed_conts:
                container = conts.get(cont["options"]["name"])
                container.stop()
                container.remove()
                update_copy(changed_conts)
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


# path = os.path.join(os.path.dirname(__file__), "copy-config-file.json")
# print(get_all_containers())
# print(get_all_containers(path))
# timestamp = os.stat(path).st_mtime
# while True:
#     if copy_config_file != get_all_containers():
#         print("They differents")
# watch_file_update()
"""
config = {
        "docker_path": "/home/tim/TestsProjects/Flask/DemoDocker/app_1",
        "options": {
                    "ports": {7000: 7777},
                    "detach": True
                    },
        "port": 7000,
        "public_url": "http://localhost:7777"
    }
options = {
        "name": "timmy-test-server",
        "ports": {7000: 7777},
        "detach": True
}
client = docker.from_env()
imgs = client.images
conts = client.containers
name, dock_path = options["name"], config["docker_path"]
# build image
cont_image = imgs.build(path=dock_path)[0]
# create container
conf_options = config["options"]
container = conts.run(image=cont_image, **conf_options)
print(f"Container {name} run!")
print(container.name)
"""
