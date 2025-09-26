-- Stakeholder summary metrics for D09
SELECT
  COUNT(*) AS total_records,
  AVG(CAST(forecast_accurate AS FLOAT)) AS forecast_accurate_rate
FROM sales_forecast;

SELECT *
FROM sales_forecast
ORDER BY 1
LIMIT 10;
