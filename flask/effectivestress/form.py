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
    gammas = FloatField('gammas')
#form 建立到這邊就好了 接下來可以先處理views 在視情況調整

    






#'e', 'Gs', 'w', 'S', 'gammas', 'gammad', 'gammam'