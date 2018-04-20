import gettext
import os
import locale
from datetime import datetime

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')

locale.setlocale(locale.LC_ALL, 'es')

es = gettext.translation('i18n', localedir, languages=['es_ES'])
es.install()

_ = es.gettext
# _ = gettext.gettext

nombre = input(_('What is your Name?') + '\n')
print(_('Hello, {name}.').format(name=nombre))

fecha_str = input(_('When did your born?') + ' (DD-MM-YY)\n')
fecha = datetime.strptime(fecha_str, '%d-%m-%y')
hoy = datetime.now()
edad = int((hoy - fecha).days / 365)
print(_('You were born on {birthday}!!.').format(birthday=fecha.strftime('%A, %d %B %Y')))

msg = _(gettext.ngettext(
    'Then, you are {age} year old.',
    'Then, you are {age} years old.',
    edad)).format(age=edad)
print(msg)

print(_('Thanks, see you later.'))
