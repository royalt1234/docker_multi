from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

todo = ["Sample task"]

HTML = '''
<!doctype html>
<title>Todo</title>
<h1>Todo list</h1>
<ul>{% for item in todo %}<li>{{ item }}</li>{% endfor %}</ul>
<form method="post"><input name="task" placeholder="New task"><button>Add</button></form>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and request.form.get('task'):
        todo.append(request.form['task'])
        return redirect(url_for('home'))
    return render_template_string(HTML, todo=todo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
