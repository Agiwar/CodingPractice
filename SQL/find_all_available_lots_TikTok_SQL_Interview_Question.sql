-- There are 2 tables: 'lots' and 'bids'.
-- Write a query that returns a list of all available lots with the number of bids,
-- the current lot price, and the current lot winner.


-- lots table:
-- lot_id      int      PK
-- lot_name    text
-- created_at  datetime


-- bids table:
-- bid_id      int      PK
-- lot_id      int
-- bid_price   decimal
-- bidder_id   int
-- created_at  datetime


-- current price is determined by latest created_at
WITH each_lot_price_created_at AS (
    SELECT
        bid_id,
        lot_id,
        bid_price,
        DENSE_RANK() OVER(PARTITION BY lot_id ORDER BY created_at DESC) AS rk_lot_datetime
    FROM
        auction_db.bids
),

-- current bid winner is determined by the one whose bid is highest with earliest created_at
each_lot_bided AS (
    SELECT
        bid_id,
        lot_id,
        bidder_id,
        DENSE_RANK() OVER(PARTITION BY lot_id ORDER BY bid_price DESC, created_at ASC) AS rk_lot_bided
    FROM
        auction_db.bids
),

-- all available lots: show all lots' info, a lot existing there doesn't mean it has been bidded
available_lots AS (
    SELECT
        t1.lot_id AS lot_id,
        t1.lot_name AS lot_name,
        COUNT(t2.bid_id) AS num_of_bids
    FROM
        auction_db.lots AS t1
    LEFT JOIN
        auction_db.bids AS t2
        ON t1.lot_id = t2.lot_id
    GROUP BY
        t1.lot_id,
        t1.lot_name
)

-- for those lots not bidded, set NULL price as 0, and set NULL bidder_id as 'not bidded'
SELECT
    t1.lot_id AS lot_id,
    t1.lot_name AS lot_name,
    t1.num_of_bids AS num_of_bids,
    COALESCE(t2.bid_price, 0) AS current_price,
    COALESCE(t3.bidder_id, 'not bidded') AS current_winner
FROM
    available_lots AS t1
LEFT JOIN
    each_lot_price_created_at AS t2
    ON t1.lot_id = t2.lot_id
    AND t2.rk_lot_datetime = 1
LEFT JOIN
    each_lot_bided AS t3
    ON t1.lot_id = t3.lot_id
    AND t3.rk_lot_bided = 1