//#include <ctime>
#include <chrono>
#include <iostream>
using namespace std;
using namespace std::chrono;

//#define N 100000000

int main() {
int N = 1.0e6;
double a[N], b[N], c[N];

typedef duration<float> fsec;

auto t0 = high_resolution_clock::now(); 
for (int i=0; i<N; i++) {
	a[i] = rand();
	b[i] = rand();
	c[i] = a[i]*b[i];
	
}
auto t1 = high_resolution_clock::now(); 

fsec fs = t1 - t0;

std::cout << fs.count() << "s\n";

//auto duration = duration_cast<miliseconds>(stop - start)/1e3; 

//cout << duration.count() << endl; 
//cout << stop << endl;

//return 0;
}



