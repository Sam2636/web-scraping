from flask import Flask ,jsonify
from requests.exceptions import URLRequired
app=Flask(__name__)
from pyngrok import ngrok

@app.route('/')
def home():

    return "hey"

sam=[{
    'name':"sam",
    "ghvg":67
}]

@app.route('/sam')
def get_store():
    return jsonify(sam)



# Open a HTTP tunnel on the default port 80
# <NgrokTunnel: "http://<public_sub>.ngrok.io" -> "http://localhost:80">
http_tunnel = ngrok.connect()
# Open a SSH tunnel
# <NgrokTunnel: "tcp://0.tcp.ngrok.io:12345" -> "localhost:22">
ssh_tunnel = ngrok.connect(22, "tcp")

app.run()    