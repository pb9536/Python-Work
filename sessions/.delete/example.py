import sys

f = open("db.txt", "rw+")
roll_nums = []
records = f.read().strip().split("\n")
f.close()
if len(records) > 1:
	for record in records:
		roll_nums.append(record.split()[0])

records = []
while True:
	record = {}
	quit = raw_input("'y'/'n'>>")
	if quit == 'n':
		break
	num = raw_input("Roll Number>>")
	if num in roll_nums:
		print "Already exist"
		break
	record['num'] = num
	fname = raw_input("Firstname>>")
	record['fname'] = fname
	lname = raw_input("Lastname>>")
	record['lname'] = lname
	records.append(record)

f = open("db.txt", "a")
for record in records:
	f.write("{} {} {}\n".format(record['num'], record['fname'], record['lname']))
f.close()
