from flask import Flask, render_template, request, redirect
from tinydb import TinyDB, Query

db = TinyDB('./db.json')
todos = Query()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    todo = request.form.get('todo')
    if request.method == 'POST':
        db.insert({'todo': todo})
    todos = db.all()
    return render_template('index.html', todos=todos)

@app.route('/delete/<int:id>')
def delete(id):
    db.remove(doc_ids=[id])
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')