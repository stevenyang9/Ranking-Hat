attrs=["models.admissiondata.adm_rate","models.admissiondata.sat_avg",
			"models.collegedata.pftfac", "models.collegedata.ugds_white","models.collegedata.inexpfte","models.collegedata.grad_debt_mdn",
			"models.graddata.c150_4","models.collegedata.locale"]

ranks=["models.admissiondata.adm_rate_rank","models.admissiondata.sat_avg_rank",
			"models.collegedata.pftfac_rank", "models.collegedata.ugds_white_rank","models.collegedata.inexpfte_rank","models.collegedata.grad_debt_mdn_rank",
			"models.graddata.c150_4_rank","models.collegedata.locale_rank"]

inputnames = {"models.admissiondata.adm_rate":"acceptance rate","models.admissiondata.sat_avg":"sat average",
			"models.collegedata.pftfac":"full-time faculty", "models.collegedata.ugds_white":"student body diversity"
,"models.collegedata.inexpfte":"instructional expenditure","models.collegedata.grad_debt_mdn":"student debt",
			"models.graddata.c150_4":"graduation rate","models.collegedata.locale":"locale"}

localedict = {11:'city(large)', 12:'city(midsize)', 13:'city(small)', 
				21:'suburb(large)', 22:'suburb(midsize)', 23:'suburb(small)',
				31:'town(fringe)', 32:'town(distant)',33:'town(remote)',
				41:'rural(fringe)',42:'rural(distant)',43:'rural(remote)' }