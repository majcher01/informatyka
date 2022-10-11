#include <iostream>

using namespace std;

double i, l1, x, maximum, minimum, suma, srednia;

int main(){

	
	cout<<"podaj ilosc liczb: ";
	cin >>i;
	
	for(x=1;x<=i;x++){
		cout <<"podaj liczbe: ";
		cin >>l1;
		suma = suma + l1;
		if (x==1){
			maximum=l1;
			minimum=l1;
		}else{
		if (l1 > maximum){
			maximum = l1;
		}else if (l1<minimum){
			minimum=l1;
		}
	}
		
	}
	
	srednia = (suma/i);
	
	cout<<endl<<"najwieksza: "<<maximum<<endl<<"najmniejsza: "<<minimum<<endl<<"suma: "<<suma<<endl<<"srednia: "<<srednia<<endl;
	
	return 0;
}
