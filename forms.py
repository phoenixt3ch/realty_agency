from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class AgentForm(FlaskForm):
    agent_name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    agent_phone = StringField('Phone', validators=[DataRequired(), Length(max=50)])
    agent_email = StringField('Email', validators=[Length(max=50)])
    submit = SubmitField('Save')

class ClientForm(FlaskForm):
    client_name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    client_phone = StringField('Phone', validators=[DataRequired(), Length(max=50)])
    client_email = StringField('Email', validators=[Length(max=50)])
    submit = SubmitField('Save')

class RealtyForm(FlaskForm):
    realty_address = StringField('Address', validators=[DataRequired(), Length(max=50)])
    realty_square = FloatField('Square', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Save')

class RentForm(FlaskForm):
    agent_id = IntegerField('Agent ID', validators=[DataRequired()])
    realty_id = IntegerField('Realty ID', validators=[DataRequired()])
    client_id = IntegerField('Client ID', validators=[DataRequired()])
    rent_beginning_date = DateField('Rent Beginning Date', validators=[DataRequired()])
    rent_ending_date = DateField('Rent Ending Date', validators=[Optional()])
    rent_price = FloatField('Rent Price', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Save')

class SalesForm(FlaskForm):
    agent_id = IntegerField('Agent ID', validators=[DataRequired()])
    realty_id = IntegerField('Realty ID', validators=[DataRequired()])
    client_id = IntegerField('Client ID', validators=[DataRequired()])
    sale_date = DateField('Sale Date', validators=[DataRequired()])
    sale_price = FloatField('Sale Price', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Save')