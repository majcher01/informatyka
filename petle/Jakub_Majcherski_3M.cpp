#include <iostream>

using namespace std;
int i, s, x, y;
int main(){
cout << "wybierz zadanie (1-4) ";
cin >>s;

switch(s){

    case 1:
    for(i=1;i<11;i++){
        cout <<i<<endl;
    }
    break;
    case 2:
    x=0;
    for(i=1;i<11;i++){
        x=x+i;
    }
    cout <<x<<endl;
    break;
    case 3:
    for(i=1;i<21;i++){
        if((i%2)==0){
            x=x+i;
        }
    }
    cout <<x;
    break;
    case 4:
    x=2;
    for(i=1;i<11;i++){
        y=y+x;
        x=x*2;
    }
    cout <<y;
    break;

    default:
    cout <<"nie wybrano zadania"<<endl;
    break;

}
    

    return 0;
}