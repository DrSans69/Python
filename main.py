from sys import stdin, stdout
try:
    from my_package import other
except ImportError:
    pass

stdin = open("input.txt", "r")
# stdout = open("output.txt", "w")
input = stdin.readline
print = stdout.write
def log(x: str = ''): stdout.write(str(x) + "\n")
def I(): return [int(i) for i in input().split()]


def main():
    n = int(input())
    print("Wish you luck!")


if __name__ == "__main__":
    main()
