import sys, os
from jinja2 import Environment, FileSystemLoader

SRC_PATH = '.'

class LayoutBuilder(object):
    '''
    Handles building a full layout
    '''
    
    def __init__(self, template_path):
        self.template_environment = Environment(
            loader=FileSystemLoader(template_path)
        )
        self.template_path = template_path
    
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
    
    def getLayouts(self):
        '''
        Get a list of available layouts and return as a list, stripping file 
        extensions.
        '''
        layouts = []
        for cd, d, f in os.walk(os.path.join(self.template_path, 'layouts')):
            for filename in f:
                layouts.append(filename)
        return layouts

def printHelp():
    print '''
build.py - Assembles various layouts based on a given template.

Usage:
    build.py list - Lists available layouts (see docs)
    build.py build <layout> - Outputs the given layout to stdout
'''

def main(argv):
    builder = LayoutBuilder('nice/templates')
    
    if len(argv) == 0:
        printHelp()
        return 1

    command = argv[0]
    
    if command == 'build':
        print builder.buildLayout(argv[1])
    elif command == 'list':
        print '\n'.join(builder.getLayouts())
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
