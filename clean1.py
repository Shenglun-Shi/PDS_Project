import numpy as np
import numpy.linalg.linalg as lsq
import csv
import os
import json
import re
pathfile = "/home/shenglun/Dropbox/PDS_Project/Shenglun/"
import matplotlib.pyplot as plt
###############################################################
#Clean data for Unemployment rate change from 1980 to 2012
#There are 9 elections all together
f1 = open(pathfile + "URate1.csv",'r+')
f2 = open(pathfile + "ur.csv",'w')
'''
cnt = 0
for line in f1:
  sline = line.split(',')
	print sline[0]
	cnt += 1
	if cnt < 10:
		i = str(cnt)
		pat1 = 'LAUST0'+i+'000003'
		if re.match(sline[0],pat1):
			print sline[1]
	
	if cnt >= 10:
'''
for i in range(45):
#for i in range(8):	
	f1.next()
#	f1.readline()
cnt = 0
for line in f1:
	sline = line.split(',')
	#write into csv file; each state has a unique csv file to contain all
	#data needed.
	a = []

	for j in range(9):
		kk = float(sline[1+4*(j+1)])-float(sline[1+4*j])
		kkk = str(kk)
		print kkk
		a.append(str(kkk))
	#a = [str(sline[5]-sline[1]),str(sline[9]-sline[5]),str(sline[13]-sline[9]),str(sline[17]-sline[13]),str(sline[21]-sline[17]),str(sline[25]-sline[21]),str(sline[29]-sline[25]),str(sline[33]-sline[29]),str(sline[37]-sline[33])]
	writer = csv.writer(f2)
	writer.writerow(a)
	#print sline[1]
	cnt += 1
	if cnt > 50:
		break
	for j in range(7):
		f1.next()

f1.close()
f2.close()

################################################################
#Now let's clean the data for interest rate
#We now have the interest rate at the end of september before each 
#presidential election
f1 = open(pathfile + "interest_rate_monthly.csv",'r+')
a = []
for i in range(8):
	f1.next()

cnt = 0
for line in f1:
	sline = line.split(',')
	print sline[1]
	a.append(float(sline[1]))
	cnt += 1
	if cnt > 8:
		break

	for i in range(47):
		f1.next()
	
	#sline = line.split(',')

f2 = open(pathfile+"interest_rate.csv",'w')
writer = csv.writer(f2)
writer.writerow(a)
f1.close()
f2.close()
	
###############################################################
#Next we should clean the data for voting rate (total)
f1 = open(pathfile + "vote_rate.csv",'r+')
f2 = open(pathfile + "vr.csv",'w')
writer = csv.writer(f2)
cnt = 0
for i in range(2):
	f1.next()
for line in f1:
	sline = line.split(',')
	aaa = []
	year = np.array([[1,1980],[1,1984],[1,1988],[1,1992],[1,1996],[1,2000],[1,2004],[1,2008]])
	x = np.array(float(sline[1]))
	for i in range(7):
	#	a.append(int(sline[i+1]))
		a = np.array(float(sline[2+2*i]))
		x = np.vstack((x,a))
	print x
	'''
	if cnt == 30:
		plt.plot(x)
		plt.show()
	'''
	#Do the regression here:
	reg = lsq.lstsq(year,x)		
	rr = reg[0]
	a = rr[0]
	b = rr[1]
	a12 = float(a + 2012*b)
	print a12
	for i in range(8):
		aaa.append(float(x[i]))
	aaa.append(a12)
	writer.writerow(aaa)

	cnt += 1
	if cnt >50:
		break
	
f1.close()
f2.close()
'''
	a = []
	a.append(sline[1])
	for i in range(7):
		a.append(sline[2+2*i])

	writer.writerow(a)

f1.close()
f2.close()
'''
#############################################################
#Now clean up GDP data (growth rate)
f1 = open(pathfile + "GDP_63.csv",'r+')
f2 = open(pathfile + "gdp.csv",'w')
writer = csv.writer(f2)

for i in range(5):
	f1.next()
cnt = 0
for line in f1:
	sline = line.split(',')
	a = []
	for i in range(9):
		r = float(sline[19+4*i])/float(sline[15+4*i])
		a.append(r)
	
	writer.writerow(a)

	cnt += 1
	if cnt >50:
		break

############################################################
# Health Care! Don't have data for that before 1990, let's first
# see what the data is like and try to model it
f1 = open(pathfile + "med_income1.csv",'r+')
f2 = open(pathfile + "mi.csv",'w')
writer = csv.writer(f2)
cnt = 0
for i in range(2):
	f1.next()
for line in f1:
	sline = line.split(',')
	aaa = []
	year = np.array([[1,1984],[1,1988],[1,1992],[1,1996],[1,2000],[1,2004],[1,2008]])
	x = np.array(int(sline[1]))
	for i in range(1,7):
	#	a.append(int(sline[i+1]))
		a = np.array(int(sline[i+1]))
		x = np.vstack((x,a))
	print x
	'''
	if cnt == 10:
		plt.plot(x)
		plt.show()
	'''
	#Do the regression here:
	reg = lsq.lstsq(year,x)		
	rr = reg[0]
	a = rr[0]
	b = rr[1]
	a80 = round(a + 1980*b)
	a12 = round(a + 2012*b)
	print a80
	print a12
	aaa.append(a80)
	for i in range(0,7):
		aaa.append(int(sline[i+1]))
	aaa.append(a12)
	writer.writerow(aaa)

	cnt += 1
	if cnt >50:
		break
	
f1.close()
f2.close()
	
###########################################################
# Now we clean the presidential election result
f1 = open(pathfile + "result_state2.csv",'r+')
f2 = open(pathfile + "state_result.csv",'w')
writer = csv.writer(f2)
cnt = 0
for i in range(1):
	f1.next()
for line in f1:
	sline = line.split(',')
	aaa = []
	for i in range(1,10):
		print sline[i]
		if sline[i] == "R":
			aaa.append(0)
		elif sline[i] == "D":
			aaa.append(1)
		else:
			aaa.append(2)
	print aaa
	writer.writerow(aaa)
	cnt += 1
	if cnt>50:
		break
	
f1.close()
f2.close()



################################################################
#Clean electoral college data
f1 = open(pathfile + "elect_vote.csv",'r+')
f2 = open(pathfile + "ev.csv",'w')
writer = csv.writer(f2)
cnt = 0
for line in f1:
	sline = line.split(',')
	aaa = []
	for i in range(1,10):
		aaa.append(int(sline[i]))
	writer.writerow(aaa)

	cnt += 1
	if cnt >50:
		break
	
f1.close()
f2.close()


###############################################################
#Clean spending on education
import math
f1 = open(pathfile + "edu_spending.csv",'r+')
f2 = open(pathfile + "edu.csv",'w')
writer = csv.writer(f2)
cnt = 0
for i in range(3):
	f1.next()
for line in f1:
	cnt += 1
	sline = line.split(',')
	aaa = []
	year = np.array([[1,1992],[1,1996],[1,2000],[1,2004],[1,2008],[1,2012]])
	x = np.array(math.log(float(sline[5])))
	for i in range(5):
	#	a.append(int(sline[i+1]))
		a = np.array(math.log(float(sline[11+i*6])))
		x = np.vstack((x,a))
	print x
	
	#Do the regression here:
	reg = lsq.lstsq(year,x)		
	rr = reg[0]
	a = rr[0]
	b = rr[1]
	a80 = float(a + 1980*b)
	a80 = math.exp(a80)
	a84 = math.exp(float(a + 1984*b))
	a88 = math.exp(float(a + 1988*b))
	print a80
	print a12
	aaa.append(a80)
	aaa.append(a84)
	aaa.append(a88)
	
	for i in range(6):
		aaa.append(math.exp(float(x[i])))
	writer.writerow(aaa)
	if cnt ==2:
		plt.plot(aaa)
		plt.title('Actual and estimated number of spending on education for Arizona(randomly selected)')
		plt.ylabel('Spending in dollars')
		plt.xlabel('Years (0 for 1980 and 8 for 2012')
		plt.show()
	if cnt >50:
		break
	
f1.close()
f2.close()



###############################################################
#Clean spending on healthcare 
import math
f1 = open(pathfile + "healthcare_spending.csv",'r+')
f2 = open(pathfile + "health.csv",'w')
writer = csv.writer(f2)
cnt = 0
for i in range(2):
	f1.next()
for line in f1:
	sline = line.split(',')
	aaa = []
	year = np.array([[1,1992],[1,1996],[1,2000],[1,2004],[1,2008],[1,2012]])
	x = np.array(math.log(float(sline[5])))
	print cnt
	for i in range(5):
	#	a.append(int(sline[i+1]))
		a = np.array(math.log(float(sline[11+i*6])))
		x = np.vstack((x,a))
	print x
	
	#Do the regression here:
	reg = lsq.lstsq(year,x)		
	rr = reg[0]
	a = rr[0]
	b = rr[1]
	a80 = float(a + 1980*b)
	a80 = math.exp(a80)
	a84 = math.exp(float(a + 1984*b))
	a88 = math.exp(float(a + 1988*b))
	print a80
	print a12
	aaa.append(a80)
	aaa.append(a84)
	aaa.append(a88)
	for i in range(6):
		aaa.append(math.exp(float(x[i])))
	writer.writerow(aaa)
	
	if cnt ==5:
		plt.plot(aaa)
		plt.title('Actual and estimated number of spending on healthcare for California(randomly selected)')
		plt.ylabel('Spending in dollars')
		plt.xlabel('Years (0 for 1980 and 8 for 2012')
		plt.show()
	cnt += 1
	if cnt >50:
		break
	
f1.close()
f2.close()












