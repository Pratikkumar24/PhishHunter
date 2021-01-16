from flask_api import FlaskAPI
from flask import request,jsonify
from flask_cors import CORS

from Main import start


app = FlaskAPI(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app)
app.config["DEBUG"] = True #False in Production

@app.route('/',methods=['GET','POST'])
def example():
    try:
        url = request.data['url']
        # print("\n The url: "+ url)
        res = start(url)
        
        return {'response': res}
    except:
        return {'response': 'something went wrong'}


app.run()