from flask import Blueprint, render_template


site = Blueprint('site',__name__,template_folder='site_templates')



@site.route('/')
def home():
    print("ooga booga in the terminal")
    return render_template('index.html')