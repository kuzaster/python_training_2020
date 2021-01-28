import ast
import re

import docker
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError

client = docker.from_env()
conts = client.containers


def check_public_url(form, field):
    pub_url = re.search(r"(http://localhost:\d+)", field.data)
    if not pub_url or field.data != pub_url.group(1):
        raise ValidationError(
            "Public URL should be in form: 'http://localhost:<free host port>'"
        )


def check_options(form, field):
    if not field.data:
        raise ValidationError("This fill couldn't be empty. Please fill with: {}")
    elif not isinstance(ast.literal_eval(field.data), dict):
        raise ValidationError(
            "This field should be in form: {option_1: value_1, option_2: value_2, etc}"
        )


def check_existing_name(form, field):

    if conts.list(all=True, filters={"name": field.data}):
        raise ValidationError("This container name is already in use. Change this name")


def check_free_port(cont_name, port):
    # port = int(re.search(r"http://localhost:(\d*)", field.data).group(1))
    for container in conts.list(all=True, filters={"publish": port}):
        if container.name != cont_name:
            raise ValidationError(
                f"Port {port} is already allocated. Please, choose another port"
            )


class ContainerForm(FlaskForm):
    cont_name = StringField("ContainerName", validators=[DataRequired()])
    options = TextAreaField("Options", validators=[check_options])
    dock_path = StringField("DockerPath", validators=[DataRequired()])
    port = IntegerField("Port", validators=[DataRequired()])
    pub_url = StringField("PublicURL", validators=[DataRequired()])
    submit = SubmitField("Apply changes")

    def __init__(self, original_cont_name, *args, **kwargs):
        super(ContainerForm, self).__init__(*args, **kwargs)
        self.original_cont_name = original_cont_name

    def validate_options(self, options):
        options = ast.literal_eval(options.data)
        if "ports" not in options:
            return
        cont_port = list(options["ports"])
        if self.port.data not in cont_port:
            print(cont_port)
            raise ValidationError(
                f"Ports {cont_port} should contain port {self.port.data}"
            )
        host_ports = options["ports"].values()
        for port in host_ports:
            if isinstance(port, list):
                for p in port:
                    check_free_port(self.original_cont_name, p)
            check_free_port(self.original_cont_name, port)

    def validate_cont_name(self, cont_name):
        if cont_name.data != self.original_cont_name:
            check_existing_name(self, cont_name)

    def validate_pub_url(self, pub_url):
        check_public_url(self, pub_url)
        port = int(re.search(r"http://localhost:(\d*)", pub_url.data).group(1))
        check_free_port(self.original_cont_name, port)


class AddContainerForm(FlaskForm):
    cont_name = StringField(
        "ContainerName", validators=[DataRequired(), check_existing_name]
    )
    options = TextAreaField("Options", validators=[check_options])
    dock_path = StringField("DockerPath", validators=[DataRequired()])
    port = IntegerField("Port", validators=[DataRequired()])
    pub_url = StringField("PublicURL", validators=[DataRequired()])
    submit = SubmitField("Add and run container")

    def validate_pub_url(self, pub_url):
        check_public_url(self, pub_url)
        port = int(re.search(r"http://localhost:(\d*)", pub_url.data).group(1))
        if conts.list(all=True, filters={"publish": port}):
            raise ValidationError(
                f"Port {port} is already allocated. Please, choose another port"
            )


class Buttons(FlaskForm):
    edit = SubmitField("Edit container")
    add = SubmitField("Add new container")
    remove = SubmitField("Remove container")
