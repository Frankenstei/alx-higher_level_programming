#!/usr/bin/python3
if __name__ == "__main__":
    answer = 0
    import sys
    for i in range(1, len(sys.argv)):
        answer += int(sys.argv[i])
    print("{}".format(answer))
