//Warning: Don't change this line.  If you change the package name, your code will not compile, and you will get zero points.
package comp2011.a2;

import java.util.ArrayList;
import java.util.List;

/**
 *
 *
 * My student ID is 22100143d, I'm implementing 3 -aray max heap.


* VERY IMPORTANT.
* 
* I've discussed this question with the following students:
*     1. 
*     2. 
*     3. 
*     ... 
* 
* I've sought help from the following Internet resources and books:
*     1. COMP2011 LEC10 page 39-41
*     2. 
*     3. 
*     ... 
*/ 
public class DaryHeap_22100143d_HeYiyang<T extends Comparable<T>> { // Please change!

    private List<T> heap; // store the key in an arraylist
    private int capacity ; //capacity
    public DaryHeap_22100143d_HeYiyang (int capacity) { //constructor of the heap
        if(capacity <= 0) throw new IllegalArgumentException("Capacity must be a positive integer.");
        this.capacity = capacity;
        this.heap = new ArrayList<>(capacity);//new an arraylist that size = capacity
    }
    public void insert(T x) {
        if (heap.size() >= capacity){
            return;
        }
        heap.add(x);
        up(heap.size() - 1);
    }

    // Running time: O( logn  ).
    public T removeRoot() {
        if (heap.isEmpty()) {
            throw new IllegalStateException("Heap is empty.");
        }
        T root = heap.get(0);
        if (heap.size() == 1) heap.clear(); //only one element
        if (heap.size() > 1){
            heap.set(0, heap.get(heap.size() - 1)); //change root to last in arraylist
            heap.remove(heap.size() - 1); //remove last
            down(0);
        }
        return root;
    }

    // Running time: O(logn ).
    private void up(int c) { //same as a regular binary heap sort
        if(c == 0){return;}
        int p = (c - 1) / 3;
        if (heap.get(c).compareTo(heap.get(p)) <= 0) return;
        swap(c,p);
        up(p);
    }

    // Running time: O( logn  ).
    private void down(int ind) {
        if(ind * 3 + 2 > heap.size()) return;
        int c = 3 * ind + 1;
        int check = c;
        if(c + 1 < heap.size() && heap.get(c).compareTo(heap.get(c + 1)) <= 0){ //compare the first child with second child in the right
            c++;
        }
        if(!(check == c) && c + 1 < heap.size() && heap.get(c).compareTo(heap.get(c + 1)) <= 0){ //compare the second child with the third child if second child is larger than first child
            c++;
        }
        if(check == c && c + 2 < heap.size() && heap.get(c).compareTo(heap.get(c + 2)) <= 0){ //compare the first child with the third child if first child is larger than the second child
            c = c + 2;
        }
        if(heap.get(ind).compareTo(heap.get(c)) >= 0) return; //compare parent and child
        swap(ind, c);
        down(c);
    }

    private void swap(int i, int j) { //swap two element in the heap
        T temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }

    private int returnsize(){
        return heap.size();
    } //return the heap size

    /**
     * Merge the given <code>heap</code> with <code>this</code>.
     * The result will be stored in <code>this</code>.
     *
     * VERY IMPORTANT.
     *
     * I've discussed this question with the following students:
     *     1.
     *     2.
     *     3.
     *     ...
     *
     * I've sought help from the following Internet resources and books:
     *     1.
     *     2.
     *     3.
     *     ...
     *
     * Running time: O(nlogn).
     */
    public void merge(DaryHeap_22100143d_HeYiyang<T> heap) {
        while (heap.returnsize() > 0) {
            T element = heap.removeRoot();
            insert(element);
        }
    }
    
    /*
     * Make sure you test your code thoroughly.
     * The more test cases, the better.
     */
    public static void main(String[] args) {
        DaryHeap_22100143d_HeYiyang<Integer> test1 = new DaryHeap_22100143d_HeYiyang(8);
        DaryHeap_22100143d_HeYiyang<Integer> test2 = new DaryHeap_22100143d_HeYiyang(8);
        test1.insert(5); // insert test1
        test1.insert(4);
        test1.insert(10);
        test1.insert(2);
        test1.insert(6);
        test1.insert(12);
        test1.insert(15);
        test1.insert(15);
        test2.insert(9); // insert test2
        test2.insert(4);
        test2.insert(2);
        test2.insert(8);
        test2.insert(9);
        test2.insert(3);
        System.out.println(test1.removeRoot()); // remove root of test1
        System.out.println(test1.removeRoot());
        System.out.println(test1.removeRoot());
        System.out.println(test1.removeRoot());
        System.out.println(test1.removeRoot());
        System.out.println(test1.removeRoot());
        System.out.println(test2.removeRoot()); // remove root of test2
        System.out.println(test2.removeRoot());
        System.out.println(test2.removeRoot());
        test1.merge(test2);// merge test1(4, 2) and test2(4, 3, 2)
        System.out.println(test1.removeRoot()); // remove root of test1 after merge test1 and test2
        System.out.println(test1.removeRoot());
        System.out.println(test1.removeRoot());
        System.out.println(test1.removeRoot());
        System.out.println(test1.removeRoot()); // all the element in test1 are removed
    }
}
     
