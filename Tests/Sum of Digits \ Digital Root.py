def digital_root(n):
    while len(str(n)) != 1:
        list_n = [i for i in str(n)]
        n = sum(list(map(lambda x: int(x), list_n)))
    return n
