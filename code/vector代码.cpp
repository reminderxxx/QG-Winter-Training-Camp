#include<iostream>
#include<vector>
using namespace std;	

int main()
{
	vector<int> ret = { 1, 2, 3, 4, 5 };
	for (int i = 0; i < ret.size(); i++) {
		cout << ret[i] << ' ' ;
	}
	cout << endl;	
	cout << ret.size() << endl;
	ret.push_back(1014); //插入到顺序表尾部
	cout << ret.size() << endl;
	cout << ret[5] << endl;	
}