# predict code
# import joblib
# import pandas as pd
# model = joblib.load("./model_MLP_SGD_fitted.pkl")
# print(model.predict(pd.DataFrame([[1,79,1,83.75,28.4]])))
import joblib
import pandas as pd
from flask import Flask,url_for,request,jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return """Welcome to our webset!</br>
    You can get help page with <b>/help</b>."""

@app.route("/help")
def help():
    return """
    The usage of this api is <i>URL</i>:5000/data</br>
    You can query the server with your following physical data.</br>
    <table>
    <th>gender</th><th>male is 0(default), female is 1</th></tr>
    <th>age</th><th>integer</th></tr>
    <th>hypertension</th><th>low is 0(default), high is 1</th></tr>
    <th>glu</th><th>float</th></tr>
    <th>bmi</th><th>float</th></tr>
    </table>
    <b>example</b> http://127.0.0.1:5000/data?glu=200.3&bmi=40&age=50
    """


@app.route("/data")
def judge():
    gender = request.args.get("gender",default=0,type = int)
    age = request.args.get("age",default=25,type=int)
    hypertension = request.args.get("hypertension",default=0,type=int)
    glu = request.args.get("glu",default=50,type=float)
    bmi = request.args.get("bmi",default=25,type=float)
    model = joblib.load("./model_MLP_SGD_fitted.pkl")
    stroke = model.predict(pd.DataFrame([[gender,age,hypertension,glu,bmi]]))
    return jsonify({
        "gender": ['male' if gender == 0 else "female"],
        "age": age,
        "hypertension": ["high" if hypertension == 1 else "low"],
        "glu": str(glu)+" mg/dL ",
        "bmi": bmi,
        "stroke": ["dangerous" if stroke == 1 else "not dangerous"]
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0")