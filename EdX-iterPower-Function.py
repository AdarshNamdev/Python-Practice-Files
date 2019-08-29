def iterPower(base, exp):  # base**exp
    result = 1
    while exp > 0:
        result = result * base
        exp -= 1

    return result

func_base = float(input("Base >> "))
func_exp = int(input("power >> "))
print(iterPower(func_base,func_exp))