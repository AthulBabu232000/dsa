 import java.util.*;
 public class Heap {
    private List<Integer> heap;

    public Heap(){
        this.heap=new ArrayList();
    }

    public List<Integer> getHeap(){
        return this.heap;
    }

    private int leftChild(int i){
        return 2*i+1;
    }

    private int rightChild(int i){
        return 2*i+2;
    }

    private int parent(int i){
        return (i-1)/2;
    }

    private void swap(int indx1, int indx2){
        int temp=this.heap.get(indx1);
        this.heap.set(indx1,indx2);
        this.heap.set(indx2,temp);
    }

    public void insert(int value){
        this.heap.add(value);
        int current=this.heap.size()-1;
        // consider this as minheap
        while(current>0 && this.heap.get(current)<this.heap.get(parent(current))){
            swap(current,parent(current));
            current=parent(current);
        }
    }

    public void sinkDown(int index){
        int maxIndex=index;
        int leftChildIndex=this.leftChild(index);
        int rightChildIndex=this.rightChild(index);
// considering a maxheap
       while(true){
         if(leftChildIndex<heap.size()-1 && this.heap.get(leftChildIndex)>this.heap.get(maxIndex)){
            maxIndex=leftChildIndex;
        }
        if(rightChildIndex<heap.size()-1 && this.heap.get(rightChildIndex)>this.heap.get(maxIndex)){
            maxIndex=rightChildIndex;
        }
        if(maxIndex!=index){
            this.swap(maxIndex,index);
            index=maxIndex;
        }else{
            return;
        }
       }
    }
    public Integer remove(int index){
        if(this.heap.isEmpty())return null;

        if(this.heap.size()==1)return heap.remove(0);

        Integer maxIndex=this.heap.get(0);
        this.heap.set(0,this.heap.remove(this.heap.size()-1));
        this.sinkDown(0);
        return maxIndex;


    }


}
