SELECT keyword, AVG(price), date
FROM `zoomcamp-project-382011.zoomcamp_project_382011.prices_raw`
GROUP BY keyword, date