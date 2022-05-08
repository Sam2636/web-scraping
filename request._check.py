#https://reqres.in/api/user/2

import requests
import ngrok
pk={"dsdf":"uhu","cwecwe":"cewc"
}

er=requests.post("https://data.mongodb-api.com/app/61dbe1e96ce5d97556e9676c/endpoint/data/beta/action/post",params=pk)

print(er)

from pyngrok import ngrok

# Open a HTTP tunnel on the default port 80
# <NgrokTunnel: "http://<public_sub>.ngrok.io" -> "http://localhost:80">
http_tunnel = ngrok.connect()
# Open a SSH tunnel
# <NgrokTunnel: "tcp://0.tcp.ngrok.io:12345" -> "localhost:22">
ssh_tunnel = ngrok.connect(22, "tcp")