from flask import Blueprint


your_blueprint = Blueprint('effectivestress', __name__)

from utils.common_functions import calculate_poreparameters, calculate_gammamparameters, calculate_gammadparameters
# 將視圖和其他設定加入 Blueprint
from . import views, form