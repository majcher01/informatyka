#include <iostream>
#include <string>
#include <string.h>

using namespace std;

string slowo;


int main(){
    cout<<"wpisz slowo: ";
    cin >> slowo;

    char arr[slowo.length()];
    int arrasc[slowo.length()];
    strcpy(arr,slowo.c_str());

    for(int i = 0; i < slowo.length(); i++){
        arrasc[i]=arr[i];      
    }

     for(int i = 0; i < slowo.length(); i++){
        int x = arrasc[i];
        int y = arrasc[i + 1];
        //cout <<x<<" "<<y;
        if((x+y)==220){
            
            cout <<endl<<"Suma "<<char(x)<<" oraz "<<char(y)<<" jest rowna 220";
        
            return 0;
            
        }
    }

    
    cout <<endl<<"Nie znaleziono znakow ktorych suma jest rowna 220";
    

    return 0;
}

