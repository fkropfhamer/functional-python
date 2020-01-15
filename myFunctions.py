def myMap(list, fn):
    return [fn(x) for x in list]

def myFilter(list, fn):
    return [x for x in list if not fn(x)]

def myReduce(list, init, fn):
    if not list:
        return init
    return myReduce(list[1:], fn(init, list[0]), fn)

def mySum(list):
    return myReduce(list, 0, lambda x, y : x + y)

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6]
    fn = lambda x : x * 2
    print(myMap(list, fn))

    fn2 = lambda x : x == 3
    print(myFilter(list, fn2))

    fn3 = lambda x, y : x + y
    print(myReduce([1, 2], 4, fn3))
