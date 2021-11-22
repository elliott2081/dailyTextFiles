import os
import configDateFolders

year = input("what year would you like")

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
		  'August', 'September', 'October', 'November', 'December']

monthDict = {'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr', '05':'May', '06':'Jun',
             '07':'Jul', '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}

days = {'01':'31', '02':'28', '03':'31', '04':'30', '05':'31', '06':'30',
       '07':'31', '08':'31', '09':'30', '10':'31', '11':'30', '12':'31'}

dir = configDateFolders.directoryForFolders + year

if not os.path.exists(dir):
	os.makedirs(dir)

os.chdir(dir)
for m in monthDict:
	if not os.path.exists(m):
		os.makedirs(m)

for root, dir, file in os.walk("."):
	for d in dir:
		os.chdir(d)
		for x in range(1, int(days[str(d)]) +1):
					if x < 10:
						open(year + "_" + str(d) + "_" + "0" + str(x) + ".txt" ,"x")
					else:
						open(year + "_" + str(d) + "_" + str(x) + ".txt" ,"x")
		path_parent = os.path.dirname(os.getcwd())
		os.chdir(path_parent)

