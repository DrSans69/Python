from sys import stdin, stdout
try:
    from my_package import other
    from my_package import benchmark
except:
    pass

stdin = open("input.txt", "r")
# stdout = open("output.txt", "w")
input = stdin.readline
print = stdout.write
def log(x): stdout.write(str(x) + "\n")
def I(): return [int(i) for i in input().split()]


@benchmark.benchmark()
def main():
    # other.create_tests()
    solve()


def solve():
    n = int(input())
    arr = I()
    all_threes = n ** 3
    total = 0


def old(n, arr):
    forbiden = dict(zip(range(1, n + 1), [set() for _ in range(n)]))
    for i, a in enumerate(arr, start=1):
        for j in range(a + 1, n + 1):
            forbiden[i].add(j)
            forbiden[j].add(i)
    for year in range(1, n + 1):
        allowed = set(range(1, n + 1)).difference(forbiden[year])
        for month in allowed:
            total += len(allowed.difference(forbiden[month]))
    log(total)


if __name__ == "__main__":
    main()
