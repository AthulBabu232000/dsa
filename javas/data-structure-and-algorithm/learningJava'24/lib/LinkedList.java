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
    public Node get(int index){
        
        if(index<0 || index>=length)return null;
        
        Node temp=this.head;
        for(int i=0;i<index;i++){

            temp=temp.next;
        }

        return temp;
    }


    public boolean set(int index, int value){
        Node setNode=get(index);
        if(setNode==null)return false;
        setNode.value=value;
        return true;

    }

    public boolean insert(int index, int value){
        if(index==0){this.prepend(value);this.length++;return true;}
                if(index==this.length){this.append(value);this.length++;return true;}
        Node prev=this.get(index-1);
        if(prev==null)return false;
        Node next=prev.next;
        Node newNode=new Node(value);
        prev.next=newNode;
        newNode.next=next;
        this.length++;
        return true;
    }

    public Node remove(int index){
        if(index==0){this.length--;return this.removeFirst();}
        if(index==this.length-1){this.length--;return this.removeLast();}
        Node prev=this.get(index-1);
        if(prev==null)return null;
        Node removedNode=prev.next;
        prev.next=removedNode.next;
        removedNode.next=null;
        this.length--;
        return removedNode;
    }
}