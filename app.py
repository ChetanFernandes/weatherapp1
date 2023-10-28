from flask import Flask, render_template, request # to get data from form
import requests # to get data from URL
app = Flask(__name__)

@app.route("/")
def render_form():
    return render_template("weather.html")
@app.route("/weatherapp", methods = ['POST','GET'])
def get_data():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
            'q':request.form.get("city"),
            'appid':request.form.get('appid'),
            'units':request.form.get('units')
            }
    response = requests.get(url,params = param)
    data = response.json()['name']
    return f"data: {data}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)