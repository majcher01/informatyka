#include <iostream>

using namespace std;

int tablica[]={49,13,1,52,-2,-22,0,23,4,-6,23,111,-52};
int y;
int main(){

cout<<"Zawartosc tablicy:"<<endl;
for(int x : tablica){
    cout<<x<<" ";
}

tablica[2]=100, tablica[4]=-33;

cout<<endl<<"Tablica po zmianie:"<<endl;
for(int x : tablica){
    cout<<x<<" ";
}

cout<<endl<<"Dodatnie elementy:"<<endl;

for(int x : tablica){
    if(x>0){
        cout<<x<<" ";
    }
}

cout<<endl<<"Ilosc ujemnych elementów:"<<endl;

for(int x : tablica){
    if(x<0){
        y=y+1;
    }
}
cout<<y;

y=0;

cout<<endl<<"Elementy mniejsze od 10:"<<endl;

for(int x : tablica){
    if(x<10){
        cout<<x<<" ";
    }
}
cout<<y;

y=0;

cout<<endl<<"Suma wszystkich elementow:"<<endl;

for(int x : tablica){
    y=y+x;
}
cout<<y;

cout<<endl<<"Srednia:"<<endl<<(y/13)<<endl;



    return 0;
}