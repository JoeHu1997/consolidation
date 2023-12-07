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
    Gs = request.form.get("item1")
    w = request.form.get("item2")
    S = request.form.get("item3")
    e = request.form.get("item4")
    parameters = [e, Gs, w, S]
    # 定義提供的參數集合
    provided_params = ['e', 'Gs', 'w', 'S']
    # 檢查每個值是否為空
    for param_name, param_value in zip(provided_params, parameters):
        if param_value is None or param_value == "":
            if param_name == 
            print(f"Error: {param_name} is empty.")
    print(parameters)
    
    return "work"
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