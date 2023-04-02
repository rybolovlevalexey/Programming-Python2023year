def custom_filter(sp: list) -> bool:
    sp = filter(lambda x: type(1) == type(x) and x % 7 == 0, sp)
    return sum(sp) <= 83
