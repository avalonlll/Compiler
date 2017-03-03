string1 = raw_input("Eisagogh parastashs");
lista=list(string1);
mhkos=len(lista);
print "to mhkos ton oron ths listas einai:", mhkos;
print list(string1);
steps = ['e'];
for i in range(mhkos-1, 0 ,-1):
	if lista[i]=='+':
		steps += ['+'];
		steps += ['o'];
steps[0] = 'o';
print steps;

mhkos1=len(steps);
pointer = 0;
prv=0;
final = ['o'];
steps.pop(0);
for i in range (0,mhkos1,2):
	while(lista[pointer] !='+'):
		if pointer < len(lista)-1:
			pointer = pointer +1;
	if pointer - prv != 2:
		for i in range(pointer,prv,-1):
			if lista[i] == '*':
				final += ['*'];
				final += ['p'];
				print final , steps;
	else:
		final.pop(len(final)-1);
		final += ['p'];
		print final , steps; 
	if prv==0:
		final[prv] = 'p';
		print final , steps;
	if prv >0:
		final[prv+1] = 'p';
		print final , steps;
	for i in range(pointer):
		if final[i]== 'p':
			final[i] = lista[i];
			print final , steps;
	prv = pointer;
	pointer = pointer + 1;
	final += ['+'];
	final += ['o'];
	steps.pop(0);
	steps.pop(0);
	print final , steps , pointer;


