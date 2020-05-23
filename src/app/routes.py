from flask import render_template

from app import App


@App.route('/')
@App.route('/index')
def index():
    user = {'username': 'Joe'}
    posts = [
        {
            'author': {'username': 'Quentin'},
            'body': 'Beautiful day in Zoom University!'
        },
        {
            'author': {'username': 'Nina'},
            'body': 'The Code Geass Movie was 5/7'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
