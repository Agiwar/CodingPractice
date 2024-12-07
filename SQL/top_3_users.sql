-- You have information on user’s daily downloads in the download_facts table
WITH rank_downloads AS (
    SELECT
        DENSE_RANK() OVER(PARTITION BY date ORDER BY downloads DESC) AS daily_rank,
        user_id,
        date,
        downloads
    FROM
        download_facts
)
SELECT
    daily_rank,
    user_id,
    date,
    downloads
FROM
    rank_downloads
WHERE
    daily_rank <= 3
ORDER BY
    date,
    daily_rank