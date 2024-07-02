//Warning: Don't change this line.  If you change the package name, your code will not compile, and you will get zero points.
package comp2011.a1;

import java.util.Arrays;

/*
 * @author Yixin Cao (September 11, 2023)
 *
 * Simulating a doubly linked list with an array.
 * 
 */
public class DListOnArray_22100143d_HeYiyang { // Please change!
    private int[] arr;
    private static final int SIZE = 126; // it needs to be a multiplier of 3.

    /**
     * VERY IMPORTANT.
     * 
     * I've discussed this question with the following students:
     *     1. 
     *     2. 
     *     3. 
     *     ... 
     * 
     * I've sought help from the following Internet resources and books:
     *     1. LAB5 PPT and Code
     *     2. 
     *     3. 
     *     ... 
     */ 
    public DListOnArray_22100143d_HeYiyang() {
        arr = new int[SIZE];
        arr[0] = 0;
        arr[1] = 0;
        arr[2] = 0;
        for (int i = 4; i < SIZE - 2; i += 3) {
            arr[i] = i + 1;//next 5, 8, 11, 14, 17...
            arr[i - 1] = 0;//data at initialisation is 0
            arr[i - 2] = i - 5;//previse except arr[2] 0, 2, 5, 8, 11, 14...
        }
        arr[2] = 0;//arr[2] is 0 because no previse for first
        arr[SIZE - 1] = 2;
        arr[SIZE - 2] = 0;//arr[size - 2] is 0 because no next for last
    }

    /**
     * VERY IMPORTANT.
     * 
     * I've discussed this question with the following students:
     *     1. 
     *     2. 
     *     3. 
     *     ... 
     * 
     * I've sought help from the following Internet resources and books:
     *     1. LAB5 PPT and Code
     *     2. 
     *     3. 
     *     ... 
     */ 
    public boolean isEmpty() {
        return arr[0] == 0;
    }

    /**
     * VERY IMPORTANT.
     * 
     * I've discussed this question with the following students:
     *     1. 
     *     2. 
     *     3. 
     *     ... 
     * 
     * I've sought help from the following Internet resources and books:
     *     1. LAB5 PPT and Code
     *     2. 
     *     3. 
     *     ... 
     */ 
    public boolean isFull() {
        return arr[SIZE - 1] == 0;
    }

    public void err() {
        System.out.println("Oops...");
    }

    /**
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
     */ 
    public void insertFirst(int x) {
        if (isFull()) { err(); return; }
        int i = arr[SIZE - 1];// i = 2 when is empty and i = arr[size -1] shows the next position
        if (isEmpty()) {arr[1] = i;}//if empty arr[1] show the head
        else{arr[arr[0]] = i;}
        arr[SIZE - 1] = arr[i + 2];//arr[size -1] become next node position and store
        arr[i + 2] = arr[0];//node(next)
        arr[i + 1] = x;//node(data)
        arr[i] = 0;//node(previse)
        arr[0] = i;//arr[0] shows the head
        arr[arr[SIZE - 1]] = 0;// next node previse become 0 for further operation
    }

    /**
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
     */ 
    public void insertLast(int x) {
        if (isFull()) { err(); return; }
        if (isEmpty()) {insertFirst(x);}
        int i = arr[SIZE - 1];// i = 2 when is empty and i = arr[size -1] shows the next position
        arr[SIZE - 1] = arr[i + 2];//arr[size -1] become next node position and store
        arr[arr[1] + 2] = i;// tail before this action need to point it next to the new node
        arr[i] = arr[1];//node(previse)
        arr[i + 1] = x;//node(data)
        arr[i + 2] = 0;//node(next)
        arr[1] = i;//shows the tail
        arr[arr[SIZE - 1]] = 0;// next node previse become 0 for further operation
    }

    /**
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
     */ 
    public int deleteFirst() {
        if (isEmpty()) {err(); return -1;}
        int i = arr[0]; //current head
        arr[arr[SIZE - 1]] = arr[0];//change next position to the current head
        arr[0] = arr[i + 2];//new head is the current head(previse)
        arr[arr[i + 2]] = 0;//the new head has no previse so 0
        arr[i + 2] = arr[SIZE - 1];
        arr[SIZE - 1] = i;//let the next position become head that we delete
        arr[i] = 0;//current previse is 0
        return arr[i + 1];
    }

    /**
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
     */ 
    public int deleteLast() {
        if (isEmpty()) {err(); return -1;}
        if (arr[0] == arr[1]) { //only one node
            return deleteFirst();
        }
        int i = arr[1];//current tail
        arr[arr[SIZE - 1]] = arr[1];//change previse position to the current tail
        arr[1] = arr[i];//new tail is the current tail next
        arr[arr[i] + 2] = 0; // the new tail has no next so 0
        arr[i + 2] = arr[SIZE - 1];
        arr[SIZE - 1] = i;//let next position become tail that we delete
        arr[i] = 0; //current previse is 0
        return arr[i + 1];
    }

    /*
     * Optional, this runs in O(n) time.
    public void reverse() {
        
    }
     */    

    /*
     * Optional, but you cannot test without it.
    // this method should print out the numbers in the list in order
    // for example, after the demonstration, it should be "75, 85, 38, 49"
    */

    public String toString() {
        if(isEmpty()) {
            return "The list is empty.";
        }
        StringBuilder sb = new StringBuilder();
        int i = arr[0] + 1;
        sb.append(arr[i]);
        while(arr[i + 1] != 0){
            i++;
            i = arr[i];
            i++;
            sb.append(", ").append(arr[i]);
        }
        return sb.toString();
    }
        /*
         * The following is prepared for your reference.
         * You may freely revise it to test your code.
         */
    public static void main(String[] args) {
        DListOnArray_22100143d_HeYiyang list = new DListOnArray_22100143d_HeYiyang();
        // You may use the following line to print out data (the array),
        // so you can monitor what happens with your operations.
        //System.out.println(Arrays.toString(list.data));
        System.out.println(list);
        list.insertFirst(75);
        list.insertFirst(99);
        list.insertLast(85);
        list.insertLast(38);
        System.out.println(list);
        list.deleteFirst();
        System.out.println(list);
        list.insertLast(49);
        System.out.println(list);
    }
}
