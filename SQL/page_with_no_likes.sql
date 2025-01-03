-- Assume you're given two tables containing data about Facebook Pages and their respective likes (as in "Like a Facebook Page").
-- Write a query to return the IDs of the Facebook pages that have zero likes. The output should be sorted in ascending order based on the page IDs.


-- pages Table:
-- page_id	    integer
-- page_name	varchar


-- page_likes Table:
-- user_id	    integer
-- page_id	    integer
-- liked_date	datetime


SELECT
    p1.page_id AS page_id
FROM
    pages AS p1
LEFT JOIN
    page_likes AS p2
GROUP BY
    p1.page_id
HAVING
    COUNT(p2.page_id) = 0
ORDER BY
    page_id;