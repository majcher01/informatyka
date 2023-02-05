#include <iostream>

int a,b;
using namespace std;

int main(){

    do{
        cout<<"podaj a: ";
        cin>>a;
        cout<<endl<<"podaj b: ";
        cin>>b;

        cout<<endl<<a+b<<endl;
    }while((a+b)>0);

    cout<<"suma nie jest wieksza od zera, koniec"<<endl;


    return 0;
}