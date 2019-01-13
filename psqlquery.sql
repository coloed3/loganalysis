-- having issues with returning data
--
-- CREATE VIEW findlog AS
-- SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as totallogcount
-- FROM log
-- GROUP BY Date;
--
--
-- CREATE VIEW elogs AS
-- SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as errcount
-- FROM log
-- WHERE STATUS = '404 NOT FOUND'
-- GROUP BY Date;
--
--
--
--
-- SELECT elogs.date, round(100.0*errcount/totallogcount,2) as percent
--             FROM findlog, elogs
--             WHERE findlog.date = elogs.date
--             AND errcount > totallogcount/100;


-- modifing query_gt1p due to errors
--  errors with query below  had to tweak for it to run
-- WITH total_request as(
--   Select time::DATE as day, count(*)
--   from log
--   GROUP BY time::DATE
--   ORDER BY time::DATE
-- ),  total_errors AS(
--   select time ::DATE as day, count(*)
--   from log
--   where status != '200 ok'
--   group by time :: Date
--   order by time :: Date
-- ), total_error_rate as (
--   SELECT total_request.day,
--   total_errors.count ::float / total_request.count ::float *100
--   AS  error_percent
--   from total_request, total_errors
--   Where total_request.day = total_errors.day
-- )
-- Select * from total_error_rate where error_percent > 1;




WITH total_request AS (
          SELECT time::date AS day, count(*)
          FROM log
          GROUP BY time::date
          ORDER BY time::date
        ), total_errors AS (
          SELECT time::date AS day, count(*)
          FROM log
          WHERE status != '200 OK'
          GROUP BY time::date
          ORDER BY time::date
        ), total_failures AS (
          SELECT total_request.day,
            total_errors.count::float / total_request.count::float * 100
            AS total_error_count
          FROM total_request, total_errors
          WHERE total_request.day = total_errors.day
        )
      SELECT * FROM total_failures WHERE total_error_count > 1;
