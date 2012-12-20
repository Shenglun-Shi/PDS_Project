import csv
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

pathfile = "/home/shenglun/Dropbox/PDS_Project/Shenglun/"

"""
First, open all csv files, prepare to extract data from files
"""
# Read from every csv file, build a numpy matrix, put all data in
# the matrix and then do the modeling
def creatTrainTest(i,XY):
  
	f2 = open(pathfile + "gdp.csv",'r+')
	f3 = open(pathfile + "mi.csv",'r+')
	f4 = open(pathfile + "ur.csv",'r+')
	f5 = open(pathfile + "vr.csv",'r+')
	f6 = open(pathfile + "edu.csv",'r+')
	f7 = open(pathfile + "health.csv",'r+')
	X2 = np.genfromtxt(f2,delimiter = ",")
	temp = X2[i,:]
	XY = np.vstack((XY,temp))
	'''
	X2 = np.genfromtxt(f2,delimiter = ",")
	XY = X2[i,:]
	'''
	X3 = np.genfromtxt(f3,delimiter = ",")
	temp = X3[i,:]
	XY = np.vstack((XY,temp))
	X4 = np.genfromtxt(f4,delimiter = ",")
	temp = X4[i,:]
	XY = np.vstack((XY,temp))
	X5 = np.genfromtxt(f5,delimiter = ",")
	temp = X5[i,:]
	XY = np.vstack((XY,temp))
	X6 = np.genfromtxt(f6,delimiter = ",")
	temp = X6[i,:]
	XY = np.vstack((XY,temp))
	X7 = np.genfromtxt(f7,delimiter = ",")
	temp = X7[i,:]
	XY = np.vstack((XY,temp))
	f2.close()
	f3.close()
	f4.close()
	f5.close()
	f6.close()
	f7.close()
	return XY
	
	'''
	global Y
	Y = np.genfromtxt(ff,delimiter = ",")
	'''	

def creatTrainTest2(i,XY):
	
	f2 = open(pathfile + "gdp.csv",'r+')
	f3 = open(pathfile + "mi.csv",'r+')
	f4 = open(pathfile + "ur.csv",'r+')
	f5 = open(pathfile + "vr.csv",'r+')
	X2 = np.genfromtxt(f2,delimiter = ",")
	temp = X2[i,:]
	XY = np.vstack((XY,temp))
	'''
	X2 = np.genfromtxt(f2,delimiter = ",")
	XY = X2[i,:]
	'''
	X3 = np.genfromtxt(f3,delimiter = ",")
	temp = X3[i,:]
	XY = np.vstack((XY,temp))
	X4 = np.genfromtxt(f4,delimiter = ",")
	temp = X4[i,:]
	XY = np.vstack((XY,temp))
	X5 = np.genfromtxt(f5,delimiter = ",")
	temp = X5[i,:]
	XY = np.vstack((XY,temp))
	f2.close()
	f3.close()
	f4.close()
	f5.close()
	return XY
	
votes1 = 0 
votes2 = 0
votes3 = 0
#Here put all names of states into one list
state_name = []
fs = open(pathfile + "state.csv",'r+')
for line in fs:
	sline = line.split(',')
	state_name.append(str(sline[0]))
fs.close()
#print state_name
result_2012 = []
#Don't forget to transpose the matrix!
'''
Now that we get X and Y for each state, put them into a loop,
and train the model with all data, finally, test the last two 
elections to see the result of the model
'''
for i in range(51):
	fk = open(pathfile + "state_result.csv",'r+')
	#global XY
	ff = open(pathfile + "result.csv",'r+')
	eee = open(pathfile + "ev.csv",'r+')
	f1 = open(pathfile + "interest_rate.csv",'r+')
	X1 = np.genfromtxt(f1,delimiter = ",")
	XY = X1[:]
	XY = creatTrainTest(i,XY)
#	print XY	
	tY = np.genfromtxt(fk,delimiter = ",")
	Y = tY[i,:]
	evv = np.genfromtxt(eee,delimiter = ",")
	evi = evv[i,:]
#	print evi
	if Y.sum() == len(Y) or Y.sum() == 0:
#		print "Not a swing state!"
		if Y.sum() == len(Y):
			votes1 += evi[8]
			result_2012.append(1)
		else:
			result_2012.append(0)
	else:
		XY = XY.T
#		print XY
#		print Y

		lr1 = LogisticRegression()
		lr1 = lr1.fit(XY[:8,:],Y[:8])
		v1 = lr1.predict(XY[8,:])
		votes1 += v1*evi[8]
#		print v1
		result_2012.append(int(v1))
		
	f1.close()
	fk.close()
	ff.close()
	eee.close()
	
#print votes1
#print	result_2012
'''
I just mannual checked, for 2012 result, we missed five states' results
'''
'''
if votes > 0.5* evi[8].sum():
	print  
'''
#####################################################
#Using only the first 5 factors
result_2012_5 = []
for i in range(51):
	fk = open(pathfile + "state_result.csv",'r+')
	#global XY
	ff = open(pathfile + "result.csv",'r+')
	eee = open(pathfile + "ev.csv",'r+')
	f1 = open(pathfile + "interest_rate.csv",'r+')
	X1 = np.genfromtxt(f1,delimiter = ",")
	XY = X1[:]
	XY = creatTrainTest2(i,XY)
#	print XY	
	tY = np.genfromtxt(fk,delimiter = ",")
	Y = tY[i,:]
	evv = np.genfromtxt(eee,delimiter = ",")
	evi = evv[i,:]
#	print evi
	if Y.sum() == len(Y) or Y.sum() == 0:
#		print "Not a swing state!"
		if Y.sum() == len(Y):
			votes3 += evi[8]
			result_2012_5.append(1)
		else:
			result_2012_5.append(0)
	else:
		XY = XY.T
#		print XY
#		print Y

		lr1 = LogisticRegression()
		lr1 = lr1.fit(XY[:8,:],Y[:8])
		v1 = lr1.predict(XY[8,:])
		votes3 += v1*evi[8]
#		print v1
		result_2012_5.append(int(v1))

	f1.close()
	fk.close()
	ff.close()
	eee.close()
	
#print votes3
#print	result_2012_5

####################################################
#Comparison of results:
#For the 7 factor model:
print "For the 7 factor model, we predict that Obama will win:"
for i in range(51):
	if result_2012[i] == 1:
		print state_name[i]
print "For the 7 factor model, we missed these states in terms of result:"
print "This is for 2012 Presidential election:"

fk = open(pathfile + "state_result.csv")
tY = np.genfromtxt(fk,delimiter = ",")
Y = tY[:,8]
Y = Y.T
for i in range(51):
	if Y[i] != result_2012[i]:
		print state_name[i]

fk.close()

print "For the 5 factor model, we predict that Obama will win:"
for i in range(51):
	if result_2012_5[i] == 1:
		print state_name[i]
print "\nFor the 5 factor model, we missed these states in terms of result:"
print "This is for 2012 Presidential election:"
fk = open(pathfile + "state_result.csv")
tY = np.genfromtxt(fk,delimiter = ",")
Y = tY[:,8]
Y = Y.T
for i in range(51):
	if Y[i] != result_2012_5[i]:
		print state_name[i]

fk.close()








'''
for i in range(51):
	fk = open(pathfile + "state_result.csv",'r+')
	#global XY
	ff = open(pathfile + "result.csv",'r+')
	eee = open(pathfile + "ev.csv",'r+')
	f1 = open(pathfile + "interest_rate.csv",'r+')
	X1 = np.genfromtxt(f1,delimiter = ",")
	XY = X1[:]
	XY = creatTrainTest(i,XY)
#	print XY	
	tY = np.genfromtxt(fk,delimiter = ",")
	Y = tY[i,:]
	Y1 = Y[1:]
#	Y1 = np.hstack((Y[:5],Y[6:]))
	evv = np.genfromtxt(eee,delimiter = ",")
	evi = evv[i,:]
#	print evi
	if Y.sum() == len(Y) or Y.sum() == 0 or Y1.sum() ==len(Y1) or Y1.sum() ==0:
		print "Not a swing state!"
		if Y1.sum() == len(Y1):
			votes2 += evi[0]
		else:
			votes2 += 0
	else:
		XY = XY.T
#		print XY
#		print Y
		XY2 = XY[1:,:]
#		XY2 = np.vstack((XY[:5,:],XY[6:,:]))
		lr2 = LogisticRegression()
		lr2 = lr2.fit(XY2,Y1)
		v1 = lr1.predict(XY[0,:])
		votes2 += v1*evi[0]
	f1.close()
	fk.close()
	ff.close()
	eee.close()
	
print votes2








'''
