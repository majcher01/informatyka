#include <iostream>

using namespace std;

int main(){

    cout <<"kwadrat"<<endl<<endl;

    for(int i=0;i<5;i++){

        for(int j=0;j<5;j++){
            cout<<"# ";
        }

        cout<<endl;
    }

    cout<<endl<<endl<<"prostokat 1"<<endl<<endl;

    for(int i=0;i<5;i++){

        for(int j=0;j<8;j++){
            cout<<"# ";
        }

        cout<<endl;
    }

    cout<<endl<<endl<<"prostokat 2"<<endl<<endl;

    for(int i=0;i<8;i++){

        for(int j=0;j<5;j++){
            cout<<"# ";
        }

        cout<<endl;
    }

    cout<<endl<<endl<<"trojkat"<<endl<<endl;

    for(int i=0;i<6;i++){

        for(int j=0;j<i;j++){
            cout<<"# ";
        }

        cout<<endl;
    }

//trapez

//ten trapez to dalo sie w sumie prosciej ale sobie poskladalem z 3 figur

    cout<<endl<<endl<<"trapez"<<endl<<endl;

    for(int i=1, k=5;i<6;i++,k--){
       // cout<<"i "<<i<<endl<<"k "<<k<<endl;
       for(int a=0;a<k;a++){
           cout<<"  ";
       }

       for(int a=0;a<i;a++){
           cout<<"# ";
       }

       for(int j=0;j<8;j++){
            cout<<"# ";
        }

        for(int j=0;j<i;j++){
            cout<<"# ";
        }

        cout<<endl;
    }



    return 0;
}