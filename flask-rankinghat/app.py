from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import models
import forms
from sqlalchemy import desc 

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

#@app.route('/')
#def all_schools():
#    schools = db.session.query(models.school).all()
#    return render_template('all-schools.html', schools=schools)

# @app.route('/')
# def all_schools():
#     schools = db.session.query(models.school).all()
#     return render_template('all-schools-test.html', schools=schools)



@app.route('/')
def all_schools_index():
    schools = db.session.query(models.school).all()
    return render_template('all-schools-index.html', schools=schools)


#@app.route('/all-schools')
#def ranked_schools():
#    schools = db.session.query(models.school).all()
#    return render_template('all-schools.html', schools=schools)    


@app.route('/all-schools')
def rankbyadmission_schools():
    schools = db.session.query(models.school)\
        .join(models.admissiondata, models.admissiondata.opeid == models.school.opeid)\
        .add_column(models.school.instnm)\
        .add_column(models.admissiondata.sat_avg)\
        .order_by(models.admissiondata.sat_avg.desc()).all()
    return render_template('all-schools-bysat.html', schools=schools)


@app.route('/all-schools-admissionrate')
def admissionrate():
    schools = db.session.query(models.school)\
        .join(models.admissiondata, models.school.opeid == models.admissiondata.opeid)\
        .add_column(models.school.instnm)\
        .add_column(models.admissiondata.adm_rate)\
        .order_by(models.admissiondata.adm_rate).all()
    return render_template('all-schools-admissionrate.html', outputs=schools)







@app.route('/drinker/<name>')
def drinker(name):
    drinker = db.session.query(models.Drinker)\
        .filter(models.Drinker.name == name).one()
    return render_template('drinker.html', drinker=drinker)

@app.route('/edit-drinker/<name>', methods=['GET', 'POST'])
def edit_drinker(name):
    drinker = db.session.query(models.Drinker)\
        .filter(models.Drinker.name == name).one()
    beers = db.session.query(models.Beer).all()
    bars = db.session.query(models.Bar).all()
    form = forms.DrinkerEditFormFactory.form(drinker, beers, bars)
    if form.validate_on_submit():
        try:
            form.errors.pop('database', None)
            models.Drinker.edit(name, form.name.data, form.address.data,
                                form.get_beers_liked(), form.get_bars_frequented())
            return redirect(url_for('drinker', name=form.name.data))
        except BaseException as e:
            form.errors['database'] = str(e)
            return render_template('edit-drinker.html', drinker=drinker, form=form)
    else:
        return render_template('edit-drinker.html', drinker=drinker, form=form)

@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
    return singular if number in (0, 1) else plural

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
