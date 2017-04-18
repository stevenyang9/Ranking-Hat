from string_res import *
from flask_sqlalchemy import SQLAlchemy
import models

def getresults(weightdict):
	querystr = calculate(weightdict)
	exec(querystr)
	return schools


def calculate(weightdict):
	querystr = ""
	orderstr = ""
	for attr in weightdict.keys():
		orderstr += attr + rankstr + "*" + str(weightdict[attr]) + "+"
	orderstr = orderstr[:-1]
	querystr = joinstr + orderbystr + orderstr + ")"
	return querystr
