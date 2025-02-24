#include<iostream>

using namespace std;
template<typename T>
class Queue {
	T* data;
	int front, rear, capacity;
	void resize();

public:
	Queue() : data(new T[capacity]), front(0), rear(0), capacity(10) {};
	~Queue();
	void enqueue(T element);
	T dequeue();
	T getFront() const;
	int getSize() const;
};

template<typename T>
void Queue<T>::resize() {
	T* newData = new T[capacity * 2];
	for (int i = 0; i < capacity; i++) {
		newData[i] = data[i];
	}
	delete[] data;
	data = newData;
	capacity *= 2;
}

template<typename T>
Queue<T>::~Queue(){
	delete[] data;
}

template<typename T>
void Queue<T>::enqueue(T element) {
	if (rear == capacity) {
		resize();
	}
	data[rear++] = element;
}

template<typename T>
T Queue<T>::dequeue() {
	if (front == rear) {
		cout << "Queue is empty!" << endl;
		return - 1;
	}
		return data[front++];
}

template<typename T>
T Queue<T>::getFront() const {
	if (front == rear) {
		cout << "Queue is empty!" << endl;
		return - 1;
	}
	return data[front];
}

template<typename T>
int Queue<T>::getSize() const {
	return rear - front;
}

int main() {
	Queue<int> q;
	q.enqueue(6);
	q.enqueue(8);
	cout << q.getFront() << endl;
	q.enqueue(10);
	cout << q.getFront() << endl;
	q.dequeue();
	cout << q.getFront() << endl;
	cout << q.getSize() << endl;
	return 0;
}