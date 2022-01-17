#include <iostream> //dołączenie biblioteki 

using namespace std; //określenie używanej przestrzeni nazw

int zadanie,liczba; //deklaracja zmiennej
double a,b,h,pole;
string powtorz;

int main(){  //główna funkcja, po uruchomieniu programu będą wykonywane zawarte w niej instrukcje
start:
cout <<"wybierz zadanie (2-5): ";  //wyswietlenie tekstu na ekran
cin>>zadanie;  //wprowadzenie wartości z klawiatury do zmiennej
switch (zadanie) {   
        case 2:
            cout <<"wprowadz pierwsza liczbe: ";
            cin >>a;
            cout<<endl<<"wprowadz druga liczbe: ";
            cin>>b;
            cout <<endl<<endl<<"roznica liczb wynosi: "<<(a-b)<<endl;
            break;
        case 3:
            cout<<"wprowadz dlugosc pierwszej podstawy: ";
            cin>>a;
            cout<<"wprowadz dlugosc drugiej podstawy: ";
            cin>>b;
            cout<<"wprowadz dlugosc wysokosci: ";
            cin>>h;
            pole = ((a+b)*h)/2;
            cout<<endl<<endl<<"pole powierzchni trapezu jest równe: "<<pole<<endl;
            break;
        case 4:
            cout << "Wprowadz liczbe: ";
            cin >> liczba;

            if ((liczba % 2) == 1) {
                cout << "Liczba nie jest parzysta" << endl;
            }
            else {
                  cout << "liczba jest parzysta" << endl;
             }
            break;
            
        case 5:
           cout<<"wprowadz pierwsza liczbe: ";
            cin>>a;
            cout<<"wprowadz druga liczbe: ";
            cin>>b;
            cout<<"wprowadz trzecia liczbe: ";
            cin>>h;

            if(a>b && a>h){
                cout <<"liczba największa to: "<<a<<endl;
            }else if(b>a && b>h){
                cout <<"liczba największa to: "<<b<<endl;
            }else {
                cout <<"liczba największa to: "<<h<<endl;
            }
            break;
            
            
        
            
        }

        cout<<"powtórzyć ? (t/n) ";
        cin >>powtorz;
        if(powtorz=="t"){
            goto start;
        }

    return 0; //zakończenie programu i zwrócenie zera
}