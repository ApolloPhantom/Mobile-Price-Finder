import os
import requests
import joblib
from functools import wraps
from flask import *
import numpy as np

model = joblib.load("trained_model.pkl")
app = Flask(__name__)
result = 4

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST","GET"])
def submitter():
    if request.method == "GET":
        return redirect("/")
    else:
        battery_power = int(request.form.get("battery_power"))
        if battery_power <=0:
            return ValueError
        blue = int(request.form.get("blue"))        
        clock_speed = float(request.form.get("clock_speed"))
        if clock_speed <=0:
            return ValueError
        dual_sim = int(request.form.get("dual_sim"))    
        fc = int(request.form.get("fc"))
        if fc <=0:
            return ValueError     
        four_g = int(request.form.get("four_g"))      
        int_memory = int(request.form.get("int_memory"))
        if int_memory <=0:
            return ValueError  
        m_dep = float(request.form.get("m_dep"))
        if m_dep <=0:
            return ValueError 
        mobile_wt = int(request.form.get("mobile_wt"))
        if mobile_wt <=0:
            return ValueError      
        n_cores = int(request.form.get("n_cores"))
        if n_cores <=0:
            return ValueError    
        pc = int(request.form.get("pc"))
        if pc <=0:
            return ValueError       
        px_height = int(request.form.get("px_height"))
        if px_height <=0:
            return ValueError     
        px_width = int(request.form.get("px_width"))
        if px_width <=0:
            return ValueError     
        ram = int(request.form.get("ram"))
        if ram <=0:
            return ValueError        
        sc_h = int((request.form.get("sc_h")))
        if sc_h <=0:
            return ValueError         
        sc_w = int(request.form.get("sc_w"))
        if sc_w <=0:
            return ValueError      
        talk_time = int(request.form.get("talk_time"))
        if talk_time <=0:
            return ValueError  
        three_g = int(request.form.get("three_g"))     
        touch_screen = int(request.form.get("touch_screen")) 
        wifi = int(request.form.get("wifi"))
        single_row_values = [
        battery_power,
        blue,
        clock_speed,
        dual_sim,
        fc,
        four_g,
        int_memory,
        m_dep,
        mobile_wt,
        n_cores,
        pc,
        px_height,
        px_width,
        ram,
        sc_h,
        sc_w,
        talk_time,
        three_g,
        touch_screen,
        wifi
        ]
        input_data = np.array(single_row_values).reshape(1, -1)
        k = model.predict(input_data)
        k = int(k)
        print(k)
        global result
        result = k
        print(result)
        return render_template("result.html",result=result)

@app.route("/res")
def res():
    return render_template("result.html",result=result)

        
      