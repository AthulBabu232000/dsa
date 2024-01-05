import java.util.*;
public class Subsequence{

    public static ArrayList<Integer> generateSequence(int idx, ArrayList<Integer>temp, int[] arr){
      int size=arr.length;
      if(idx==size){
        // System.out.println(temp.toString());
        return temp;
      }
      temp.add(arr[idx]);
      
      generateSequence(idx+1,temp,arr);
      temp.remove(temp.size()-1); 
      generateSequence(idx+1,temp,arr);
    return null;

    }
    public static void main(String[] args){
        int arr[] = {1, 2, 3, 4};
        generateSequence(0, new ArrayList<Integer>(), arr);

    }

}