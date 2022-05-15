from flask import render_template
from . import main

@main.errorhandler(404)
def four_Ow_four(error):
    '''
    Function ro render the 404 error page
    '''
    return render_template('fourOwforu.html'),404