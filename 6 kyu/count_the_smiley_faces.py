def count_smileys(arr):
    els = [':', ';', '-', '~', ')', 'D']
    count = 0
    for el in arr:
        if len(list(filter(lambda y: y in els, el))) == len(el) and \
                (':' in el or ';' in el) and (')' in el or 'D' in el):
            count += 1
    return count


arr = [';]', ':[', ';*', ':$', ';-D']
print(count_smileys(arr))
