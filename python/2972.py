def pop(u):
    ans = 0
    while u:
        u &= (u - 1)
        ans += 1
    return ans


n = int(input())
print(1 << pop(n))
