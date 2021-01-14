from flask_api import FlaskAPI
from flask import request,jsonify
from flask_cors import CORS

app = FlaskAPI(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app)
app.config["DEBUG"] = True #False in Production

@app.route('/',methods=['GET','POST'])
def example():
    try:
        url = request.data['url']
        print(url)
        res = "Response"
        # res = funName(url)  
        #call your function here
        return {'response': url}
    except:
        return {'detail': 'something went wrong'}


app.run()