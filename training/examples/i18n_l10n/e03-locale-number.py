import gettext
import os
import locale
from decimal import Decimal

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')

locale.setlocale(locale.LC_ALL, 'es')

es = gettext.translation('i18n', localedir, languages=['es_ES'])
es.install()

_ = es.gettext
# _ = gettext.gettext

nombre = input(_('What is your Name?') + '\n')
print(_('Hello, {name}.').format(name=nombre))

sueldo = float(input(_('How much do you earn?') + '\n'))
print(_('{salary:n} USD is good.').format(salary=Decimal(sueldo)))

print(_('Thanks, see you later.'))
