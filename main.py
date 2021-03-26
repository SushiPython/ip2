from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def main():
  ip = request.headers.get('Cf-Connecting-Ip')
  if ip is None:
    return render_template('error.html')
  else:
    return redirect('/ip?addr='+ip, 302)


@app.route('/ip')
def ip():
  addr = request.args.get('addr')
  response = requests.get('http://ip-api.com/json/'+addr).json()
  rnd_items = {
    'lat': round(response['lat'], 3),
    'lon': round(response['lon'], 3)
  }
  return render_template('index.html', data=response, rnd_items=rnd_items)

app.run(host='0.0.0.0', port=8080)