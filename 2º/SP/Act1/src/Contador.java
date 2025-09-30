public class Contador extends Thread{
    private static int num=50;

    public static synchronized void decrement(){
        num--;
    }
    public static int getNum(){
        return num;
    }

    public void run(){
        decrement();
    }
}