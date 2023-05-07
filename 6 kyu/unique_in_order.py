def unique_in_order(s):
    letters = list(map(lambda i: s[i] if i + 1 == len(s) or s[i + 1] != s[i] else None, range(len(s))))
    return list(filter(lambda x: x is not None, letters))


# print(
#     unique_in_order('AAAABBBCCDAABBB'),
#     unique_in_order('ABBCcAD'),
#     unique_in_order([1, 2, 2, 3, 3]),
#     unique_in_order((1, 2, 2, 3, 3)), sep='\n'
# )
