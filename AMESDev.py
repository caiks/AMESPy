from AlignmentDevRepa import *
import csv

def aahr(uu,aa):
    return hhhr(uu,aahh(aa))

def decomperIO(uu,vv,hr,wmax,lmax,xmax,omax,bmax,mmax,umax,pmax,fmax,mult,seed):
    return parametersSystemsHistoryRepasDecomperMaxRollByMExcludedSelfHighestFmaxIORepa(wmax,lmax,xmax,omax,bmax,mmax,umax,pmax,fmax,mult,seed,uu,vv,hr)

# amesIO :: IO (System, Histogram, Histogram)

def amesIO():
	def intornull(s):
		if len(s) > 0:
			try:
				return ValInt(int(s))
			except ValueError:
				return ValStr(s)
		return ValStr("null")
	vv = []
	ll = []
	for row in csv.reader(open('train.csv','r'), delimiter=','):
		rr = list(row)
		if len(vv) == 0:
			vv = list(map(VarStr,rr))
		else:
			ss = list(map(ValStr,rr))
			ss[0] = intornull(rr[0])
			ss[1] = intornull(rr[1])
			ss[3] = intornull(rr[3])
			ss[4] = intornull(rr[4])
			ss[17] = intornull(rr[17])
			ss[18] = intornull(rr[18])
			ss[19] = intornull(rr[19])
			ss[20] = intornull(rr[20])
			ss[26] = intornull(rr[26])
			ss[34] = intornull(rr[34])
			ss[36] = intornull(rr[36])
			ss[37] = intornull(rr[37])
			ss[38] = intornull(rr[38])
			ss[43] = intornull(rr[43])
			ss[44] = intornull(rr[44])
			ss[45] = intornull(rr[45])
			ss[46] = intornull(rr[46])
			ss[47] = intornull(rr[47])
			ss[48] = intornull(rr[48])
			ss[49] = intornull(rr[49])
			ss[50] = intornull(rr[50])
			ss[51] = intornull(rr[51])
			ss[52] = intornull(rr[52])
			ss[54] = intornull(rr[54])
			ss[56] = intornull(rr[56])
			ss[59] = intornull(rr[59])
			ss[61] = intornull(rr[61])
			ss[62] = intornull(rr[62])
			ss[66] = intornull(rr[66])
			ss[67] = intornull(rr[67])
			ss[68] = intornull(rr[68])
			ss[69] = intornull(rr[69])
			ss[70] = intornull(rr[70])
			ss[71] = intornull(rr[71])
			ss[75] = intornull(rr[75])
			ss[76] = intornull(rr[76])
			ss[77] = intornull(rr[77])
			ss[80] = intornull(rr[80])
			ll.append((llss(list(zip(vv,ss))),1))
	aatr = llaa(ll)
	vv = []
	ll = []
	for row in csv.reader(open('test.csv','r'), delimiter=','):
		rr = list(row)
		if len(vv) == 0:
			vv = list(map(VarStr,rr))
		else:
			ss = list(map(ValStr,rr))
			ss[0] = intornull(rr[0])
			ss[1] = intornull(rr[1])
			ss[3] = intornull(rr[3])
			ss[4] = intornull(rr[4])
			ss[17] = intornull(rr[17])
			ss[18] = intornull(rr[18])
			ss[19] = intornull(rr[19])
			ss[20] = intornull(rr[20])
			ss[26] = intornull(rr[26])
			ss[34] = intornull(rr[34])
			ss[36] = intornull(rr[36])
			ss[37] = intornull(rr[37])
			ss[38] = intornull(rr[38])
			ss[43] = intornull(rr[43])
			ss[44] = intornull(rr[44])
			ss[45] = intornull(rr[45])
			ss[46] = intornull(rr[46])
			ss[47] = intornull(rr[47])
			ss[48] = intornull(rr[48])
			ss[49] = intornull(rr[49])
			ss[50] = intornull(rr[50])
			ss[51] = intornull(rr[51])
			ss[52] = intornull(rr[52])
			ss[54] = intornull(rr[54])
			ss[56] = intornull(rr[56])
			ss[59] = intornull(rr[59])
			ss[61] = intornull(rr[61])
			ss[62] = intornull(rr[62])
			ss[66] = intornull(rr[66])
			ss[67] = intornull(rr[67])
			ss[68] = intornull(rr[68])
			ss[69] = intornull(rr[69])
			ss[70] = intornull(rr[70])
			ss[71] = intornull(rr[71])
			ss[75] = intornull(rr[75])
			ss[76] = intornull(rr[76])
			ss[77] = intornull(rr[77])
			ll.append((llss(list(zip(vv,ss))),1))
	aate = llaa(ll)
	return (uunion(sys(aatr),sys(aate)),aatr,aate)

