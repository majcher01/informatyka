#include <iostream>
#include <stdlib.h>

using namespace std;
int numer, strzal;
int x = 17;
int main(){

srand(time(0));

numer = rand() % 750 +1;



do{

cout<<endl<<endl<<"Pozostałych prób: "<<x;
cout <<endl<<endl<<"wprowadz liczbe: ";
cin>>strzal;


if(strzal>numer){
    cout <<endl<<"Wprowadzona liczba jest wieksza od wylosowanej";
}else if(strzal<numer){
    cout <<endl<<"Wprowadzona liczba jest mniejsza od wylosowanej";
}

if(strzal==numer){
    cout <<endl<<endl<< "Wygrałeś!";
    return 0;
}
x--;
}while((x>0) && (strzal!=numer));

cout<<endl<<endl<<"Przegrałeś, wylosowana liczba to: "<<numer;

    return 0;
}