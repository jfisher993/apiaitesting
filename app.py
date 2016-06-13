#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "apiaitest":
        return {}
   #  baseurl = "https://query.yahooapis.com/v1/public/yql?"
   #  yql_query = makeYqlQuery(req)
   #  if yql_query is None:
   #     return {}
   #  yql_url = baseurl + urllib.urlencode({'q': yql_query}) + "&format=json"

   #  result = urllib.urlopen(yql_url).read()

    data = json.loads(req)
    res = makeWebhookResult(data, req)
    return res


# def makeYqlQuery(req):
#     result = req.get("result")
#     parameters = result.get("parameters")
#     city = parameters.get("geo-city")
#     if city is None:
#         return None

#     return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "')"

def makeWebhookResult(data, req):
    # query = data.get('query')
    # if query is None:
    #     return {}

    # result = query.get('results')
    # if result is None:
    #     return {}

    # channel = result.get('channel')
    # if channel is None:
    #     return {}

    # item = channel.get('item')
    # location = channel.get('location')
    # units = channel.get('units')
    # if (location is None) or (item is None) or (units is None):
    #     return {}

    # condition = item.get('condition')
    # if condition is None:
    #     return {}

    result = req.get("result")
	parameters = result.get("parameters")
    programming = parameters.get("programming")

    if (programming == "python"):
    	speech = "You snake"
    else:
    	speech = "I am not a fan of " + programming

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {"slack": slack_message},
        "data": {"facebook": speech},
        "source": "FisherTestApp"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    app.run(debug=False, port=port, host='0.0.0.0')