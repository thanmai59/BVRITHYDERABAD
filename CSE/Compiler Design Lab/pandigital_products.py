sum = 0
products = []
for i in range(2, 10000):
    for j in range(i, 10 ** (5 - len(str(i)))):
        string = str(i) + str(j) + str(i * j)
        if len(string) == 9:
            zeroes = False
            for k in string:
                if k == '0':
                    zeroes = True
            if not zeroes:
                pandigital = True
                for k in range(1, 10):
                    found = False
                    for h in string:
                        if str(k) == h:
                            found = True
                    if not found:
                        pandigital = False
                if pandigital:
                    used = False
                    for k in products:
                        if i * j == k:
                            used = True
                    if not used:
                        products.append(i * j)
                        sum += i * j
print(sum)
