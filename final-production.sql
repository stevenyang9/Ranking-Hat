CREATE TABLE school
(opeid INT PRIMARY KEY,
city VARCHAR(40) NOT NULL,
instnm VARCHAR(100) NOT NULL,
insturl VARCHAR(200) NOT NULL,
stabbr VARCHAR(2) NOT NULL
);

CREATE TABLE admissiondata
(opeid INT PRIMARY KEY,
adm_rate FLOAT NOT NULL,
adm_rate_rank INT NOT NULL,
sat_avg INT NOT NULL,
sat_avg_rank INT NOT NULL
);

CREATE TABLE collegedata
(opeid INT PRIMARY KEY,
pftfac FLOAT NOT NULL,
pftfac_rank INT NOT NULL,
locale INT NOT NULL,
ugds_white FLOAT NOT NULL,
ugds_white_rank INT NOT NULL,
inexpfte INT NOT NULL,
inexpfte_rank INT NOT NULL,
grad_debt_mdn FLOAT NOT NULL,
grad_debt_mdn_rank INT NOT NULL
);

CREATE TABLE graddata
(opeid INT PRIMARY KEY NOT NULL,
c150_4 FLOAT NOT NULL,
c150_4_rank INT NOT NULL
);

\COPY school(opeid, city, instnm, insturl, stabbr) FROM '~/CS316Project/SampleData/school.csv' DELIMITER ',' CSV HEADER
\COPY admissiondata(opeid, adm_rate, sat_avg,adm_rate_rank, sat_avg_rank) FROM '~/CS316Project/SampleData/admissiondata.csv' DELIMITER ',' CSV HEADER
\COPY collegedata(opeid, pftfac, locale, ugds_white, inexpfte, grad_debt_mdn, pftfac_rank,ugds_white_rank,inexpfte_rank,grad_debt_mdn_rank) FROM '~/CS316Project/SampleData/collegedata.csv' DELIMITER ',' CSV HEADER
\COPY graddata(opeid, c150_4, c150_4_rank) FROM '~/CS316Project/SampleData/graddata.csv' DELIMITER ',' CSV HEADER

-- Output all data
SELECT *
FROM school NATURAL JOIN admissiondata NATURAL JOIN collegedata NATURAL JOIN graddata;
