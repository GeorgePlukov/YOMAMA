# -*- coding: utf-8 -*-

from flask import request, Flask
import requests
import config
YO_API_TOKEN = config.devKey

app = Flask(__name__)


@app.route("/yo/")
def yo():

    # extract and parse query parameters
    username = request.args.get('username')

 #  print "We got a Yo from " + username
    joke = username + " joke"
    # Yo the result back to the user
    requests.post("http://api.justyo.co/yo/", data={'api_token': YO_API_TOKEN, 'username': username, 'link': 'http://54.86.232.229/YOMAMA/'})
#'http://www.yotext.co/show/?text=' + joke}
    # OK!
    return 'OK'


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5000)


    # where yo at