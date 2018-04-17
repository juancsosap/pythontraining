def logging(outType, filePath):
	def decorator(func):
		def inside(*args, **kwargs):
			log = f'Method {args[0].__class__.__name__}.{func.__name__}() was called.\n'
			if outType == 'file':
				with open(filePath, 'a') as logFile:
					logFile.write(log)
			elif outType == 'console':
				print(log, end='')
			func(*args, **kwargs)
		return inside
	return decorator

class ValidatorArgumentsError(Exception):
	pass

def validator(*vargs):
	def decorator(func):
		def inside(*args):
			if len(vargs)-1 == len(args):
				for i in range(len(args)):
					if not isinstance(args[i], vargs[i]):
						msg = f'The argument {i+1} do not math with the type required.'
						raise ValidatorArgumentsError(msg)
			else:
				msg = f'The amount of arguments in the Decorator do not match with the amount of arguments in the function {func.__name__}'
				raise ValidatorArgumentsError(msg)
			result = func(*args)
			if isinstance(result, vargs[0]):
				return result
			else:
				msg = f'The return value type do not math with the type required.'
				raise ValidatorArgumentsError(msg)
		return inside
	return decorator


def suppresserrors(func):
	def inside(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except Exception as e:
			print(f'Error: {e}')
	return inside

@suppresserrors
def divition(x, y):
	return x/y

@validator(float, float, float)
def add(x, y):
	return x+y


class Number:

	@logging('file', 'logging.log')
	def __init__(self):
		self.number = self.valor()

	@logging('console','logging.log')
	def valor(self):
		return 10

if __name__ == '__main__':
	print(Number().number)
	print(add(5.0, 5.0))

	divition(z=1)
	divition(1)
	divition(1,0)
	divition(1,'2')


