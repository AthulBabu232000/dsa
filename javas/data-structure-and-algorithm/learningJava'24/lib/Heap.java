// import java.util.*;

// public class Heap {
//     private List<Integer> heap;

//     public Heap(List<Integer> listBeforeHeapify) {
//         this.heap = listBeforeHeapify;
//     }

//     public List<Integer> getHeap() {
//         return this.heap;
//     }

//     private int leftChild(int i) {
//         return (2 * i) + 1;
//     }

//     private int rightChild(int i) {
//         return (2 * i) + 2;
//     }

//     private int parent(int i) {
//         return (i - 1) / 2;
//     }

//     private void swap(int indx1, int indx2) {
//         int temp = this.heap.get(indx1);
//         this.heap.set(indx1, this.heap.get(indx2));
//         this.heap.set(indx2, temp);
//     }
    

//     public List<Integer> displayHeap() {
//         return this.heap;
//     }

//     public void insert(int value) {
//         this.heap.add(value);
//         int current = this.heap.size() - 1;
//         // consider this as minheap
//         while (current > 0 && this.heap.get(current) < this.heap.get(parent(current))) {
//             swap(current, parent(current));
//             current = parent(current);
//         }
//     }

//     public void sinkDown(int index) {
//         int maxIndex = index;
//         int leftChildIndex = this.leftChild(index);
//         int rightChildIndex = this.rightChild(index);
//         // considering a maxheap
//         while (true) {
//             if (leftChildIndex < heap.size()&& this.heap.get(leftChildIndex) > this.heap.get(maxIndex)) {
//                 maxIndex = leftChildIndex;
//                 System.out.println("inside the leftchild");
//             }
//             if (rightChildIndex < heap.size() && this.heap.get(rightChildIndex) > this.heap.get(maxIndex)) {
//                 maxIndex = rightChildIndex;
//                 System.out.println("inside the rightchild");

//             }
//             if (maxIndex != index) {
//                 System.out.println("inside the maxindex!=index");

//                 this.swap(index,maxIndex);
//                 index = maxIndex;
//             } else {
//                 return;
//             }
//         }
//     }

//     public Integer remove(int index) {
//         if (this.heap.isEmpty())
//             return null;

//         if (this.heap.size() == 1)
//             return heap.remove(0);

//         Integer maxIndex = this.heap.get(0);
//         this.heap.set(0, this.heap.remove(this.heap.size() - 1));
//         this.sinkDown(0);
//         return maxIndex;

//     }

//     public List<Integer> heapify() {
//         int length = this.heap.size();
//         int nodeBeforeLeaf = (length / 2) - 1;
//         System.out.println(nodeBeforeLeaf);
//         for (int i = nodeBeforeLeaf; i >= 0; i--) {
//             this.sinkDown(i);
//         }
//         return this.heap;
//     }

// }
import java.util.ArrayList;
import java.util.List;

public class Heap {
    private List<Integer> heap;

   public Heap(List<Integer> listBeforeHeapify) {
        this.heap = listBeforeHeapify;
    }

    public List<Integer> getHeap() {
        return new ArrayList<>(heap);
    }

    private int leftChild(int index) {
        return 2 * index + 1;
    }

    private int rightChild(int index) {
        return 2 * index + 2;
    }

    private int parent(int index) {
        return (index - 1) / 2;
    }

    private void swap(int index1, int index2) {
        int temp = heap.get(index1);
        heap.set(index1, heap.get(index2));
        heap.set(index2, temp);
    }

    public void insert(int value) {
        heap.add(value);
        int current = heap.size() - 1;

        while (current > 0 && heap.get(current) > heap.get(parent(current))) {
            swap(current, parent(current));
            current = parent(current);
        }
    }

    private void sinkDown(int index) {
        int maxIndex = index;
        while (true) {
            int leftIndex = leftChild(index);
            int rightIndex = rightChild(index);

            if (leftIndex < heap.size() && heap.get(leftIndex) > heap.get(maxIndex)) {
                maxIndex = leftIndex;
            }

            if (rightIndex < heap.size() && heap.get(rightIndex) > heap.get(maxIndex)) {
                maxIndex = rightIndex;
            }

            if (maxIndex != index) {
                swap(index, maxIndex);
                index = maxIndex;
            } else {
                return;
            }
        }
    }

    public Integer remove() {
        if (heap.size() == 0) {
            return null;
        }

        if (heap.size() == 1) {
            return heap.remove(0);
        }

        int maxValue = heap.get(0);
        heap.set(0, heap.remove(heap.size() - 1));
        sinkDown(0);

        return maxValue;
    }
    
    public List<Integer> heapify() {
        int length = this.heap.size();
        int nodeBeforeLeaf = (length / 2) - 1;
        System.out.println(nodeBeforeLeaf);
        for (int i = nodeBeforeLeaf; i >= 0; i--) {
            this.sinkDown(i);
        }
        return this.heap;
    }

}