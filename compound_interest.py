def fixed_compound(years):
    p = 10000
    r = .08
    n = 12
    t = years
    amount = p*(1 + (r / n)) ** (n * t)
    return amount

print(fixed_compound(10))
