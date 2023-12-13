from flask import Blueprint

your_blueprint = Blueprint('effectivestress', __name__)

# 將視圖和其他設定加入 Blueprint
from . import views, form