from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,SubmitField
from wtforms.validators import DataRequired,Length,NumberRange

class Userform(FlaskForm):
    name= StringField('Name',validators=[DataRequired(),Length(min=3,max=50)],render_kw={'class':'form-control'})
    age = StringField('Age',validators=[DataRequired()])
    submit=SubmitField('Submit')