import sys
if len(sys.argv) < 3:
    print("none")
else:
    x = sys.argv[1:]
    x.reverse()
    for i in x:
        print(i)