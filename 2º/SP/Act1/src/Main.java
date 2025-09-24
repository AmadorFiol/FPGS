import java.lang.Integer;
import java.lang.String;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Contador hilo = new Contador();
        hilo.start();
        System.out.println("Inicio hilo principal");
        Contador[] hilos = new Contador[10];
        for(int i = 0; i < 10; i++){
            hilos[i] = new Contador();
            hilos[i].start();
            hilos[i].join();
        }
        System.out.println("Fin hilo principal");
        System.out.println(hilo.getNum());
    }

}
