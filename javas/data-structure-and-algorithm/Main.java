// package data-structure-and-algorithm;

public class Main {
    
    public static void main(String[] args) {

        DoublyLinkedList ddl=new DoublyLinkedList(1);
        ddl.append(2);
        ddl.append(3);
        ddl.append(4);
        ddl.printList();
        ddl.removeLast();
        ddl.printList();
     
    }
}
