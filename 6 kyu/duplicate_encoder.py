def duplicate_encode(word: str):
    return ''.join(list(map(lambda x: '(' if word.lower().count(x.lower()) == 1 else ')', word)))


# print(duplicate_encode('))(()())())'))
# print(duplicate_encode('IXQAT(fWSO)dTvvmH(gQMKFzLJgOMp! fmOh'))
# print(duplicate_encode('Success'))
# print(duplicate_encode('(( @'))
