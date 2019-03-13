import gettext
import os

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')

es = gettext.translation('test', localedir, languages=['es'])
es.install()

# _ = es.gettext
_ = gettext.gettext


print(_('Hello Word'))
