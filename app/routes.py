from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'World'}
    posts = [
        {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

# render_template()" é uma função built-in do Flask que invoca o Jinja2