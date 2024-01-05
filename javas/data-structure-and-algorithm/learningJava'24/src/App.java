import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {

        List<Integer> listBeforeHeapify=new ArrayList<Integer>();
        listBeforeHeapify.add(7);
        listBeforeHeapify.add(10);
        listBeforeHeapify.add(3);
        listBeforeHeapify.add(4);
        listBeforeHeapify.add(20);
        listBeforeHeapify.add(15);

        System.out.println(listBeforeHeapify.toString());
        Heap heap=new Heap(listBeforeHeapify);
        heap.insert(25);
        // System.out.println(heap.displayHeap().toString());
        List<Integer> resultHeap=heap.heapify();
        System.out.println(resultHeap.toString());

        
    
}
}
