from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class AgentForm(FlaskForm):
    agent_name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    agent_phone = StringField('Phone', validators=[DataRequired(), Length(max=50)])
    agent_email = StringField('Email', validators=[Length(max=50)])
    submit = SubmitField('Save')