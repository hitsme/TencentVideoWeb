from flask import Flask,render_template,request,jsonify
from spiderStudio import spiderStidio
app = Flask(__name__)
browser=spiderStidio.browser


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/additem', methods=['POST'])
def additem():
    print(request.form.get("videourl")+"4324234234")
    realurl=spiderStidio.getYourVideoUrl(browser,request.form.get("videourl"))
    return jsonify({"result":realurl})
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8888,
        debug=True
    )
