# -*- coding: utf-8 -*-

from flask import request, Flask
import requests
import config
import Jokes
import random
YO_API_TOKEN = config.devKey

app = Flask(__name__)


@app.route("/yo/")
def yo():
	# get the jokes list from the Jokes file
    jokes = Jokes.jokeList
    # Generate a random number 
    ran = random.randint(0, len(jokes)-1)


    # extract and parse query parameters
    username = request.args.get('username')


     #print "We got a Yo from " + username
    joke = username + " joke"

    # Yo the result back to the user
    requests.post("http://api.justyo.co/yo/", data={'api_token': YO_API_TOKEN, 'username': username, 'link': 'http://www.yotext.co/show/?text=' + jokes[ran]})
#'http://www.yotext.co/show/?text=' + joke}
    # OK!
    return 'OK'


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5000)


    # where yo at