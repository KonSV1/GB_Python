def rle_code(data):
    cod = ''
    data = [i for i in data]
    data.append('')
    el = 0
    count = 1
    while el < len(data)-1:
        if data[el] == data[el+1]:
            count += 1
            el += 1
        else:
            cod += str(count)+data[el]
            count = 1
            el += 1
    return cod


def rle_decod(data):
    decod = ''
    data = [i for i in data]
    el = 0
    while el < len(data):
        i = 1
        while i <= int(data[el]):
            decod += data[el+1]
            i += 1
        el += 2
    return decod