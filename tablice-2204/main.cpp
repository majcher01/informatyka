#include <iostream>

using namespace std;

int tablica[]={49,13,1,52,-2,-22,0,23,4,-6,23,111,-52};

int main(){

cout<<"Zawartosc tablicy:"<<endl;
for(int x : tablica){
    cout<<x<<", ";
}

tablica[3]=100, tablica[5]=-33;

cout<<"Elementy 3 i 5 po zmianie:"<<endl<<tablica[3]<<" "<<tablica[5]<<endl;


    return 0;
}