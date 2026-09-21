SELECT
  circle,
  COUNT(*) AS outage_count,
  AVG(EXTRACT(EPOCH FROM (end_time - start_time))/3600.0) AS mttr_hours
FROM outages
GROUP BY circle
ORDER BY outage_count DESC;

SELECT site_id, COUNT(*) AS outage_count
FROM outages
GROUP BY site_id
ORDER BY outage_count DESC
LIMIT 20;
