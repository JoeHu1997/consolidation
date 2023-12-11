from flask import Flask, request, render_template

app = Flask(__name__,
            static_folder="static",   #靜態檔案的「資料夾」名稱
            static_url_path="/static"
            )

@app.route("/input")
def input():
    return render_template("input.html")

@app.route("/polecalculater", methods=["POST"])
def polecalculater():
    def convert_to_int(value_str):
        try:
            return int(value_str) if value_str is not None else None
        except ValueError:
            return None
    
    Gs_str = request.form.get("item1")
    w_str = request.form.get("item2")
    S_str = request.form.get("item3")
    e_str = request.form.get("item4")
    gammaw = 1000

    Gs = convert_to_int(Gs_str)
    w = convert_to_int(w_str)
    S = convert_to_int(S_str)
    e = convert_to_int(e_str)
    
    # 定義參數集合
    calculate_poreparameters(e, Gs, w, S)
    """ parameters = [e, Gs, w, S]

    # 定義提供的參數集合
    provided_params = ['e', 'Gs', 'w', 'S']


    for param_name, param_value in zip(provided_params, parameters):
        if param_value is None or param_value == "":
            if param_name == 'e':
                e = Gs*w/S
                print(1)
            elif param_name == 'Gs':
                Gs = S*e/w
                print(2)
            elif param_name == 'w':
                w = S*e/Gs
                print(3)
            else:
                S = Gs*w/e
                print(4)
    """
    #兩種土壤密度建立
    
    return render_template("output.html", item1=Gs, item2=w, item3=S, item4=e)

@app.route("/polecalculater2", methods=["POST"])
def polecalculater2():
    #讀取參數
    Gs_str = request.form.get("item1")
    w_str = request.form.get("item2")
    S_str = request.form.get("item3")
    e_str = request.form.get("item4")
    gammad_str = request.form.get("item5")
    gammam_str = request.form.get("item6")
    gammas_str = request.form.get("item7")
    gammaw = 1000
    #將參數轉成int
    Gs = convert_to_int(Gs_str)
    w = convert_to_int(w_str)
    S = convert_to_int(S_str)
    e = convert_to_int(e_str)
    gammas = convert_to_int(gammas_str)
    gammad = convert_to_int(gammad_str)
    gammam = convert_to_int(gammam_str)

    # 定義參數集合
    parameters = [e, Gs, w, S, gammas, gammad ,gammam]

    # 定義提供的參數集合
    provided_params = ['e', 'Gs', 'w', 'S', 'gammas', 'gammad', 'gammam']


    #for param_name, param_value in zip(provided_params, parameters):
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
#共享函數區
def convert_to_int(value_str):
    try:
       return int(value_str) if value_str is not None else None
    except ValueError:
        return None

def calculate_poreparameters(e, Gs, w, S):
    parameters = [e, Gs, w, S]
    provided_params = ['e', 'Gs', 'w', 'S']

    for param_name, param_value in zip(provided_params, parameters):
        if param_value is None or param_value == "":
            if param_name == 'e':
                e = Gs * w / S
                print(1)
            elif param_name == 'Gs':
                Gs = S * e / w
                print(2)
            elif param_name == 'w':
                w = S * e / Gs
                print(3)
            else:
                S = Gs * w / e
                print(4)
    return e, Gs, w, S
def calculate_gammamparameters(gammam, Gs, w, e):
    parameters = [gammam, Gs, w, e]
    provided_params = ['gammam', 'Gs', 'w', 'e']
#gammam = Gs* gammaw*(1+w)/(1+e)  
    gammaw = 1000
    for param_name, param_value in zip(provided_params, parameters):
        
        if param_value is None or param_value == "":
            if param_name == 'e':
                e = (Gs* gammaw*(1+w)/gammam)-1
                print(1)
            elif param_name == 'gammam':
                gammam = Gs* gammaw*(1+w)/(1+e)  
                print(2)
            elif param_name == 'w':
                w = (gammam*(1+e)/(Gs*gammaw))-1
                print(3)
            else:
                Gs = gammam/(gammaw*(1+w)/(1+e))
                print(4)

    return gammam, Gs, w, e

def calculate_gammadparameters(gammad, Gs, e):
    parameters = [gammad, Gs, e]
    provided_params = ['gammad', 'Gs', 'e']
    #gammad = Gs* gammaw/(1+e)
    for param_name, param_value in zip(provided_params, parameters):
        gammaw = 1000
        if param_value is None or param_value == "":
            if param_name == 'e':
                e = (Gs* gammaw/gammad)-1
                print(1)
            elif param_name == 'gammad':
                gammad = Gs* gammaw/(1+e)  
                print(2)
            elif param_name == 'Gs':
                Gs = gammad/(gammaw/(1+e))
                print(3)
            
    return gammad, Gs, e

app.debug = True
#app.run(host='0.0.0.0')
app.run()
