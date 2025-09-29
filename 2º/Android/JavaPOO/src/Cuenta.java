//Creditos de actividad a
// https://discoduroderoer.es/ejercicios-propuestos-y-resueltos-programacion-orientado-a-objetos-java/
public class Cuenta {
    String titular;
    Double cantidad;

    public Cuenta(String titular){
        this.titular=titular;
        this.cantidad=0.0;
    }

    public Cuenta(String titular, Double cantidad){
        this.titular=titular;
        if(cantidad<0.0){
            this.cantidad=0.0;
        }else{
            this.cantidad=cantidad;
        }
    }

    public void setTitular(String titular){
        this.titular=titular;
    }

    public String getTitular(){
        return this.titular;
    }

    public void setCantidad(Double cantidad){
        this.cantidad=cantidad;
    }

    public Double getCantidad(){
        return this.cantidad;
    }

    public void ingresar(Double cantidad){
        if (cantidad>0.0){
            this.cantidad+=cantidad;
            System.out.println("Transaccion exitosa");
        }else{
            System.out.println("No se puede agregar saldo negativo");
        }
    }

    public void retirar(Double cantidad) {
        /*
        * Si la cantidad a retirar es negativa la paso a positiva
        * y luego se procede con normalidad
        * */
        if (cantidad<0.0){cantidad=cantidad*-1;}
        if (this.cantidad-cantidad<0.0) {
            System.out.println("No hay suficiente saldo");
        } else {
            this.cantidad-=cantidad;
            System.out.println("Transaccion exitosa");
        }
    }

    public String toString(){
        return "Titular: "+this.titular+"\nSaldo: "+this.cantidad;
    }

    public static void main(String[] args) { //Main pillado de la pagina og

        Cuenta cuenta_1 = new Cuenta("DiscoDurodeRoer");
        Cuenta cuenta_2 = new Cuenta("Fernando", 300.0);

        //Ingresa dinero en las cuentas
        cuenta_1.ingresar(300.0);
        cuenta_2.ingresar(400.0);

        //Retiramos dinero en las cuentas
        cuenta_1.retirar(500.0);
        cuenta_2.retirar(100.0);

        //Muestro la informacion de las cuentas
        System.out.println(cuenta_1); // 0 euros
        System.out.println(cuenta_2); // 600 euros

    }
}