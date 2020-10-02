pentagons = []
n = 1
done = False
while done is False:
    p = int(n*(3*n-1)/2)
    for pent in pentagons:
        if p - pent in pentagons and p - 2 * pent in pentagons:
            print("Pentagons:", pent, p - pent, "- Difference:", p - 2 *pent)
            done = True
            break
    pentagons.append(p)
    n += 1
    # print(pentagons)
