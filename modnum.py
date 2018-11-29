def mod_num(x):
    return x + 5, x - 3, x + 2
    nums = [9, 45, 23]
    result = list(map(mod_num,nums))
    print(result)
    