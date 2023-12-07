
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://aszx11112:aszx2222@cluster0.cygbwu0.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)


# 選擇操作 test 資料庫
db = client.test
Collection = db.users  # 選擇操作users 集合
# 把資料新增到集合中
Collection.insert_one({
    "name": "chichi",
    "gender": "男生"
    })
print("success~!")
