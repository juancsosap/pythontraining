import gettext
import os

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')

es = gettext.translation('i18n', localedir, languages=['es'])
es.install()

_ = es.gettext
# _ = gettext.gettext

nombre = input(_('What is your Name?') + '\n')
print(_('Hello, {name}.').format(name=nombre))

edad = int(input(_('How old are you?') + '\n'))
msg = _(gettext.ngettext(
    'Then, you are {age} year old.',
    'Then, you are {age} years old.',
    edad)).format(age=edad)
print(msg)

print(_('Thanks, see you later.'))
