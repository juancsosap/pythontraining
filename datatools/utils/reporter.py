from jinja2 import Environment, FileSystemLoader
from IPython.core.display import HTML
import pdfkit

class ReportUtils:
    def __init__(self, template_name, title):
        env = Environment(loader=FileSystemLoader('.'))
        self.template = env.get_template(f'datatools/templates/{template_name}.html')
        self.vars = {'title':title, 'seccions':[]}
     
    def addseccion(self, category, seccion, title=None):
        self.vars['seccions'].append({'title':title, category:seccion})

    def gethtml(self):
        html_out = self.template.render(self.vars)
        return HTML(html_out)

    def topdf(self, filepath):
        html_out = self.template.render(self.vars)
        pdfkit.from_string(html_out.decode('utf-8'), filepath)
        
