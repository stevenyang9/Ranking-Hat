from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask import redirect
import models
from string_res import *
from config import POSTS_PER_PAGE
from timeit import Timer
import timeit
 
app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

wdict = dict()

@app.route('/')
def all_schools_index():
    return render_template('all-schools-index.html')

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
	return results(1)


@app.route('/results', methods=['GET','POST'])
@app.route('/results/<int:page>', methods=['GET','POST'])
def results(page=1):
	#time query
	# t = Timer("getresults(wdict)", setup="from app import wdict, getresults")
	# print "-------###PROFILING RESULT###-------"
	# print t.timeit(10000);
	# t = timeit.Timer('getresults(wdict)', "from __main__ import getresults,wdict")
	# print "-------###PROFILING RESULT###-------"
	# print t.timeit(1000);
	schools = getresults(wdict)
	outputs = schools.paginate(page, POSTS_PER_PAGE, False)
	#remove 0s
	inputdict = {inputnames[k]:v for k, v in wdict.items() if v}
	return render_template('results.html', outputs=outputs, pagenum = page, localedict = localedict, inputdict = inputdict)

@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
	return singular if number in (0, 1) else plural

def getresults(wdict):
	schools = models.college.query.order_by(wdict[attrs[0]]*models.college.adm_rate_rank\
												+wdict[attrs[1]]*models.college.sat_avg_rank\
												+wdict[attrs[2]]*models.college.pftfac_rank\
												+wdict[attrs[3]]*models.college.ugds_white_rank\
												+wdict[attrs[4]]*models.college.inexpfte_rank\
												+wdict[attrs[5]]*models.college.grad_debt_mdn_rank\
												+wdict[attrs[6]]*models.college.c150_4_rank);
	return schools	


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

