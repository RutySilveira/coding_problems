a, b = map(int, input().split())

rb = (b * (b + 1)) // 2
ra = (a * (a - 1)) // 2

if a <= 1:
    ra = 0

print(rb - ra)
