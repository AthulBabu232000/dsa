public class DoublyLinkedList {
    private Node head;
    private Node tail;
    private int length;

    class Node{
        int value;
        Node next;
        Node prev;
        public Node(int value){
            this.value=value;
        }
    }

    public DoublyLinkedList(int value){

        Node newNode = new Node(value);
        this.head=newNode;
        this.tail=newNode;
        this.length=1;
    }
}
