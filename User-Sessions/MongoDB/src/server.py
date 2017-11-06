from flask import Flask, request
from managelogin import create_user
from managelogin import verify_login_create_session

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello App!!"


@app.route("/v1/users", methods = ['POST'])
def manage_users():
    if request.method == 'POST':
        data = request.json
        result = create_user(data["firstname"], data["lastname"], data["email"], data["password"])
        if result == 0:
            return "Email already exists. Log in or use a new email."
        if result == 1:
            return "Created user. Error creating session. Please login again."
        if result is None:
            return "Failed to add user. Please try again"
        else:
            return "Added user with session: " + str(result)

    # TODO: Create appropriate http response


@app.route("/v1/login", methods = ['POST'])
def login():
    if request.method == 'POST':
        data = request.json
        result = verify_login_create_session(data["email"], data["password"])
        if result is None:
            return "Invalid credentials. Please try again."
        if result == 0:
            return "User valid. Error creating session. Please try again."
        else:
            return "Session created: " + str(result)
        # TODO: Create appropriate http response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')