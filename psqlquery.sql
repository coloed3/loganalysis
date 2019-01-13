

CREATE VIEW findlog AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as totallogcount
FROM log
GROUP BY Date;


CREATE VIEW elogs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as errcount
FROM log
WHERE STATUS = '404 NOT FOUND'
GROUP BY Date;




SELECT elogs.date, round(100.0*errcount/totallogcount,2) as percent
            FROM findlog, elogs
            WHERE findlog.date = elogs.date
            AND errcount > totallogcount/100;
