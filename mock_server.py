from flask import Flask

app = Flask(__name__)

mock_data_1 = {"data":{"aprovadores":[{"representnates":[{"documento":"81517468078"},{"documento":"22582334022"}]},{"representnates":[{"documento":"81517468078"},{"documento":"52489892053"}]},{"representnates":[{"documento":"81517468078"},{"documento":"11527478009"}]},{"representnates":[{"documento":"64756598005"},{"documento":"22582334022"}]},{"representnates":[{"documento":"64756598005"},{"documento":"52489892053"}]},{"representnates":[{"documento":"64756598005"},{"documento":"11527478009"}]},{"representnates":[{"documento":"41899190040"},{"documento":"22582334022"}]},{"representnates":[{"documento":"41899190040"},{"documento":"52489892053"}]},{"representnates":[{"documento":"41899190040"},{"documento":"11527478009"}]}]}}


@app.route('/get_1')
def hello_world():
    return mock_data_1


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
