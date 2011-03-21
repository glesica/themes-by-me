import sys, os

def getSection(name):
    try:
        sfile = open(os.path.join('src', name + '.html'), 'r')
        return sfile.readlines()
    except IOError:
        return ''

def main(argv):
    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))