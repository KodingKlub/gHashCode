import wojtek as w
import philipp as p
import kordian as k
import sys

def solve():
    pass

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) == 2 else "data/small.in"
    with open(fname) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    print(content)
    solve()