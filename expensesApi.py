from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello', methods=['GET'])
def hello_world():
    """
    Hello World endpoint
    ---
    responses:
      200:
        description: A hello world message
    """
    return jsonify(message="Hello, World!")

@app.route('/add', methods=['POST'])
def add_numbers():
    """
    Add two numbers
    ---
    parameters:
      - name: payload
        in: body
        type: object
        required: true
        schema:
          type: object
          properties:
            x:
              type: integer
              example: 56
              description: The first number
            y:
              type: integer
              example: 30
              description: The second number
    responses:
      200:
        description: The sum of x and y
        schema:
          type: object
          properties:
            sum:
              type: integer
    """
    data = request.json
    x = data['x']
    y = data['y']
    return jsonify(sum=x + y)



@app.route('/example', methods=['POST'])
def example_post():
    """
    Example endpoint to demonstrate setting MIME type
    ---
    tags:
      - example
    parameters:
      - name: payload
        in: body
        type: object
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: "John"
            age:
              type: integer
              example: 30
    responses:
      200:
        description: success
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Data received successfully."
    """
    data = request.json
    # Process your data here
    return {"message": "Data received successfully."}, 200


if __name__ == '__main__':
    app.run(debug=True)