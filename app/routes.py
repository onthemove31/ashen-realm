from flask import Blueprint, render_template,  request, redirect, url_for

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/projects')
def projects():
    return render_template('projects.html')

@main_bp.route('/blog')
def blog():
    return render_template('blog.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')

@main_bp.route('/send_message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Handle form submission, e.g., send an email or save to a database
    
    return redirect(url_for('main.contact'))
