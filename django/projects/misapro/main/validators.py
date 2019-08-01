from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _

@deconstructible
class PhoneValidator(RegexValidator):
	"""
	International Phone validator acording to E.164 ITU-T recommendation call "The international public telecommunication numbering plan"
	"""
	regex = r'^((00|\+)[0-9]{1,3})?([0-9]{6,14})$'
	message = _('Enter a valid phone number')