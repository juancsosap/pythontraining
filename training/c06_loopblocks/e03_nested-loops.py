hora, minu = 0, 0
while(hora < 24):
    print('{0:02d}:{1:02d}'.format(hora, minu), end='  ')
    minu = minu + 15 if minu < 45 else 0
    hora += 1 if minu == 0 else 0


print('\n')


for hora in range(24):
    for minu in range(0, 60, 15):
        print('{0:02d}:{1:02d}'.format(hora, minu), end='  ')

print('\n')

hora = 0
while(hora < 24):
    minu = 0
    while(minu < 60):
        print('{0:02d}:{1:02d}'.format(hora, minu), end='  ')
        minu += 15
    hora += 1
