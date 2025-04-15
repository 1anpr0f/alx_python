import sys
def main():
    argv = sys.argv[1:]
    count = len(argv)
    if count == 1:
        print("{} argument:".format(count))
    elif count == 0:
        print("{} arguments.".format(count))
    else:
        print("{} arguments:".format(count))   
    for i,arg in enumerate(argv,start=1):
        print("{}: {}".format(i,arg))
if __name__ == "__main__":
    main()