
'''
SPACE NEEDLE
for loop practice assignment
By: Phil Boothe
'''


#thin needle - 4 rows
for i in range(4):
	row = ''
	for j in range(12):
		row += ' '
	row += '||'
	print row
#top of dome - 4 rows
for i in range(4):
	row = ''
	for j in range(9 - 3*i):
		row += ' '
	row += '__/'
	for j in range(3*i):
		row += ':'
	row += '||'
	for j in range(3*i):
		row += ':'
	print row + '\\__'
#center of dome
row = '|'
for j in range(24):
	row += '"'
print row + '|'
#bottom of dome - 4 rows
for i in range(4):
	row = ''
	for j in range(0 + 2*i):
		row += ' '
	row += '\\_'
	for j in range(11 - 2*i):
		row += '/\\'
	print row + '_/'
#thin needle - 4 rows
for i in range(4):
	row = ''
	for j in range(12):
		row += ' '
	row += '||'
	print row
#thick needle - 16 rows
for i in range(16):
	row = ''
	for j in range(9):
		row += ' '
	print row + '|%%||%%|'
#base - 4 rows
for i in range(4):
	row = ''
	for j in range(9 - 3*i):
		row += ' '
	row += '__/'
	for j in range(3*i):
		row += ':'
	row += '||'
	for j in range(3*i):
		row += ':'
	print row + '\\__'
#bottom row
row = '|'
for j in range(24):
	row += '"'
print row + '|'
