from flask import Flask, request, make_response, jsonify, abort, render_template
from produce.fill_queue import publish_to_queue
import os
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.debug = True


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/', methods=['GET', 'POST'])
def form_example():
    logging.warning(request)
    if request.method == 'POST':
        parameter_list = list()
        print("request" + str(request))

        parameters = request.form.get('parameters')
        print("parametersparametersparametersparameters" + str(parameters))
        parameter2 = request.args.get('parameters')
        print("parametersparametersparametersparameters" + str(parameter2))

        parameter_list.append(parameters)
        result = publish_to_queue(parameter_list)

        return '''<h1>The given parameters are added to the queue!</h1>'''

    if request.method == 'GET':
        return render_template("main.html")
    return abort(400)


if __name__ == '__main__':
    os.environ["FLASK_DEBUG"] = "1"
    app.run(debug=True, host='0.0.0.0', port=5000)
