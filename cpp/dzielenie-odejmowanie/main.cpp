#include <iostream>

using namespace std;

int a, b, licznik;

int main(){

    cout<<"wprowadz liczbe 1"<<endl;
    cin>>a;
    cout<<"wprowadz liczbe 2"<<endl;
    cin>>b;

licznik = 0;

while(a>0){
    a=a-b;
    if(a<0){
        break;
    }
    licznik++;
//    cout<<"a="<<a<<endl;
}

cout<<"wynik: "<<licznik<<endl;




    return 0;
}