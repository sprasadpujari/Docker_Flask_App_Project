from flask import Flask, render_template, request, redirect
from urllib.parse import quote, unquote

app = Flask(__name__)

# Sample to-do list
todo_list = ["Buy groceries", "Finish homework", "Read a book"]

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list, quote=quote, unquote=unquote)

@app.route('/add', methods=['POST'])
def add():
    new_task = request.form.get('new_task')
    if new_task:
        todo_list.append(new_task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

