triangles = [[1],1]
pentagons = [[1],1]
hexagons = [[1],1]

while True:
    m = min(triangles[0][-1], pentagons[0][-1], hexagons[0][-1])
    if triangles[0][-1] == m:
        triangles[1] += 1
        n = int(triangles[1] * (triangles[1] + 1) / 2)
        triangles[0].append(n)
    elif pentagons[0][-1] == m:
        pentagons[1] += 1
        n = int(pentagons[1] * (3 * pentagons[1] - 1) / 2)
        pentagons[0].append(n)
    elif hexagons[0][-1] == m:
        hexagons[1] += 1
        n = int(hexagons[1] * (2 * hexagons[1] - 1))
        hexagons[0].append(n)
    else:
        print('ERROR')
        break

    if pentagons[0][-1] == triangles[0][-1] == hexagons[0][-1] != 40755:
        print(pentagons[0][-1])
        break
