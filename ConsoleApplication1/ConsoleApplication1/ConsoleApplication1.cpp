// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include "string"
using namespace std;
char namear[1000];
char gen[1000];
char prv[1000];
string name;
void shiftright(char myarray[], int size)
{
	for (int i = 99; i>=0; i--)
	{
		myarray[i] = myarray[i - 1];
	}
	
}
void rotateleft(char myarray[], int size)
{

	char temp = myarray[0];

	for (int i = 0; i<(size - 1); i++)
	{
		myarray[i] = myarray[i + 1];
	}
	myarray[size - 1] = temp;

}
void getChar(int i) {
	for (int a = 0; a <= i + 1; a++) {
		prv[a] = gen[a];
	}
	if (namear[i + 1] == '[') {
		if (gen[i + 1] == 'A') {
			prv[i + 1] = 'B';
			prv[i + 2] = 'E';
			shiftright(gen, 100);

		}
		if (gen[i + 1] == 'B') {
			prv[i + 1] = 'S';
		}
		if (gen[i + 1] == 'S') {
			prv[i + 1] = '[';
			prv[i + 2] = 'A';
			prv[i + 3] = ']';
			shiftright(gen, 100);
			shiftright(gen, 100);
		}
	}
	if (namear[i + 1] == 'y') {
		if (gen[i + 1] == 'A') {
			prv[i + 1] = 'B';
			prv[i + 2] = 'E';
			shiftright(gen, 100);
		}
		if (gen[i + 1] == 'B') {
			prv[i + 1] = 'y';
		}
	}
	if (namear[i + 1] == ':') {
		prv[i + 1] = ':';
		prv[i + 2] = 'A';
		shiftright(gen, 100);
	}
	if (namear[i + 1] == 'x') {
		if (gen[i + 1] == 'A') {
			prv[i + 1] = 'B';
			prv[i + 2] = 'E';
			shiftright(gen, 100);
		}
		if (gen[i + 1] == 'B') {
			prv[i + 1] = 'x';
		}
	}
	if (namear[i + 1] == '+') {
		prv[i + 1] = '+';
		prv[i + 2] = 'A';
		shiftright(gen, 100);
	}
	if (namear[i + 1] == ']') {
		//prv[i + 1] = 'å';
		gen[0] = NULL;
		prv[i + 1] = ']';
		rotateleft(gen, 1000);
	}
	for (int z = 0;prv[z]!=NULL;z++) {
		gen[z] = prv[z];
	}




}



int main()
{
	int x;
	//for (int s = 0;s < 1000;s++) {
	//	gen[s] = ' ';
	//	prv[s] = ' ';
	//	namear[s] = ' ';
	//}
	cout << "Please, enter your full name: ";
	getline(cin, name);
	cout << name.length() << endl;
	for (int i = 0; i < name.length();i++) {
		namear[i] = name[i];
		cout << namear[i] << endl;
	}
	cin >> x;
	gen[0] = '['; gen[1] = 'A';gen[2] = ']';
	int pointer = 0;
	while (true) {
		getChar(pointer);
		if (gen[pointer + 1] == 'x' || gen[pointer + 1] == 'y' || gen[pointer + 1] == 'å' || gen[pointer + 1] == ':' || gen[pointer + 1] == '+' || gen[pointer + 1] == '[' || gen[pointer + 1] == ']')
			pointer++;
		if (pointer == name.length()-1)
			break;
		for (int k = 0;k < 1000;k++) {
			if (gen[k] == NULL) {
				break;
			}
			cout << gen[k];

		}
		cout << endl;
	}



	return 0;
}

