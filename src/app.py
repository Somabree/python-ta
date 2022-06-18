import sys
import os


def prime(s):
    # your code goes here
    if s > 1:
        for i in range(2, int(s/2) +1):
            if (s %  i == 0):
                return False
        return True
    return False

def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
