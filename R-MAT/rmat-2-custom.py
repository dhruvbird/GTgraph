import sys
from random import sample

def main(argc, argv):
    num_sources = 1
    n = 0
    m = 0

    if argc > 1:
        num_sources = int(argv[1])

    try:
        while True:
            line = raw_input()
            parts = line.split()
            if len(parts) == 4:
                    if parts[0] == 'a':
                        print parts[1], parts[2]
                    elif parts[0:2] == ['p', 'sp']:
                        print parts[2], parts[3], num_sources
                        n = int(parts[2])
                        m = int(parts[3])
            else:
                pass
    except:
        pass

    for i in sample(xrange(n), num_sources):
        print i

    return 0

if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
