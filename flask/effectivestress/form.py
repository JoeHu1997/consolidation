from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class soilparameters(FlaskForm):
    e = FloatField('e')
    Gs = FloatField('Gs')
    w = FloatField('w')
    S = FloatField('S')
    gammad = FloatField('gammad')
    gammam = FloatField('gammam')
    






#'e', 'Gs', 'w', 'S', 'gammas', 'gammad', 'gammam'