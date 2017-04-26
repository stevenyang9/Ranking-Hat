from sqlalchemy import sql, orm
from app import db

class college(db.Model):
    __tablename__ = 'college'
    opeid = db.Column('opeid', db.Integer(), primary_key=True)
    instnm = db.Column('instnm', db.String(100))
    city = db.Column('city', db.String(40))
    stabbr = db.Column('stabbr', db.String(2))
    insturl = db.Column('insturl', db.String(200))
    adm_rate = db.Column('adm_rate', db.Float())
    sat_avg = db.Column('sat_avg', db.Float())
    grad_debt_mdn = db.Column('grad_debt_mdn', db.Float())
    inexpfte = db.Column('inexpfte', db.Integer())
    pftfac = db.Column('pftfac', db.Float())
    locale = db.Column('locale', db.Integer())
    ugds_white = db.Column('ugds_white', db.Float())
    c150_4 = db.Column('c150_4', db.Float())
    adm_rate_rank = db.Column('adm_rate_rank', db.Integer())
    sat_avg_rank = db.Column('sat_avg_rank', db.Integer())
    c150_4_rank = db.Column('c150_4_rank', db.Integer())
    pftfac_rank = db.Column('pftfac_rank', db.Integer())
    ugds_white_rank = db.Column('ugds_white_rank', db.Integer())
    inexpfte_rank = db.Column('inexpfte_rank', db.Integer())
    grad_debt_mdn_rank = db.Column('grad_debt_mdn_rank', db.Integer())
