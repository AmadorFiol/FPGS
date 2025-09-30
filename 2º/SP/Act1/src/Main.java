import java.lang.String;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Contador[] hilos = new Contador[100];
        for(int i = 0; i < 100; i++){
            hilos[i] = new Contador();
        }
        for(Contador c:hilos){
            c.start();
        }
        System.out.println(Contador.getNum());
    }

}
