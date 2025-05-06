#include <iostream>

using namespace std;

// Heap class to handle max heap operations
class Heap {
    int *arr;
    int size;

public:
    Heap(int n) {
        size = n;
        arr = new int[n + 1];
        arr[0] = 0;  // Placeholder for heap property [cite: 1, 2, 3]
    }

    void createHeap(int input[], int n) {
        for (int i = 0; i < n; i++) {
            insert(input[i]);
        }
    }

    void insert(int value) {
        size++;
        int i = size;
        arr[i] = value;
        while (i > 1 && arr[i] > arr[i / 2]) {
            swap(arr[i], arr[i / 2]);
            i /= 2;
        }
    }

    void heapify(int i, int n) {
        int largest = i;
        int left = 2 * i;
        int right = 2 * i + 1;

        if (left <= n && arr[left] > arr[largest]) {
            largest = left;
        }

        if (right <= n && arr[right] > arr[largest]) {
            largest = right;
        }

        if (largest != i) {
            swap(arr[i], arr[largest]);
            heapify(largest, n);
        }
    }

    void heapSort() {
        for (int i = size / 2; i >= 1; i--) {
            heapify(i, size);
        }

        for (int i = size; i > 1; i--) {
            swap(arr[1], arr[i]);
            heapify(1, i - 1);
        }
    }

    void displaySorted() {
        cout << "\n# Marks in descending order: " << endl;
        for (int i = 1; i <= size; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
        cout << "# Highest score: " << arr[1] << " & Lowest score: " << arr[size] << endl;
    }
};

// Class for handling student marks
class Marks {
    int arr[50], n;

public:
    void input() {
        cout << "Enter number of students: ";
        cin >> n;
        for (int i = 0; i < n; i++) {
            cout << "Enter marks of student " << i + 1 << ".";
            cin >> arr[i];
        }
    }

    void processHeap() {
        Heap maxHeap(n);
        maxHeap.createHeap(arr, n);
        maxHeap.heapSort();
        maxHeap.displaySorted();
    }
};

int main() {
    Marks obj;
    obj.input();
    obj.processHeap();
    return 0;
}