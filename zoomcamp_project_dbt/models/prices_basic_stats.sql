SELECT keyword, AVG(price) AS average_price, date
FROM `zoomcamp-project-382011.zoomcamp_project_382011.prices_raw`
GROUP BY keyword, date