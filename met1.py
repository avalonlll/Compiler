parlist = list();
leftpar=0;
rightpar=0;
var1=0;
var2=0;
flag=True;
r = open('prakseis.py','r+');
#print r.read() #to diabazei, ola ok
print"hre"
with open("prakseis.py") as r:
	data=r.read()
	print data
	if r=="(" :
		parlist.append("0");
		var1+=1
		print"here"
	elif r==")" :
		parlist.append("1");
		var2+=1
		print"or here"
		if (var2>var1) :
			print"NO";
			flag=False;
			#break;
	

	
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

