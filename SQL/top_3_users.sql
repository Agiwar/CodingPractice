WITH user_daily_downloads AS (
    SELECT
        user_id,
        `date`,
        SUM(downloads) AS downloads
    FROM
        download_facts
    GROUP BY
        user_id,
        `date`
),

rank_user_daily_downloads AS (
    SELECT
        user_id,
        `date`,
        downloads,
        RANK() OVER(PARTITION BY `date` ORDER BY downloads DESC) AS daily_rank
    FROM
        user_daily_downloads
)

SELECT
    daily_rank,
    user_id,
    `date`,
    downloads
FROM
    rank_user_daily_downloads
WHERE
    daily_rank <= 3
ORDER BY
    `date`,
    daily_rank