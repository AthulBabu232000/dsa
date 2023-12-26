public class LinkedList{
    Node head;
    Node tail;
    int length;
    class Node{
        int value;
        Node next;
        Node(int value){
            this.value=value;
        }
    }
    public LinkedList(int value){
        Node newNode=new Node(value);
        this.head=newNode;
        this.tail=newNode;
        this.length=1; 
    }

    public void append(int value){
        Node newNode=new Node(value);
        if(this.head==null){
            this.head=newNode;
            this.tail=newNode;
        }else{
            this.tail.next=newNode;
            this.tail=newNode;
        }
        this.length++;
    }

    public void prepend(int value){
        Node newNode=new Node(value);
        if(this.head==null){
            this.append(value);
        }else{
            newNode.next=this.head;
            this.head=newNode;

        }
        this.length++;
    }

    public Node removeLast(){
        if(this.head==null){
            return null;
        }
        Node temp=this.head;
        Node prev=this.head;

        while(temp.next!=null){
            prev=temp;
            temp=temp.next;
        }

        this.tail=prev;
        this.tail.next=null;
        this.length--;
        if(this.length==0){
            this.head=null;
        }

        return temp;


    }

    public Node removeFirst(){

        if(this.length==0){
            return null;
        }

        Node temp=this.head;
        this.head=this.head.next;
        temp.next=null;
        this.length--;
        if(this.length==0){
            this.tail=null;
        }

        return temp;


    }
}