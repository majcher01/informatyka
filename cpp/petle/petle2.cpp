#include <iostream>
#include <string>

using namespace std;
int i,s,x,y, ilosc;
string dzielniki, powtorz;
int main(){
    do{
        cout <<"wybierz zadanie (1-3): ";
        cin>>s;
        switch(s){

        case 1:
        cout <<"wprowadz liczbe: ";
        cin >>x;
        y=1;
        for(i=1;i<(x+1);i++){
            y=y*i;

        }
        cout <<y;
        break;
        case 2:
        dzielniki="";
        cout <<"wprowadz liczbe: ";
        cin>>x;
        for(i=1;i<(x+1);i++){
            if((x%i)==0){
                ilosc = ilosc +1;
                dzielniki = dzielniki + " "+to_string(i);
                
            }
        }
        cout <<x<<" ma "<<ilosc<<" dzielnikow, i sa to: "<<dzielniki;
        break;
        case 3:
        ilosc = 0;
        cout <<"wprowadz liczbe: ";
        cin>>x;
        for(i=1;i<(x+1);i++){
            if((x%i)==0){
                ilosc = ilosc +1;  
            }
        }
        if(ilosc==2){
            cout <<x<<" jest liczba pierwsza.";
        }else{
            cout <<x<<" nie jest liczba pierwsza.";
        } 
        break;
        default:
        cout<<"wybrano nieprawidłowe zadanie.";
        break;

        }

        cout<<endl<<endl<<"powtorzyc ? (t/n)";
        cin>>powtorz;
    }while(powtorz=="t");

    
    

    return 0;
}