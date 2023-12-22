# views.py
from flask import Blueprint, render_template, redirect, url_for
from .form import soilparameter

your_blueprint = Blueprint('effectivestress', __name__)

@your_blueprint.route('/input', methods=['GET', 'POST'])
def input():
    form = soilparameter()

    if form.validate_on_submit():
        # 在這裡處理表單提交的邏輯
        e_value = form.e.data
        Gs_value = form.Gs.data
        w_value = form.w.data
        S_value = form.S.data
        gammas_value = form.gammas.data
        gammad_value = form.gammad.data
        gammam_value = form.gammam.data
        gammaw = 1000

        if gammad is None and gammam is None:
            e, Gs, w, S = calculate_poreparameters(e, Gs, w, S) 
            gammad = Gs* gammaw/(1+e)
            gammam = Gs* gammaw*(1+w)/(1+e)  
        elif gammad is None:
            gammam, Gs, w, e = calculate_gammamparameters(gammam, Gs, w, e)
            e, Gs, w, S = calculate_poreparameters(e, Gs, w, S)
            gammad = Gs* gammaw/(1+e)
        elif gammam is None and any(param is None for param in [gammad, Gs, e]):
            gammad, Gs, e = calculate_gammadparameters(gammad, Gs, e)
            e, Gs, w, S = calculate_poreparameters(e, Gs, w, S)
            gammam = Gs* gammaw*(1+w)/(1+e) 
        elif gammam is None and all(param is not None for param in [gammad, Gs, e]):
            if any(param is not None for param in [w ,S ]):
                e, Gs, w, S = calculate_poreparameters(e, Gs, w, S)
                gammam = Gs* gammaw*(1+w)/(1+e)
            else :
                return render_template("input.html", item1=Gs, item2=w, item3=S, item4=e, item5 = gammad, item6 = gammam, item7 =gammas, item8 ='the input is NOT enough')
        return render_template("output.html", item1=Gs, item2=w, item3=S, item4=e, item5 = gammad, item6 = gammam,item7 =gammas)
        





        return redirect(url_for('your_blueprint.example'))
        #上面這行回傳 理論上應該是要渲染正確提交後的模板，目前先放著，且整個計算函數都在上面這個框框中要完成

    return render_template('example_template.html', form=form)
