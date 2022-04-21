from pymongo import MongoClient
client = MongoClient('클러스터 URL')
db = client.team

from flask import Flask, render_template, request, jsonify, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getPerson1')
def getpeople1():
    return render_template('personal_test_1.html')

@app.route('/gittin') 
def gittin(): return redirect("https://github.com/kti0940")

@app.route('/blgtin')
def blgtin(): return redirect("https://velog.io/@kti0940")

@app.route('/getPerson2')
def getpeople2():
    return render_template('personal_test_2.html')

@app.route('/gitfr') 
def gitfr(): return redirect("https://github.com/KimmyJay")

@app.route('/blgfr') 
def blgfr(): return redirect("https://frannyk.tistory.com/")

@app.route('/getPerson3')
def getpeople3():
    return render_template('personal_test_3.html')

@app.route('/gitmun') 
def gitmun(): return redirect("https://github.com/ansaudwn1234")

@app.route('/blggmun') 
def blgmun(): return redirect("https://velog.io/@ansaudwn123")

@app.route('/getPerson4')
def getpeople4():
    return render_template('personal_test_4.html')

@app.route('/gitgh') 
def gitgh(): return redirect("https://github.com/soiyo")

@app.route('/blggh') 
def blggh(): return redirect("https://velog.io/@soyoyun")


@app.route("/profile", methods=["POST"])
def web_post():
    name_receive = request.form['name_give']
    hi_receive = request.form['hi_give']
   
    doc = { 
        'name':name_receive,
        'hi':hi_receive,
    }
    db.introduce.insert_one(doc)
    return jsonify({'msg': '작성완료!'})

@app.route("/profile", methods=["GET"])
def web_get():
    intro_list = list(db.introduce.find({},{'_id':False})) 
    return jsonify({'intro': intro_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)