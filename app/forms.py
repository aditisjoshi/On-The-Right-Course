from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired

class Inputs(Form):
    openid = StringField('openid', validators=[DataRequired()])
    myField = SelectField(u'Major', choices = [('meche', 'MechE'), ('ece', 'ECE'), ('design', 'E:Design'), ('bio', 'E:Bio'), ('matsci', 'E:MatSci'), ('robo', 'E:Robo'), ('systems', 'E:Systems')])

