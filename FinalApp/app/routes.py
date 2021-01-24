import ast

from app import app
from app.containers import (
    add_container,
    change_container,
    get_all_containers,
    get_cont_by_name,
    remove_container,
    start_containers,
    watch_file_update,
)
from app.forms import Buttons, ContainerForm
from flask import Flask, flash, redirect, render_template, request, url_for

start_containers()


@app.route("/", methods=["GET", "POST"])
def containers():
    watch_file_update()
    form = Buttons()
    conts = get_all_containers()
    if form.validate_on_submit():
        return redirect(url_for("add"))
    return render_template("containers.html", conts=conts, form=form)


@app.route("/")
@app.route("/cont/<cont_name>", methods=["GET", "POST"])
def cont(cont_name):
    cont = get_cont_by_name(cont_name)
    form = Buttons()
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
        if not form.options.data:
            form.options.data = "{}"
        new_opts, new_path = ast.literal_eval(form.options.data), form.dock_path.data
        new_port, new_url = form.port.data, form.pub_url.data
        change_container(cont_name, new_opts, new_path, new_port, new_url)
        flash(f"Changes requested for container {new_opts['name']} applied!")
        return redirect(url_for("cont", cont_name=new_opts["name"]))
    elif request.method == "GET":
        form.options.data = cont["options"]
        form.dock_path.data = cont["docker_path"]
        form.port.data = cont["port"]
        form.pub_url.data = cont["public_url"]
    return render_template("changes.html", title="Change container", form=form)


@app.route("/")
@app.route("/add", methods=["GET", "POST"])
def add():
    form = ContainerForm()
    if form.validate_on_submit():
        new_opts = ast.literal_eval(form.options.data)
        new_path = form.dock_path.data
        new_port, new_url = form.port.data, form.pub_url.data
        container = add_container(new_opts, new_path, new_port, new_url)
        flash(f"Add and run new container {container.name}!")
        return redirect(url_for("cont", cont_name=container.name))
    elif request.method == "GET":
        form.options.data = "{}"
    return render_template("changes.html", title="Add new container", form=form)
