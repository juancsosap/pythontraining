# To create the file structure for I18n must be executed
# the pygettext.py tool available in the python instalation
# folder that must be referenced in the Environment Variables
# as PYTHONPATH

# set GETTEXT=%PYTHONPATH%\Tools\i18n\pygettext.py
# python %GETTEXT% -d <file_name> <script-name>.py

import gettext
import os

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')

es = gettext.translation('i18n', localedir, languages=['es'])
es.install()

_ = es.gettext
# _ = gettext.gettext

nombre = input(_('What is your Name?') + '\n')
print(_('Hello, {name}.').format(name=nombre))

print(_('Thanks, see you later.'))
