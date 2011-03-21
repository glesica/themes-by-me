import sys, os
from jinja2 import Environment, PackageLoader

class LayoutBuilder(object):
    '''
    Handles building a full layout
    '''
    
    def __init__(self):
        self.template_environment = Environment(
            loader=PackageLoader('nice', 'templates')
        )

    def getSection(name):
        template_file = name
        if not name.startswith('section_'):
            template = 'section_' + template_file
        if not name.endswith('.html'):
            template_file = template_file + '.html'
    
        t = template_environment.get_template(template_file)
        return t.render()
    
    def buildLayout(sections):
        context = {}
        
        for section in sections:
            context[section] = getSection(section)
        
        return 

def main(argv):
    

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
