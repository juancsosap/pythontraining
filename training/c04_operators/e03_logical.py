print('Logical Tables'.center(25))
print(''.center(25, '-'))

print(' AND '.center(25, '#'))
print('False'.ljust(7), 'False'.ljust(7), ':', False and False)
print('False'.ljust(7), 'True'.ljust(7), ':', False and True)
print('True'.ljust(7), 'False'.ljust(7), ':', True and False)
print('True'.ljust(7), 'True'.ljust(7), ':', True and True)

print(' OR '.center(25, '#'))
print('False'.ljust(7), 'False'.ljust(7), ':', False or False)
print('False'.ljust(7), 'True'.ljust(7), ':', False or True)
print('True'.ljust(7), 'False'.ljust(7), ':', True or False)
print('True'.ljust(7), 'True'.ljust(7), ':', True or True)

print(' NOT '.center(25, '#'))
print(''.ljust(7), 'False'.ljust(7), ':', not False)
print(''.ljust(7), 'True'.ljust(7), ':', not True)
print(''.center(25, '-'))
