def xeirismos():
	parlist = list();
	leftpar=0;
	rightpar=0;
	var1=0;
	var2=0;
	flag=True;
	k = 0
	with open(a) as r:
		for line in r:  
			for ch in line:
				if ch=="(" :
					parlist.append(0);
					var1+=1
					print"Found a left parenthesis"
				elif ch==")" :
					parlist.append(1);
					var2+=1
					print"Found a right parenthesis"
					if (var2>var1) :
						print"NO";
						flag=False;
						break;
	
		if (flag==False):
			for i in range (len(parlist)) :
				if parlist[i]==0:
					leftpar+=1
				elif parlist[i]==1:
					rightpar+=1
			print"i am here"
		if (rightpar==leftpar):
			print"YES"; 
			k = len(parlist);
			i=0;
			minus=0
			while i < k:
				j=0
				while j<k:
					if (parlist[i-minus]==0 & parlist[j-minus]==1) | (parlist[i-minus]==1 & parlist[j-minus]==0):
						parlist.remove(0)
						parlist.remove(1)
						k=k-2;
						minus = minus +1
						print parlist
						break
					j = j+1
				i=i+1
	print parlist

def xeirismos2():
	parlist = list();
	leftpar=0;
	rightpar=0;
	var1=0;
	var2=0;
	flag=True;
	with open(a) as r:
		for line in r:  
			for ch in line:
				if ch=="(" :
					parlist.append(0);
					var1+=1
					print"here"
				elif ch==")" :
					parlist.append(1);
					var2+=1
					print"or here"
					if (var2>var1) :
						print"NO";
						flag=False;
						break;
	
		if (flag==False):
			for i in range (parlist.length() ):
				if parlist[i]==0:
					leftpar+=1
				elif parlist[i]==1:
					rightpar+=1
			print"i am here"
		if (rightpar==leftpar):
			print"YES";
			
	print parlist



arxeio=raw_input("Please give files name\n")
a=str(arxeio)
r = open(a,'r+');
#print r.read() #to diabazei, ola ok
answer=raw_input("Do you want to print the steps? Press Y for yes, or N for no. ")
if answer =='y':
	xeirismos()
elif answer=='n':
	xeirismos2()
else:
	print"Wrong answer given from user"

