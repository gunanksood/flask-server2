from flask import Flask
from flask import send_from_directory

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/post')
def method_get():
    send_from_directory('/template', as_attachment = True)


if __name__ == '__main__':
    app.run()
