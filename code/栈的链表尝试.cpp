#include<iostream>
#include<stdexcept>
#include<stack>

using namespace std;

template<typename T>
class Stack {
private:
	struct Node {
		T data;
		Node* next;
		Node(T d) : data(d), next(NULL) {}
	};
	Node* head;
	int size;

public:
	Stack() : head(NULL), size(0) {};
	~Stack();
	void push(T element);
	T pop();
	T top() const;
	int getSize() const;
};

template<typename T>
Stack<T>::~Stack() {
	while (head) {
		Node* temp = head;
		head = head->next;
		delete temp; 
	}
}

template<typename T>
void Stack<T>::push(T element) {
	Node* newNode = new Node(element);
	newNode->next = head;
	head = newNode;
	++size;
}

template<typename T>
T Stack<T>::pop() {
	if (head == NULL) {
		throw std::out_of_range("Stack<>::pop(): empty stack");
	}
	Node* temp = head;
	T data = head->data;
	head = head->next;
	delete temp;
	--size;
	return data;
}

template<typename T>
T Stack<T>::top() const {
	if (head == NULL) {
		throw std::out_of_range("Stack<>::top(): empty stack");
	}
	return head->data;
}

template<typename T>
int Stack<T>::getSize() const {
	return size;
}

int main() {
	Stack<int> s;
	s.push(1);
	s.push(4);
	s.push(8);
	s.push(9);
	cout << s.top() << endl;
	s.push(19);
	cout << s.top() << endl;
	s.pop();
	s.pop();
	cout << s.top() << endl;
}
