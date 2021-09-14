from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle

import ml_fit
import ml
import numpy as np

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])  # route to display the home page
@cross_origin()
def homePage():
    try:
        result = str()
        if request.method == "POST":
            air_temp = request.form["air_temp"]
            process_temp = request.form["process_temp"]
            rotational_speed = request.form["rotational_speed"]
            torque = request.form["torque"]
            tool_wear = request.form["tool_wear"]
            tool_wear_time = request.form["tool_wear_time"]

            values = ml.ml_trails(air_temp,process_temp,rotational_speed,torque,tool_wear,tool_wear_time)

            ml_fit.instance_fit()

            file = "linear_reg.sav"
            saved_model = pickle.load(open(file, 'rb'))

            failure = saved_model.predict(np.array([values]))

            if failure > 0.05:
                result = "Machine process Will Fail"
            else:
                result = "Machine process is Fine"

    except Exception as e:
        raise Exception(" Something went wrong" + str(e))
    return render_template("index.html", result=result)


@app.route("/profile", methods=["POST", "GET"])
@cross_origin()
def homePage1():
    if request.method == "POST":
        return render_template("test_case_profiling.html")
    else:
        return render_template('test_case_profiling.html')


if __name__ == "__main__":
    app.run(debug=True)
