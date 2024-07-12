from flask import redirect,url_for,jsonify,request,flash,render_template
from flask_login import current_user, login_required
from . import main
from webapp.models import Entry
from webapp.extensions import db
import ast


################################################################ HOME
@main.route('/')
@main.route('/index')
def index():
    if current_user.is_authenticated:
        entry = Entry.query.filter_by(user_id=current_user.id).all()
        return render_template('index.html',title='Welcome',entry=entry)
    else:
        return redirect(url_for('auth.login'))

@main.route('/account')
@login_required
def account():
    return render_template('account.html',title='Budget Tracker')

################################################################# ENTRY

@main.route('/add_entry',methods=['GET', 'POST'])
def add_entry():	
    if request.method=='POST':
        if current_user.is_authenticated:
            entry = Entry(category=request.form['category'],user_id=current_user.id,entry_date=request.form['entry_date'],spent=request.form['spent'])
            db.session.add(entry)
            db.session.commit()
            flash('Entry added - {}'.format(request.form['category']))        	
    return redirect(url_for('main.index'))

@main.route('/delete_entry',methods=['GET','POST'])
def delete_entry():
    delete_id = request.form['id']
    entryToDelete = Entry.query.filter_by(id=delete_id).first()
    db.session.delete(entryToDelete)
    db.session.commit()
    flash('Entry deleted')
    return redirect(url_for('main.index'))

@main.route('/update_entry',methods=['GET','POST'])
def update_entry():
    update_id = request.form['id']
    category = request.form['category']
    spent=request.form['spent']
    print(category)
    entryToUpdate = Entry.query.filter_by(id=update_id).first()
    entryToUpdate.category = category
    entryToUpdate.spent = spent
    db.session.add(entryToUpdate)
    db.session.commit()
    flash('Entry changed')
    return redirect(url_for('main.index'))
