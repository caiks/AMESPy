from AlignmentDevRepa import *
import csv

def aahr(uu,aa):
    return hhhr(uu,aahh(aa))

def decomperIO(uu,vv,hr,wmax,lmax,xmax,omax,bmax,mmax,umax,pmax,fmax,mult,seed):
    return parametersSystemsHistoryRepasDecomperMaxRollByMExcludedSelfHighestFmaxIORepa(wmax,lmax,xmax,omax,bmax,mmax,umax,pmax,fmax,mult,seed,uu,vv,hr)

# isOrd :: System -> Variable -> Bool

def isOrd(uu,v):
	def isOrdVal(u):
		if u._cl == 2 or u._cl == 3:
			return True
		return False 
	uat = systemsVarsSetValue
	return any(map(isOrdVal,uat(uu,v)))

# bucket :: Int -> Histogram -> Variable -> Map.Map Value Value

def bucket(b,aa,v):
	def slice(k,ll):
		if len(ll) == 0:
			return []
		elif len(ll) < k:
			return [ll] 
		return [ll[:k]] + slice(k,ll[k:])
	ll = sorted([ssll(ss)[0][1] for (_,ss) in hhll(aahh(red(aa,sset([v]))))])
	return sdict(reversed([(i,j) for jj in slice(len(ll)//b,ll) for (i,j) in zip(jj,[jj[-1]]*len(jj))]))

# reframeb :: Histogram ->  Map.Map Variable (Map.Map Value Value) -> Histogram

def reframeb(aa,xx):
	def repl(ss,xx):
		ll = []
		for (v,u) in ssll(ss):
			(w,ww) = (v,sdict())
			if v in xx:
				(w,ww) = xx[v]
			if u in ww:
				ll.append((w,ww[u]))
			else:
				ll.append((w,u))
		return llss(ll)
	return llaa([(repl(ss,xx),q) for (ss,q) in aall(aa)])

# amesIO :: IO (System, Histogram, Histogram)

def amesIO():
	def intornull(s):
		if len(s) > 0:
			try:
				return ValInt(int(s))
			except ValueError:
				return ValStr("null")
		return ValStr("null")
	vv = []
	ll = []
	for row in csv.reader(open('train.csv','r'), delimiter=','):
		rr = list(row)
		if len(vv) == 0:
			vv = list(map(VarStr,rr))
		else:
			ss = list(map(ValStr,rr))
			for i in [0,1,3,4,17,18,19,20,26,34,36,37,38,43,44,45,46,47,48,49,50,51,52,54,56,59,61,62,66,67,68,69,70,71,75,76,77,80]:
				ss[i] = intornull(rr[i])
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
			for i in [0,1,3,4,17,18,19,20,26,34,36,37,38,43,44,45,46,47,48,49,50,51,52,54,56,59,61,62,66,67,68,69,70,71,75,76,77]:
				ss[i] = intornull(rr[i])
			ll.append((llss(list(zip(vv,ss))),1))
	aate = llaa(ll)
	return (uunion(sys(aatr),sys(aate)),aatr,aate)

# amesBucketedIO :: Int -> IO (System, Histogram, Histogram)

def amesBucketedIO(b):
	(uu,aatr,aate) = amesIO()
	vv = uvars(uu) - sset([VarStr("Id")])
	vvl = sset([VarStr("SalePrice")])
	vvk = vv - vvl
	aa = add(red(aatr,vvk),red(aate,vvk))
	vvo = sset([w for w in vv for u in [vol(uu,sset([w]))] if isOrd(uu,w) if u > 16])
	vvoz = sset([w for w in vvk & vvo for rr in [unit(sset([llss([(w,ValInt(0))])]))] for bb in [mul(red(aatr,sset([w])),rr)] if size(bb) > 100])
	xx = sdict()
	for v in vvk & (vvo - vvoz):
		xx[v] = (VarStr(str(v)+"B"),bucket(20,aa,v))
	xx[VarStr("SalePrice")] = (VarStr("SalePrice"+"B"),bucket(20,aatr,VarStr("SalePrice")))
	for v in vvk & vvoz:
		rr = unit(sset([llss([(v,ValInt(0))])]))
		bb = mul(red(aa,sset([v])),rr)
		aa1 = trim(sub(red(aa,sset([v])),bb))
		xx[v] = (VarStr(str(v)+"B"),bucket(20,aa1,v))
	aab = reframeb(aa,xx)
	aatrb = reframeb(aatr,xx)
	aateb = reframeb(aate,xx)
	uub = uunion(sys(aab),uunion(sys(aatrb),sys(aateb)))
	return (uub,aab,aatrb,aateb)


