from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class Buttons(FlaskForm):
    edit = SubmitField("Edit container")
    add = SubmitField("Add new container")
    remove = SubmitField("Remove container")


class ContainerForm(FlaskForm):
    # cont_name = StringField('ContainerName', validators=[DataRequired()])
    options = TextAreaField("Options")
    dock_path = StringField("DockerPath", validators=[DataRequired()])
    port = IntegerField("Port", validators=[DataRequired()])
    pub_url = StringField("PublicURL", validators=[DataRequired()])
    submit = SubmitField("Apply changes")


class AddContainerForm(ContainerForm):
    submit = SubmitField("Add and run container")
