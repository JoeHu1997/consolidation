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
    parameters = [e, Gs, w, S]

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

    #兩種土壤密度建立
    gammad = Gs*gammaw/(1+e)
    gammam = Gs*gammaw*(1+w)/(1+e)
    gammas = Gs*gammaw 
    return render_template("output.html", item1=Gs, item2=w, item3=S, item4=e, item5 = gammad, item6 = gammam)

@app.route("/polecalculater2", methods=["POST"])
def polecalculater2():
    #讀取參數
    Gs_str = request.form.get("item1")
    w_str = request.form.get("item2")
    S_str = request.form.get("item3")
    e_str = request.form.get("item4")
    gammas_str = request.form.get("item5")
    gammad_str = request.form.get("item6")
    gammam_str = request.form.get("item7")
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


    for param_name, param_value in zip(provided_params, parameters):
        if param_value is None or param_value == "":


#共享函數
def convert_to_int(value_str):
    try:
       return int(value_str) if value_str is not None else None
    except ValueError:
        return None
#app.debug = True
app.run(host='0.0.0.0')