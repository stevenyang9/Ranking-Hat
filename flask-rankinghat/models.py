from sqlalchemy import sql, orm
from app import db

class school(db.Model):
    __tablename__ = 'school'
    opeid = db.Column('opeid', db.Integer(), primary_key=True)
    city = db.Column('city', db.String(40))
    instnm = db.Column('instnm', db.String(100))
    insturl = db.Column('insturl', db.String(200))
    stabbr = db.Column('stabbr', db.String(2))

class admissiondata(db.Model):
    __tablename__ = 'admissiondata'
    opeid = db.Column('opeid', db.Integer(), primary_key=True)
    adm_rate = db.Column('adm_rate', db.Float())
    adm_rate_rank = db.Column('adm_rate_rank', db.Integer())
    sat_avg = db.Column('sat_avg', db.Float())
    sat_avg_rank = db.Column('sat_avg_rank', db.Integer())

class collegedata(db.Model):
    __tablename__ = 'collegedata'
    opeid = db.Column('opeid', db.Integer(), primary_key=True)
    pftfac = db.Column('pftfac', db.Float())
    pftfac_rank = db.Column('pftfac_rank', db.Integer())
    locale = db.Column('locale', db.Integer())
    ugds_white = db.Column('ugds_white', db.Float())
    ugds_white_rank = db.Column('ugds_white_rank', db.Integer())
    inexpfte = db.Column('inexpfte', db.Integer())
    inexpfte_rank = db.Column('inexpfte_rank', db.Integer())
    grad_debt_mdn = db.Column('grad_debt_mdn', db.Float())
    grad_debt_mdn_rank = db.Column('grad_debt_mdn_rank', db.Integer())

class graddata(db.Model):
    __tablename__ = 'graddata'
    opeid = db.Column('opeid', db.Integer(), primary_key=True)
    c150_4 = db.Column('c150_4', db.Float())
    c150_4_rank = db.Column('c150_4_rank', db.Integer())
