#include <iostream>
#include <string>
using namespace std;


int wybor;
double bok1;
double bok2;
double bok3;
double wynik;
string powtorzyc ="";

int main () {
start:
	
cout << "pole jakiej figury chcesz obliczyc ?"<<endl;
cout << "kwadrat [1]"<<endl<<"prostokat [2]"<<endl<<"trojkat [3]"<<endl<<"trapez [4]"<<endl<<"rownoleglobok [5]"<<endl;
cin >>wybor;

switch (wybor){
	case 1:
		cout<<"wprowadz dlugosc boku: "<<endl;
		cin>>bok1;
		wynik = bok1*bok1;
		cout << wynik;
	break;
	case 2:
		cout <<"wprowadz dlugosc boku 1: "<<endl;
		cin>>bok1;
		cout<<"wprowadz dlugosc boku 2: "<<endl;
		cin>>bok2;
		wynik = bok1*bok2;
		cout<<wynik;
	break;
	case 3:
		cout<<"wprowadz dlugosc podstawy: "<<endl;
		cin>>bok1;
		cout<<"wprowadz dlugosc wysokosci: "<<endl;
		cin>>bok2;
		wynik=(bok1*bok2)/2;
		cout<<wynik;
	break;
	case 4:
		cout <<"wprowadz dlugosc ramienia 1: "<<endl;
		cin>>bok1;
		cout<<"wprowadz dlugosc ramienia 2: "<<endl;
		cin>>bok2;
		cout<<"wprowadz dlugosc wysokosci: "<<endl;
		cin>>bok3;
		wynik = ((bok1+bok2)*bok3)/2;
		cout<<wynik;
	break;
	case 5:
		cout<<"wprowadz dlugosc boku 1: "<<endl;
		cin>>bok1;
		cout<<"wprowadz dlugosc wysokosci: "<<endl;
		cin>>bok2;
		wynik=bok1*bok2;
		cout<<wynik;
	break;
}
cout<<endl;
cout <<"powtorzyc ? (t/n)"<<endl;
cin>>powtorzyc;
if(powtorzyc=="t"){
	goto start;
}else {
	return 0;
}
}
