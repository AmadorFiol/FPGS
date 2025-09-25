import javax.swing.*;
import java.lang.Integer;
import java.lang.String;

void main() {
    System.out.println("Act 1 Calculos basicos");

    Integer x = 5;
    Integer y = 2;

    Integer sum = x + y;
    Integer res = x - y;
    Integer mul = x * y;
    Integer div = x / y;
    Integer mod = x % y;

    System.out.println(
            "Los numeros son " + x + " y " + y +
            "\nEl resultado es de la suma es " + sum.toString() +
            "\nEl resultado de la resta es " + res.toString() +
            "\nEl resultado de la multiplicacion es " + mul.toString() +
            "\nEl resultado de la division es " + div.toString() +
            "\nEl resultado resto/modulo es " + mod.toString()
    );


    System.out.println("\n\nAct 2 Comparacion tamaño");

    if(x<y){
        System.out.println(x.toString()+" es menor que " + y.toString());
    } else if (x>y) {
        System.out.println(x.toString()+" es mayor que "+ y.toString());
    } else {
        System.out.println(x.toString() +" es igual que "+ y.toString());
    };


    System.out.println("\nAct 3 Mostrar un mensaje");

    String nombre = "Amador";
    System.out.println("Bienvenido a Java, "+nombre);


    System.out.println("\nAct 4 Primeros input");

    nombre = JOptionPane.showInputDialog("Introduce tu nombre");
    System.out.println("Bienvenido a Java, "+nombre);


    System.out.println("\nAct 5 Calculo area ciruclo");

    String input = JOptionPane.showInputDialog("Introduce el radio");
    double area = Math.PI*Math.pow(Double.parseDouble(input), 2);
    System.out.println("El area es "+area);


    System.out.println("\nAct 6 Par o impar");

    input = JOptionPane.showInputDialog("Escribe un numero");
    if(Integer.parseInt(input)/2==0){
        System.out.println("El numero "+input+" es par");
    }else {
        System.out.println("El numero "+input+" es impar");
    };


    System.out.println("\nAct 7 ASCII a caracter");

    input = JOptionPane.showInputDialog("Escribe un numero entre 1 y 255");
    System.out.println((char)Integer.parseInt(input));


    System.out.println("\nAct 8 Caracter a ASCII");

    input = JOptionPane.showInputDialog("Escribe un caracter");
    System.out.println((int)input.charAt(0));


    System.out.println("\nAct 9 Calcular IVA");

    Double IVA = 0.21;
    input = JOptionPane.showInputDialog("Escriba el precio de un producto");
    System.out.println("El precio con IVA es: " + (Double.parseDouble(input) + (Double.parseDouble(input)*IVA)));


    System.out.println("\nAct 10 Numeros 1 al 100 con while");

    x=1;
    while(x<=100){
        System.out.println(x);
        x++;
    }


    System.out.println("\nAct 11 Numeros 1 al 100 con for");

    for(Integer i = 1; i<=100; i++){
        System.out.println(i);
    }


    System.out.println("\nAct 12 Numeros 1 al 100 divisibles entre 2 y 3");

    for(Integer i = 1; i<=100; i++){
        if(i%2==0 || i%3==0){
            System.out.println(i);
        }
    }


    System.out.println("\nAct 13 Numero de ventas y sumatorio");

    Double db = 0.0;
    input = JOptionPane.showInputDialog("Cuantas ventas has tenido hoy?");
    for(Integer i=Integer.parseInt(input); i>0; i--){
        input=JOptionPane.showInputDialog("Que tanto ha sido la venta?");
        db = db + Double.parseDouble(input);
    }


    System.out.println("\nAct 14 ");
}