%{
	#include <stdio.h>
	#include <stdbool.h>
	int count;
	bool NvS, WrongPnt, DblPnt;
	char MyString[100];

%}


letter [a-z]
P [A-D]


%%
[^{letter} /t/n] { NvS = true; } //NotValidString
{letter}|[/t/n] { count++;  }

tetragwno {
	if (MyString[count-4] != ' ' )
		WrongPnt=true;
	else{
		for (int i=count-4;i<count;i++){
			for (int j=i+1; j<count;j++){
				if (MyString[i]=MyString[j])
					DblPnt=true;
			}
		}
	}
}

trigwno {
	if (MyString[count-3] != ' ' )
		WrongPnt=true;
	else{
		for (int i=count-3;i<count;i++){
			for (int j=i+1; j<count;j++){
				if (MyString[i]=MyString[j])
					DblPnt=true;
			}
		}
            }
}
gwnia {
	if (MyString[count-1] != ' ' )
		WrongPnt=true;
 }
%%
int main(void) {
	yylex();
	char Scanned;
	scanf("Dwse protash %c",Scanned);
   	
	MyString[] = Scanned;
	return 0;
}
