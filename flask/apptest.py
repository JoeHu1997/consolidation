from flask import Flask, request, render_template

app = Flask(__name__,
            static_folder="static",   #靜態檔案的「資料夾」名稱
            static_url_path="/static"
            )

@app.route("/")
def home():
    name = request.args.get('name')
    return render_template('test.html', name=name)

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
app.run(host="0.0.0.0")