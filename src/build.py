import sys, os
from jinja2 import Environment, FileSystemLoader

SRC_PATH = '.'

class LayoutBuilder(object):
    '''
    Handles building a full layout
    '''
    
    def __init__(self):
        self.template_environment = Environment(
            loader=FileSystemLoader('nice/templates')
        )
    
    def buildLayout(self, layoutName):
        layoutFileName = layoutName
        if not layoutFileName.endswith('.html'):
            layoutFileName = layoutFileName + '.html'

        layoutPath = os.path.join(SRC_PATH, 'layouts', layoutFileName)
        t = self.template_environment.get_template(layoutPath)
        return t.render()

def main(argv):
    builder = LayoutBuilder()
    print builder.buildLayout(argv[0])

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
