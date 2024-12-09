from typing import List


def stock_list(stocklist: List[str], categories: List[str]) -> str:
    if not stocklist or not categories:
        return ""

    book_category_agg = {category: 0 for category in categories}

    for book in stocklist:
        category_quantity = book.split()
        category = category_quantity[0][0]
        
        if category in book_category_agg:
            quantity = int(category_quantity[1])
            book_category_agg[category] += quantity

    return " - ".join(
        [
            f"({category} : {quantity})"
            for category, quantity in book_category_agg.items()
        ]
    )