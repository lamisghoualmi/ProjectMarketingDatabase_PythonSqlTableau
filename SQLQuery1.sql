/* Table information, type, precision*/
sp_help CleanMarketing_data

/* delete column and update the table*/
ALTER TABLE CleanMarketing_data DROP COLUMN column1; 

select * from CleanMarketing_data

select INCOME from CleanMarketing_data where MARITAL_Status='Married' order by INCOME DESC

select MARITAL_Status, INCOME from CleanMarketing_data order by INCOME DESC 

select NUMWEBPURCHASES, MARITAL_STATUS, EDUCATION,YEAR_BIRTH from CleanMarketing_data where EDUCATION=Phd order by NUMWEBPURCHASES desc 

/* Webpurchases grouped by Education*/
select SUM(NUMWEBPURCHASES), EDUCATION from CleanMarketing_data group by EDUCATION  order by SUM(NUMWEBPURCHASES) DESC

/* Webpurchases grouped by MARITAL_STATUS*/
select SUM(NUMWEBPURCHASES), MARITAL_STATUS from CleanMarketing_data group by MARITAL_STATUS order by SUM(NUMWEBPURCHASES) DESC

/* Webpurchases by country*/
select SUM(NUMWEBPURCHASES), COUNTRY from CleanMarketing_data group by COUNTRY  order by SUM(NUMWEBPURCHASES) DESC

/* Webpurchases by country*/
select SUM(NUMWEBPURCHASES),COMPLAIN from CleanMarketing_data group by COMPLAIN  order by SUM(NUMWEBPURCHASES) DESC

/* Webpurchases by country*/
select SUM(NUMWEBPURCHASES),COMPLAIN from CleanMarketing_data group by COMPLAIN  order by SUM(NUMWEBPURCHASES) DESC

/* TOtal purchase by Marketing compain
ACCEPTEDCMP1 3046
ACCEPTEDCMP2 598
ACCEPTEDCMP3 2507
ACCEPTEDCMP4 3337
ACCEPTEDCMP5 3373  The 5th marketing compain is the most successful*/
select SUM(TOTALPURSHASE),ACCEPTEDCMP5 from CleanMarketing_data group by ACCEPTEDCMP5 order by SUM(TOTALPURSHASE) DESC