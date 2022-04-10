# Upside Down Triangle pattern
n = 5

for i in range(n):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing stars
    for j in range(2*(n-i)-1):
        print('*', end='')
    print()
# Triangle star pattern
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()
