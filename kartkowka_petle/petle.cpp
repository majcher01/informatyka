
#include <iostream>

using namespace std;

int i, sw, x, y;
string p = "";

int main(){
	do {
		cout << "Wybierz zadanie (1-5) ";
		cin >> sw;

		switch (sw) {

		case 1:
			for (i = 1; i < 21; i++) {
				cout << i << endl;
			}
			break;
		case 2:
			for (i = 5; i < 16; i++) {
				x = x + i;
			}
			cout << x;
			break;
		case 3:
			for (i = 3; i < 30; i++) {
				if ((i % 2) != 0) {
					cout << i << endl;
				}
			}
			break;
		case 4:
			for (i = 1; i < 67; i++) {
				if ((i % 3 == 0) && (i % 7 == 0)) {
					cout << i << endl;
				}
			}
			break;
		case 5:
			cout << "wprowadz liczbe: ";
			cin >> x;
			y = 1;
			for (i = x; i > 0; i--) {
				y = y * i;
			}
			cout << y;
			break;
		default:
			cout << "wybrano nieprawidlowe zadanie";
			break;



		}
		cout <<endl<< "powtorzyc ? (t/n) ";
		cin >> p;
	} while (p != "n");
	return 0;
}


