import ast
import re

import docker
from app import app
from app.containers import (
    add_container,
    change_container,
    check_port_in_options,
    check_port_in_pub_url,
    get_all_containers,
    get_cont_by_name,
    remove_container,
    start_containers,
    watch_file_update,
)
from app.forms import AddContainerForm, Buttons, ContainerForm
from flask import Flask, flash, redirect, render_template, request, url_for


def pre_checking():
    try:
        start_containers()
        return True
    except docker.errors.APIError as f:
        if "port is already allocated" in f.explanation:
            return docker.errors.APIError(
                "Invalid port in config-file. Port is already allocated. "
                "Please, choose another port in config-file"
            )
        elif ("The container name" and "is already in use") in f.explanation:
            return docker.errors.APIError(
                "Container name is already in use. "
                "Please, choose another container name in config-file"
            )


@app.route("/", methods=["GET", "POST"])
def containers():
    check = pre_checking()
    form = Buttons()
    conts = get_all_containers()
    if check is not True:
        print(check)
        return render_template("errors.html", error=check)
    if form.validate_on_submit():
        return redirect(url_for("add"))
    return render_template("containers.html", conts=conts, form=form)


@app.route("/")
@app.route("/cont/<cont_name>", methods=["GET", "POST"])
def cont(cont_name):
    check = pre_checking()
    cont = get_cont_by_name(cont_name)
    form = Buttons()
    if check is not True:
        print(check)
        return render_template("errors.html", error=check)
    if form.edit.data:
        return redirect(url_for("change", cont_name=cont_name))
    elif form.remove.data:
        return redirect(url_for("remove", cont_name=cont_name))
    return render_template("cont.html", cont=cont, form=form)


@app.route("/")
@app.route("/remove/<cont_name>", methods=["GET", "POST"])
def remove(cont_name):
    cont_name = cont_name
    remove_container(cont_name)
    flash(f"Container {cont_name} stopped and removed")
    return redirect("/")


@app.route("/")
@app.route("/change/<cont_name>", methods=["GET", "POST"])
def change(cont_name):
    cont = get_cont_by_name(cont_name)
    form = ContainerForm()
    if form.validate_on_submit():
        try:
            port = int(re.search(r"http://localhost:(\d*)", form.pub_url.data).group(1))
            check_port_in_pub_url(cont_name, port)
            check_port_in_options(cont_name, ast.literal_eval(form.options.data))
            new_name = form.cont_name.data
            new_opts, new_path = (
                ast.literal_eval(form.options.data),
                form.dock_path.data,
            )
            new_port, new_url = form.port.data, form.pub_url.data
            rerun_cont = change_container(
                cont_name, new_name, new_opts, new_path, new_port, new_url
            )
            flash(f"Changes requested for container {rerun_cont.name} applied!")
            return redirect(url_for("cont", cont_name=rerun_cont.name))
        except docker.errors.APIError as er:
            if er.explanation:
                er = "Container name is already in use. Please, choose another container name"
            flash(f"An ERROR! {er}")
            return redirect(url_for("change", cont_name=cont_name))
    elif request.method == "GET":
        form.cont_name.data = cont["name"]
        form.options.data = cont["options"]
        form.dock_path.data = cont["docker_path"]
        form.port.data = cont["port"]
        form.pub_url.data = cont["public_url"]
    return render_template("changes.html", title="Change container", form=form)


@app.route("/")
@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddContainerForm()
    if form.validate_on_submit():
        new_name = form.cont_name.data
        new_opts = ast.literal_eval(form.options.data)
        new_path = form.dock_path.data
        new_port, new_url = form.port.data, form.pub_url.data
        container = add_container(new_name, new_opts, new_path, new_port, new_url)
        flash(f"Add and run new container {container.name}!")
        return redirect(url_for("cont", cont_name=container.name))
    elif request.method == "GET":
        form.options.data = "{}"
    return render_template("changes.html", title="Add new container", form=form)
