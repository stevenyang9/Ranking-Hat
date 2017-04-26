CREATE TABLE college
(opeid INT PRIMARY KEY,
instnm VARCHAR(100) NOT NULL,
city VARCHAR(40) NOT NULL,
stabbr VARCHAR(2) NOT NULL,
insturl VARCHAR(200) NOT NULL,
adm_rate FLOAT NOT NULL,
sat_avg INT NOT NULL,
grad_debt_mdn FLOAT NOT NULL,
inexpfte INT NOT NULL,
pftfac FLOAT NOT NULL,
locale INT NOT NULL,
ugds_white FLOAT NOT NULL,
c150_4 FLOAT NOT NULL,
adm_rate_rank INT NOT NULL,
sat_avg_rank INT NOT NULL,
c150_4_rank INT NOT NULL,
pftfac_rank INT NOT NULL,
ugds_white_rank INT NOT NULL,
inexpfte_rank INT NOT NULL,
grad_debt_mdn_rank INT NOT NULL
);

\COPY college(opeid, instnm, city, stabbr, insturl, adm_rate, sat_avg, grad_debt_mdn, inexpfte, pftfac, locale, ugds_white, c150_4, adm_rate_rank, sat_avg_rank, c150_4_rank, pftfac_rank, ugds_white_rank, inexpfte_rank, grad_debt_mdn_rank) FROM '~/college.csv' DELIMITER ',' CSV HEADER


-- Output all data
SELECT * FROM college;
