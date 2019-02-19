from collections import defaultdict

def list_sort():
    listtobesorted = ([2, 0, 6, 5, 1, 7, 'z', 'a'])
    d = defaultdict(list)
    for item in listtobesorted:
        if isinstance(item, int):
            if (item % 2 == 0):
                d['evens'].append(item)
            elif (item % 2 > 0):
                d['odds'].append(item)
        else:
            d['chars'].append(item)
    print(d)
list_sort()
