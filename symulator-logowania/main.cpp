#include <iostream>
#include <string>

string login="andrzej", haslo="hasloandrzeja";
string ulogin="", uhaslo="";
int x, proby;
using namespace std;

int main(){


    do{
        cout<<"podaj login: ";
        cin >> ulogin;
        cout<<endl<<"podaj haslo: ";
        cin >> uhaslo;

        if(ulogin != login){
            cout<<"podano nieprawidlowy login"<<endl;
        }else if(uhaslo != haslo){
            cout<<"podano nieprawidlowe haslo"<<endl;
        }else{
            cout<<"login oraz haslo sa nieprawidlowe"<<endl;
        }

        proby++;
        cout<<"proby: "<<proby<<endl;
    }while((login==ulogin && haslo==uhaslo) && proby<4);

    cout<<"konirc";



    return 0;
}