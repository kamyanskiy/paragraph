from itertools import zip_longest


def paragraph(given):
    """
    
    :param given: string like "1.2.3" 
    :return: list of combinations ['1 2 3', '1 2.3', '1.2 3', '1.2.3']
    """
    splitted = given.replace(".", "_").split("_")
    num_combinations = len(splitted) - 1

    combinations = []
    for j in range(num_combinations):
        for k in range(num_combinations):
            combinations.append(("." if j else " ", "." if k else " "))

    all_zipped = []
    for item in combinations:
        all_zipped.append(list(zip_longest(splitted, item, fillvalue='')))

    all_result = []
    for lst in all_zipped:
        all_result.append("".join(["".join(i) for i in lst]))

    for res in all_result:
        print(res)
    return all_result
