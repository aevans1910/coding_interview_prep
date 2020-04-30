#Excercism code

# Book Store

# To try and encourage more sales of different books from a popular 5 book
# series, a bookshop has decided to offer discounts on multiple book purchases.
# One copy of any of the five books costs $8.
# If, however, you buy two different books, you get a 5%
# discount on those two books.
# If you buy 3 different books, you get a 10% discount.
# If you buy 4 different books, you get a 20% discount.
# If you buy all 5, you get a 25% discount.

# Note: that if you buy four books, of which 3 are
# different titles, you get a 10% discount on the 3 that
# form part of a set, but the fourth book still costs $8.
# Your mission is to write a piece of code to calculate the
# price of any conceivable shopping basket (containing only
# books of the same series), giving as big a discount as
# possible.

def total(basket):
    total = 0
    total_distributed = 0
    book_types = {}
    bundles = []
    num_bundles = 0

    for book in basket:
        if book in book_types:
            book_types[book] += 1
        else:
            book_types[book] = 1
        
        if book_types[book] > num_bundles:
            num_bundles = book_types[book]

        
    for book_type in book_types:
        for index in range(book_types[book_type]):
            if index >= len(bundles):
                bundles.append([])
            bundles[index].append(book_type)


    bundles_distributed = [[] for _ in range(num_bundles)]
    last_index = 0

    for book_type in book_types:
        for index in range(book_types[book_type]):
            bundles_distributed[last_index].append(book_type)
            last_index = (last_index + 1) % num_bundles


    for bundle in bundles:
        if len(bundle) == 1:
            total += 800
        elif len(bundle) == 2:
            total += (1600 * 0.95)
        elif len(bundle) == 3:
            total += (2400 * 0.9)
        elif len(bundle) == 4:
            total += (3200 * 0.8)
        else:
            total += (4000 * 0.75)

    for bundle in bundles_distributed:
        if len(bundle) == 1:
            total_distributed += 800
        elif len(bundle) == 2:
            total_distributed += (1600 * 0.95)
        elif len(bundle) == 3:
            total_distributed += (2400 * 0.9)
        elif len(bundle) == 4:
            total_distributed += (3200 * 0.8)
        else:
            total_distributed += (4000 * 0.75)

    if total_distributed > total:
        return total
    return total_distributed

# Test case: basket=[1, 2, 2, 4, 5]
# Walkthrough:
# 1 -> booktypes=[] -> booktypes=[{1: 1}]
# 2 -> booktypes=[{1: 1}] -> booktypes=[{1: 1}, {2: 1}]
# 2 -> booktypes=[{1: 1}, {2: 1}] -> booktypes=[{1: 1}, {2: 2}]
# 4 -> booktypes=[{1: 1}, {2: 2}] -> booktypes=[{1: 1}, {2: 2}, {4: 1}]
# 5 -> booktypes=[{1: 1}, {2: 2}, {4: 1}] -> booktypes=[{1: 1}, {2: 2}, {4: 1}, {5: 1}]
# {1: 1} -> bundles[[1]]
# {2: 2} -> bundles[[1]] -> bundles[[1, 2], [2]]
# {4: 1} -> bundles[[1, 2], [2]] -> bundles[[1, 2, 4], [2]]
# {5: 1} ->  bundles[[1, 2, 4], [2]] ->  bundles[[1, 2, 4, 5], [2]]
# [1, 2, 4, 5] -> 25.6
# [2] -> 8
# 25.6 + 8 = 33.6
# {1: 1} -> bundles[[1]]
# {2: 2} -> bundles[[1]] -> bundles[[1, 2], [2]]
# {4: 1} -> bundles[[1, 2], [2]] -> bundles[[1, 2], [2, 4]]
# {5: 1} ->  bundles[[1, 2], [2, 4]] ->  bundles[[1, 2, 5], [2, 4]]
# [1, 2, 5] -> 21.6
# [2, 4] -> 15.2
# 21.6 + 15.2 = 36.8
# 33.6 < 36.8
# return 33.6