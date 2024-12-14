from typing import Dict, List


def fund_return(purchases: Dict[str, List], prices: Dict[str, List]) -> float:
    purchases_zip = dict(zip(purchases["date"], purchases["purchase"]))
    prices_zip = dict(zip(prices["date"], prices["price"]))

    spends = []
    shares = []

    for date_fund in prices_zip:
        if date_fund in purchases_zip:
            transaction = purchases_zip[date_fund] // prices_zip[date_fund]
            transaction_mod = purchases_zip[date_fund] % prices_zip[date_fund]

        spends.append(purchases_zip[date_fund] - transaction_mod)
        shares.append(transaction)

    return sum(shares) * prices["price"][-1] - sum(spends)