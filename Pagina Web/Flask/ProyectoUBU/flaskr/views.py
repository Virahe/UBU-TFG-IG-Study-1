from flask import Blueprint, render_template,request

main = Blueprint('main', __name__)

@main.route('/')
def index():

    return render_template('index.html')


@main.route('/sign')
def sign():
    return render_template('sign.html')

@main.route('/sign', methods=['POST'])
def sign_post():
    name = request.form.get('name')
    comment = request.form.get('comment')

    return 'Name:{name} Comment:{comment}'