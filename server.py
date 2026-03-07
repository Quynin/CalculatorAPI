#Import flask libraries for Python REST Server
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app) #allow CORS for all domains on all routes
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/ping', methods=['GET'])
@cross_origin()
def ping():
    #Access query params from request
    user_id = request.args.get('user_id', default=1, type=int)
    print(user_id)

     #Get ping data to return
    data = {
        'message': 'MEOWWWWW',
        'user_id': user_id,
        'data_source': 'example_db'
    }

    return data

@app.route('/api/calc', methods=['GET'])
@cross_origin()
def perform_calc():
    #Access query params from request
    user_id = request.args.get('user_id', default=1, type=int)
    print(user_id)
    calc_string = request.args.get('calc_string', default="")
    print(calc_string)


    data = {}
    try:
        result = eval(calc_string)
        print(f'={result}')
        #Build data to return
        data = {
            'result': result,
        }
    except Exception as e:
        error = e
        #JSON data with error
        data = {
            'result': result,
            'error': error
        }

    return data

if __name__ == 'main':
    #Run server
    #Can be accessed at http://127.0.0.1
    app.run(debug=True)