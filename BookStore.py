#Excercism code

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



