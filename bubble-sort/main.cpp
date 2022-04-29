#include<iostream>
using namespace std;

void bubblesort(int tab[],int n)
{
	for(int i=0;i<n;i++)
		for(int j=1;j<n-i;j++) 
		if(tab[j-1]>tab[j])
		swap(tab[j-1], tab[j]);
}

int main()
{
		
	int tab[] = {5,1,7,24,7,1,2,4}; //tablica do posortowania
 
    int n =8;   //dlugosc tablicy
    
	
	bubblesort(tab,n);
	
	for(int i=0;i<n;i++){
          cout<<tab[i]<<" ";
    }
    cout<<endl;

  return 0;
}