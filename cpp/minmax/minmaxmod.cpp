#include <iostream>

using namespace std;

double x, l1, maximum, minimum, suma, srednia;

int main(){
x=1;
cout <<"podaj liczbe: ";
cin >> l1;
suma = l1;
maximum = l1;
minimum = l1;

do {
	cout <<"podaj liczbe: ";
	cin >> l1;
	suma = suma + l1;
	if(l1!=0){
	if (l1>maximum){
		maximum=l1;
	}else if(l1<minimum){
		minimum=l1;
	}
}
	
	x++;
}
while(l1!=0);
x=x-1;
cout <<endl<<"max: "<<maximum<<endl<<"min: "<<minimum<<endl<<"suma: "<<suma<<endl<<"srednia: "<<(suma/x)<<endl;
	

	
	return 0;
}
