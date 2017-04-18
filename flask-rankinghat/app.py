from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask import redirect
import models
import sql
from string_res import *
from sql import *
from config import POSTS_PER_PAGE

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

wdict = dict()

@app.route('/')
def all_schools_index():
    schools = db.session.query(models.school).all()
    return render_template('all-schools-index.html', schools=schools)

@app.route('/inputweights')
def inputweights():
    return render_template('inputweights.html')

@app.route('/getuserinput', methods= ['GET','POST'])
def getuserinput():
	wdict[attrs[0]] = int(request.form['acceptancerate']) if request.form['acceptancerate'] else 0
	wdict[attrs[1]] = int(request.form['sataverage']) if request.form['sataverage'] else 0
	wdict[attrs[2]] = int(request.form['fulltimefaculty']) if request.form['fulltimefaculty'] else 0
	wdict[attrs[3]] = int(request.form['studentbodydiversity']) if request.form['studentbodydiversity'] else 0
	wdict[attrs[4]] = int(request.form['instructionalexpenditure']) if request.form['instructionalexpenditure'] else 0
	wdict[attrs[5]] = int(request.form['studentdebt']) if request.form['studentdebt'] else 0
	wdict[attrs[6]] = int(request.form['graduationrate']) if request.form['graduationrate'] else 0
	# wdict[attrs[7]] = int(request.form['locale'])
	return results(1)


@app.route('/results', methods=['GET','POST'])
@app.route('/results/<int:page>', methods=['GET','POST'])
def results(page=1):
	schools = getresults(wdict)
	outputs = schools.paginate(page, POSTS_PER_PAGE, False)
	return render_template('results.html', outputs=outputs, pagenum = page)

@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
	return singular if number in (0, 1) else plural

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

