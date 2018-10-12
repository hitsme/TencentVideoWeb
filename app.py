from flask import Flask,render_template,request,jsonify
from tools import pcOrmobile
from spiderStudio import spiderStidio
#import threading
app = Flask(__name__)
browser=spiderStidio.browser
#R=threading.Lock()

@app.route('/')
def home():
    if pcOrmobile.pc_or_mobile(str(request.user_agent)):
       return render_template("indexmobile.html")
    else:
        return render_template("index.html")
@app.route('/options')
def options():
    return render_template("options.html")
@app.route('/jz')
def jz():
    return render_template("jz.html")
@app.route('/additem', methods=['POST'])
def additem():
    print(request.form.get("videourl")+"4324234234")
    #R.acquire()
    realurl=spiderStidio.getYourVideoUrl(browser,request.form.get("videourl"))
    #R.release()
    return jsonify({"result":realurl})
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=80,
        debug=False
    )
