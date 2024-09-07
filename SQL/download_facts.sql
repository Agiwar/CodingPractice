SELECT
    d.download_date AS download_date,
    a.paying_customer AS paying_customer,
    ROUND(AVG(d.downloads), 2) AS average_downloads
FROM
    downloads AS d
INNER JOIN
    accounts AS a
    ON d.account_id = a.account_id
GROUP BY
    d.download_date,
    a.paying_customer