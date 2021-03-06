import sys, os
from jinja2 import Environment, FileSystemLoader

SRC_PATH = '.'

class LayoutBuilder(object):
    '''
    Handles building a full layout
    '''
    
    def __init__(self, theme):
        self.template_environment = Environment(
            loader=FileSystemLoader(theme)
        )
        self.theme = theme
    
    def buildLayout(self, layoutName):
        '''
        Build a given layout and return the result as a string.
        '''
        layoutFileName = layoutName
        if not layoutFileName.endswith('.html'):
            layoutFileName = layoutFileName + '.html'

        layoutPath = os.path.join('layouts', layoutFileName)
        t = self.template_environment.get_template(layoutPath)
        return t.render()
    
    def buildAll(self, path='../'):
        '''
        Builds all available layouts and saves them to the specified path.
        '''
        for layout in self.getLayouts():
            rendered = self.buildLayout(layout)
            
            f = open(os.path.join(path, layout), 'w')
            f.write(rendered)
            f.close()
    
    def getLayouts(self):
        '''
        Get a list of available layouts and return as a list, stripping file 
        extensions.
        '''
        layouts = []
        for cd, d, f in os.walk(os.path.join(self.theme, 'layouts')):
            for filename in f:
                layouts.append(filename)
        return layouts

def printHelp():
    print '''
build.py - Assembles various layouts based on a given theme.

Usage:
    build.py <command> <theme> [arguments]

Commands:
    help - Print this help and quit
    list <theme> - Lists available layouts (see docs)
    build <theme> <layout> - Outputs rendered <layout> to stdout
    buildall <theme> <path> - Build all available layouts and save to <path>
'''

def main(argv):
    if len(argv) < 1:
        print 'Not enough arguments.'
        printHelp()
        return 1

    command = argv[0]
    
    if command == 'help':
        printHelp()
        return 0
        
    builder = LayoutBuilder(argv[1])
    
    if command == 'build':
        print builder.buildLayout(argv[2])
    elif command == 'buildall':
        if len(argv) == 3:
            builder.buildAll(argv[2])
        else:
            builder.buildAll()
    elif command == 'list':
        print '\n'.join(builder.getLayouts())
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
