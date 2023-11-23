// package data-structure-and-algorithm;

public class DoublyLinkedList {
    private Node head;
    private Node tail;
    private int length;

    class Node{
        int value;
        Node next;
        Node prev;
        Node(int value){
            this.value=value;
        }
    }

    public int getHeadValue(){
        if(head != null){
            return this.head.value;
        }
        return -1;
    }
      public int getTailValue(){
        if(head != null){
            return this.tail.value;
        }
        return -1;
    }
      public int getLength(){
        return this.length;
    }

    public DoublyLinkedList(int value){

        Node newNode=new Node(value);
        this.head=newNode;
        this.tail=newNode;
        this.length=1;

        
    }
  public void printList(){
        Node temp=head;
        while(temp!=null){
            System.out.println(temp.value);
            temp=temp.next;
        }
    }
    public void append(int value){
        Node newNode=new Node(value);
        if(length==0){
            this.head=newNode;
            this.tail=newNode;
        }
        tail.next=newNode;
        newNode.prev=tail;
        this.tail=newNode;
        this.length++;
    }

    public Node removeLast(){
        if(length==0){
            return null;
        }
        Node temp=tail;
        if(length==1){
            this.head=null;
            this.tail=null;
        }else{
            this.tail=this.tail.prev;
            this.tail.next=null;
            temp.prev=null;
        }
        this.length--;
        return temp;
    }

    public void prepend(int value){
        Node newNode=new Node(value);
        if(length==0){
            this.head=newNode;
            this.tail=newNode;
        }else{
            newNode.next=head;
            this.head.prev=newNode;
            this.head=newNode;
        }
        this.length++;

    }

    public Node removeFirst(){
        if(length==0){
            return null;
        }
        Node temp=head;
        if(length==1){
            this.head=null;
            this.tail=null;
        }else{
            this.head=this.head.next;
            this.head.prev=null;
            temp.next=null;
        }
        this.length--;
        return temp;
    }

    public Node get(int index){
        if(index<0 || index>=length){
            return null;
        }
        Node temp=head;
       if(index<length/2){
         for(int i=0;i<index;i++){
            temp=temp.next;
        }
       }else{
        temp=tail;
        for(int i=length-1;i>index;i--){
            temp=temp.prev;
        }
       }
        return temp;
    }

    public boolean set(int index, int value){
        Node temp=get(index);
        if(temp!=null){
             temp.value=value;
             return true;
        }
        return false;
    }

    public boolean insert(int index, int value){

        if(index<0 || index > length)return false;
        if(index==0){
            prepend(value);
            return true;
        }
        if(index==length){
            append(value);
            return true;
        }

        Node before=get(index - 1);
        Node after=before.next;
        Node newNode=new Node(value);
        before.next=newNode;
        after.prev=newNode;
        newNode.prev=before;
        newNode.next=after;
        length++;
        return true;
    }

    public Node remove(int index){
        if(index<0 || index>=length) return null;
        if(index==0){
            return removeFirst();
        }
        if(index == length-1){
            return removeLast();
        }
        Node temp=get(index);
        temp.prev.next=temp.next;
        temp.next.prev=temp.prev;
        temp.prev=null;
        temp.next=null;

        length--;
        return temp;

    }

  
}
