import random

print random.randint(0, 1)
print random.uniform(0,1)

recordread = open('record')
record = recordread.readlines()
recordread.close()

print float(record[1])
if 1 > float(record[1]):
    recordmodify = open('record.txt','w')
    recordmodify.write('%s\n%s' % ('111', '234.5'))
    recordmodify.close()
    print '\n' \
          '\n' \
          '\n' \
          '************************************************ \n' \
          '******************CONGRADUATION***************** \n' \
          '*******************NEW**RECORD****************** \n' \
          '%s : $%.1f' \
          % (111, 234.5)