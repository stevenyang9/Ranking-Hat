from sqlalchemy import sql, orm
from app import db

class School(db.Model):
    __tablename__ = 'School'
    OPEID = db.Column('OPEID', db.Integer(), primary_key=True)
    CITY = db.Column('CITY', db.String(40))
    INSTNM = db.Column('INSTNM', db.String(100))
    INSTURL = db.Column('INSTURL', db.String(200))
    STABBR = db.Column('STABBR', db.String(2))

class AdmissionData(db.Model):
    __tablename__ = 'AdmissionData'
    OPEID = db.Column('OPEID', db.Integer(), primary_key=True)
    ADM_RATE = db.Column('ADM_RATE', db.Float())
    SAT_AVG = db.Column('SAT_AVG', db.Float())

class CollegeData(db.Model):
    __tablename__ = 'CollegeData'
    OPEID = db.Column('OPEID', db.Integer(), primary_key=True)
    PFTFAC = db.Column('PFTFAC', db.Float())
    LOCALE = db.Column('LOCALE', db.Integer())
    UGDS_WHITE = db.Column('UGDS_WHITE', db.Float())
    INEXPFTE = db.Column('INEXPFTE', db.Integer())
    GRAD_DEBT_MDN = db.Column('GRAD_DEBT_MDN', db.Float())

class GradData(db.Model):
    __tablename__ = 'GradData'
    OPEID = db.Column('OPEID', db.Integer(), primary_key=True)
    C150_4 = db.Column('C150_4', db.Float())


