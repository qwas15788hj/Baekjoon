import sys
input = sys.stdin.readline

king, rock, n = map(str, input().split())
kx, ky = 8-int(king[1]), ord(king[0])-65
rx, ry = 8-int(rock[1]), ord(rock[0])-65

dire = ["R", "L", "B", "T", "RT", "LT", "RB", "LB"]
dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

for i in range(int(n)):
    d = input().strip()
    idx = dire.index(d)

    nkx, nky = kx + dx[idx], ky + dy[idx]
    if rx == nkx and ry == nky:
        nrx, nry = rx + dx[idx], ry + dy[idx]
    else:
        nrx, nry = rx, ry

    if 0 <= nkx < 8 and 0 <= nky < 8 and 0 <= nrx < 8 and 0 <= nry < 8:
        kx, ky, rx, ry = nkx, nky, nrx, nry

print(chr(ky+65) + str(8-kx))
print(chr(ry+65) + str(8-rx))