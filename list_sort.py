from collections import defaultdict

def list_sort():
               
    listtobesorted = ([2, 0, 6, 5, 1, 7, 'z', 'a'])
    expected_types = {int, str}
    evens = []
    odds = []
    chars = []
    d = dict()
    try:
        if all(any(isinstance(item, t) for t in expected_types) for item in listtobesorted):
            for item in listtobesorted:
                if isinstance(item, int):
                    if (item % 2 == 0):
                        evens.append(item)
                    elif (item % 2 > 0):
                        odds.append(item)
                else:
                    chars.append(item)
            d['evens'] = sorted(evens)
            d['odds'] = sorted(odds)
            d['chars'] = sorted(chars)
            print(d)
        else: 
            raise ValueError
    except ValueError:
        print("invalid input") 
list_sort()