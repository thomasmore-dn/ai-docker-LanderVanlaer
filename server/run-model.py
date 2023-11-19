import json
import pickle

from flask import Flask, request, make_response

app = Flask(__name__)

# noinspection PickleLoad
model = pickle.load(open('./imports/model.pkl', 'rb'))


@app.route('/')
def index():
    return "Status ok!"


# noinspection PyPep8Naming
@app.route('/predict')
def predict():
    x_unparsed = request.args.get('X')

    if x_unparsed is None:
        return {"error": "X is required"}, 400

    try:
        x = json.loads(x_unparsed)
    except json.decoder.JSONDecodeError as e:
        return {"error": str(e)}, 400

    if not isinstance(x, list):
        return {"error": "X must be a list"}, 400

    if len(x) != 64:
        return {"error": "X must have 64 elements"}, 400

    if not all(isinstance(i, int) for i in x):
        return {"error": "X must be a list of integers"}, 400

    if not all(0 <= i <= 16 for i in x):
        return {"error": "X must be a list of integers between 0 and 16"}, 400

    y = model.predict([x])[0]
    response = make_response(str(y), 200)
    response.mimetype = "text/plain"
    return response


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=8080)
