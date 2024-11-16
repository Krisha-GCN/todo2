from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'ToDo'

# if __name__ == '__name__':
    