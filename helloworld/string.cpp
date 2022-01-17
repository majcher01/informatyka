#include <iostream>
#include <string>
using namespace std;

string wyraz;
int dlugosc, i;
int main(){
    cout<<"podaj wyraz: ";
    cin >> wyraz;
    dlugosc = wyraz.size();
    cout<<endl<<wyraz[0];

     i=1;
    do{
        if((i%2)!=0){
            cout<<"x";
        }else{
            cout<<wyraz[i];
        }


        i++;
    }while(i<dlugosc);
    

    


    return 0;
}