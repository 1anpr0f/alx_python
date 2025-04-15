def number(*argv):
    print("{} arguments:".format(len(argv)))
    for i,k in enumerate(argv,start=1):
        print("{}:{}".format(i,k))
if __name__ == "__main__":
    number(1,2,234)