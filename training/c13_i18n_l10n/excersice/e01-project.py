import gettext
import os
import locale
from datetime import datetime
from decimal import Decimal

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')

locale.setlocale(locale.LC_ALL, 'es')

es = gettext.translation('i18n', localedir, languages=['es_ES'])
es.install()

_ = es.gettext

print(_("Project Estimation Tool"))

nombre = input(_('Project Name') + ': ')

fecha_ini = input(_('Project Begin') + ' (DD-MM-YY): ')
fecha_ini = datetime.strptime(fecha_ini, '%d-%m-%y')

fecha_fin = input(_('Project End') + ' (DD-MM-YY): ')
fecha_fin = datetime.strptime(fecha_fin, '%d-%m-%y')

duracion = int((fecha_fin - fecha_ini).days)

costo_dia = float(input(_('Cost per Day') + ': '))
costo_total = costo_dia * duracion

msg = _(gettext.ngettext(
    'The project will have a duration of {days:,d} day.',
    'The project will have a duration of {days:,d} days.',
    duracion)).format(days=duracion)
print(msg)

print(_('The total cost will be {cost:n} USD.').format(cost=Decimal(costo_total)))

print(_("Thanks for you election"))
