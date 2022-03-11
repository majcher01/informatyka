#include <iostream>
#include <string>


using namespace std;
int proby;
int main() {
    string login = "andrzej";
    string haslo = "andrzejhaslo";
    string ulogin, uhaslo;
   

    do {
        cout << "podaj login: ";
        cin >> ulogin;
        cout << endl << "podaj haslo: ";
        cin >> uhaslo;

        if (ulogin != login && uhaslo != haslo) {
            cout << "podano nieprawidlowy login i haslo" << endl;
        }
        else if (uhaslo != haslo) {
            cout << "podano nieprawidlowe haslo" << endl;
        }
        else if(ulogin != login){
            cout << "podano nieprawidlowy login" << endl;
        }

        proby++;
    } while ((login != ulogin || haslo != uhaslo) && proby < 4);

    if(proby==4){
        cout<<endl<<"======================"<<endl<<"za duzo prob, zablokowano"<<endl<<"======================"<<endl;
    }else{
        cout<<endl<<"================="<<endl<<"ZALOGOWANO"<<endl<<"================="<<endl;
    }




    return 0;
}