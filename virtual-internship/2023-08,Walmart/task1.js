import java.util.Arrays;
import java.util.NoSuchElementException;

public class PowerHeap {
    private double x;
    private int size;
    private int[] heap;

    // Constructor
    public PowerHeap(double x, int capacity) {
        // initialize size of heap
        this.size = 0;
        heap = new int[capacity + 1];
        this.x = x;
        Arrays.fill(heap, -1);
    }

    // find the parent of the node-index
    private int parent(int i) {
        if (i==0)
            throw new IllegalArgumentException("this node doesn't have parent");
        return (int) ((i - 1) / Math.pow(2, x));
    }

    // check if the heap is full
    public boolean isFull() {
        return size == heap.length;
    }

    // method of inserting a node
    public void insert(int value) {
        if (isFull()) {
            throw new NoSuchElementException("Heap is full");
        } else {
            heap[size++] = value;
            heapcheck(size - 1);
        }
    }

    // check and fix if the heap mantains its feature
    private void heapcheck(int i) {
        int tmp = heap[i];
        while (i > 0 && tmp > heap[parent(i)]) {
            heap[i] = heap[parent(i)];
            i = parent(i);// move the index to it's parent
        }
        heap[i] = tmp;
    }

    // pop out the max node
    public int popMax() {
        // 
        int maxNode = heap[0];
        heap[0] = heap[size - 1];
        heap[size - 1] = null;
        size--;

        // check the heap from the start
        int i = 0;
        while (i < size - 1) {
            heapcheck(i);
            i++;
        }

        return maxNode;
    }
}