#include<iostream>
#include<stack>
using namespace std;

int main() {
	stack<int> intStk;
	intStk.push(1);
	intStk.push(2);
	intStk.push(3);
	intStk.push(4);
	while (!intStk.empty()) {
		cout << intStk.top() << ' ';
		intStk.pop();
	}

	return 0;
}
//empty()
//pop()
//push(v)
//top()