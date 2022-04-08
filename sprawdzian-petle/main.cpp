#include <iostream>

using namespace std;
int s, x;

int main()
{
    cout << "Wybierz zadanie (1-5) ";
    cin >> s;

    switch (s) {
    case 1:
        for (int i = 1; i < 21; i++) {
            cout << i << endl;
        }
    break;

    case 2:
        x = 3;
        for (int i = 4; i < 14; i++) {
            x = x + i;
        }
        cout << "suma liczb to: " << x << endl;
    break;

    case 3:
        for (int i = 1; i < 67; i++) {
            if ((i % 2 == 0) && (i % 7 == 0)) {
                cout << i<<endl;
            }
        }
    break;
    
    case 4:
        do {
            cout << "podaj liczbe: ";
            cin >> x;
            cout << endl << "twoja liczba to: " << x << endl;
        } while (x>=0);
        cout << endl << "KONIEC";
    break;
    
    case 5:
        cout << "podaj liczbe: ";
        cin >> x;
        cout << "dzielniki liczby " << x << " to:" << endl<<endl;
        for (int i = x; i > 0; i--) {
            if (x % i == 0) {
                
                cout << i << endl;
            }
        }
    break;
    }
}

