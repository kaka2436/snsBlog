from datetime import datetime
from flask import render_template,session,redirect,url_for

from . import main
# from .forms import NameForm
from .. import db
from ..models import User

@main.route('/',methods=['POST','GET'])
def index():
    # return render_template('index.html',form = form , name = session.get('name'),
    #                         known = session.get('known',False),
    #                         current_time = datetime.utcnow())
    return render_template('index.html')
