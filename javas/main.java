import java.util.*;
 class Main{

    public static void main(String[] args){
//    Set<String> set1 = new HashSet<>(Arrays.asList("apple", "banana", "cherry", "date"));
// Set<String> set2 = new HashSet<>(Arrays.asList("banana", "date", "grape", "kiwi"));
String[] fruits={"banana","orange","pomegranate"};
List<String> fruitList=Arrays.asList(fruits);
System.out.println(fruitList.toString());
fruitList.set(1,"grapes");// you can't add here as it cannot be modified

System.out.println(fruitList.toString());
System.out.println(Arrays.toString(fruits));

    }
}