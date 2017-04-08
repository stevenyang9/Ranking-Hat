from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import models
from sqlalchemy import desc 

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})


@app.route('/')
def all_schools_index():
    schools = db.session.query(models.school).all()
    return render_template('all-schools-index.html', schools=schools)

@app.route('/all-schools')
def rankbyadmission_schools():
    schools = db.session.query(models.school)\
        .join(models.admissiondata, models.admissiondata.opeid == models.school.opeid)\
        .join(models.graddata, models.graddata.opeid == models.school.opeid)\
        .add_column(models.school.instnm)\
        .add_column(models.admissiondata.sat_avg)\
        .add_column(models.admissiondata.adm_rate)\
        .add_column(models.graddata.c150_4)\
        .order_by(models.admissiondata.sat_avg).limit(25).all()
    return render_template('all-schools-bysat.html', schools=schools)


@app.route('/all-schools-admissionrate')
def admissionrate():
    s="schools = db.session.query(models.school).join(models.admissiondata, models.school.opeid == models.admissiondata.opeid).add_column(models.school.instnm).add_column(models.admissiondata.adm_rate).order_by(models.admissiondata.adm_rate).limit(25).all()"
    exec(s)
    return render_template('all-schools-admissionrate.html', outputs=schools)


@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
    return singular if number in (0, 1) else plural

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

