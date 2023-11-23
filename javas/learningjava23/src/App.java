package learningjava23.src;
import java.util.Vector;

interface Area{
    final static float pi=3.14F;
    float compute(float x, float y);
}

class Rectangle implements Area{
    public float compute(float x, float y){
        return x*y;
    }
}

class Circle implements Area{
    public float compute(float x,float y){
        return pi*x*x;
    }
}

public class App {

    public static void main(String[] args) throws Exception {
      
        Rectangle rect=new Rectangle();
        System.out.println("Area of rectangle is "+rect.compute(5,6));
        Circle circle = new Circle();
        System.out.println("Area of the circle is "+circle.compute(5,0));
        
    }
}
