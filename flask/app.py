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
    print(parameters)    
    return render_template("output.html", item1=Gs, item2=w, item3=S, item4=e)
@app.route("/head")
def index():
    '''
    print("請求方法:", request.method)   #(物件.屬性)
    print("通訊協定 :", request.scheme)   
    print("主機名稱 :", request.host)
    print("路徑 :",request.path)
    print("完整的網址 :",request.url)
    '''
    print("瀏覽器何作業系統 :", request.headers.get("user-agent")) 
    print("語言偏好 :", request.headers.get("accept-language"))
    print("引薦網址", request.headers.get("referrer"))
    return "Hello Flask"

@app.route("/posttest",methods=['POST'])
def home2():
    print(request.form)            # 使用 request.form
    return "<h1>hello world</h1>"


#get的路由模板
@app.route('/data/appInfo/<name>', methods=['GET'])
def queryDataMessageByName(name):
    print("type(name) : ", type(name))
    return 'String => {}'.format(name)

@app.route('/data/record',methods=['GET','POST'])
def login():
    #  利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
                          #  利用request取得表單欄位值
        return 'Hello ' + request.values['username']
    
    #  非POST的時候就會回傳一個空白的模板
    return render_template('login.html')
app.debug = True
app.run(port=5000)