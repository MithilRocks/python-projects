from flask import Flask 
from flask_pymongo import PyMongo 
import urllib

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'posts'
app.config['MONGO_URI'] = 'mongodb://mithilb:' + urllib.parse.quote_plus('mithil@92') + '@ds121871.mlab.com:21871/posts'

mongo = PyMongo(app)

@app.route('/add')
def add():
    user = mongo.db.users
    user.insert({"name":"Mithil"})
    return "Added user!"

if __name__ == "__main__":
    app.run(debug=True)