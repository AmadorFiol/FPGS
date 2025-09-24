
public class Contador extends Thread{
    private int num=0;

    public void increment(){
        this.num++;
    }

    public int getNum(){
        return this.num;
    }
    public void run(){
        System.out.println("Inicio del hilo "+this.getName()+" con id "+this.getId());
        increment();
    }

}