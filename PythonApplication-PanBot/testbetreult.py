import module2
import module4
tl=[]
loglist=[43637, 43638, 43647, 43648, 43651, 43652, 43656, 43662, 43664, 43863, 43865, 43867, 43868, 43871, 43875, 43876, 43877, 43880, 43881, 43883, 43884, 43886, 43888, 43892, 43893, 43895, 43897, 43898, 43900, 43903, 43904, 43906, 43909, 43913, 43915, 43916, 43917, 43918, 43920, 43923, 43925, 43927, 43929, 43930, 43931, 43932, 43933, 43935, 43940, 43944, 43947, 43951, 43953, 43955, 43962, 43968, 43973, 43976, 43979, 43980, 43982, 43994, 43995, 43996, 44003, 44006, 44009, 44010, 44013, 44014, 44016, 44017, 44018, 44019, 44020, 44022, 44024, 44025, 44026, 44027, 44028, 44029, 44035, 44039, 44046, 44052, 44056, 44057, 44058, 44063, 44069, 44074, 44077, 44078, 44083, 44089, 44107, 44112, 44122, 44124, 44129, 44130, 44137, 44140, 44142, 44147, 44148, 44149, 44151, 44156, 44160]
for i in range(0,len(loglist),4):
	temp=module4.getrounddata(loglist[i])
	tl.append(temp)

result=module2.analyzedata(tl)

'''status=[]
for i in result:
	temp=module2.stats(i)
	status.append(temp)
'''
mywin=[]
for i in result:
	rno=i["roundno"]
	whowin=i["whowin"]


44124
{'run_at': datetime.datetime(2022, 2, 11, 8, 59, 21), 'bet_at': datetime.datetime(2022, 2, 11, 9, 0, 1)}
413.953
412.9
44129
{'run_at': datetime.datetime(2022, 2, 11, 9, 25), 'bet_at': datetime.datetime(2022, 2, 11, 9, 25, 40)}
416.716
416.1
44130
{'run_at': 

