import ast
import re

import docker
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError


class Buttons(FlaskForm):
    edit = SubmitField("Edit container")
    add = SubmitField("Add new container")
    remove = SubmitField("Remove container")


def check_public_url(form, field):
    if field.data != re.search(r"(http://localhost:\d*)", field.data).group(1):
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
    client = docker.from_env()
    conts = client.containers
    if conts.list(all=True, filters={"name": field.data}):
        raise ValidationError("This container name is already in use. Change this name")


def check_free_port(form, field):
    client = docker.from_env()
    conts = client.containers
    port = int(re.search(r"http://localhost:(\d*)", field.data).group(1))
    if conts.list(all=True, filters={"publish": port}):
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


class AddContainerForm(FlaskForm):
    cont_name = StringField(
        "ContainerName", validators=[DataRequired(), check_existing_name]
    )
    options = TextAreaField("Options", validators=[check_options])
    dock_path = StringField("DockerPath", validators=[DataRequired()])
    port = IntegerField("Port", validators=[DataRequired()])
    pub_url = StringField(
        "PublicURL", validators=[DataRequired(), check_public_url, check_free_port]
    )
    submit = SubmitField("Add and run container")
