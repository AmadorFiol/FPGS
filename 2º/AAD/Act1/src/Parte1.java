import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Parte1 {
    public static void main(String[] args) {
        //File creation
        File file = new File("reservas.txt");

        try {
            file.createNewFile();

            //File writting
            FileWriter fileWriter = new FileWriter(file.getName());
            fileWriter.write("12A, Juan Perez, Economy\n14B, Maria Lopez, Business\n21C, Carlos Garcia, Economy");
            fileWriter.close();

            //File reading
            Scanner fileReader = new Scanner(file);
            Integer i=0;
            while (fileReader.hasNextLine()){
                String line=fileReader.nextLine();
                if(line.contains("Business")){
                    i++;
                }
                System.out.println(line);
            }
            System.out.println("Hay "+i+" pasajero/s en Business");

        } catch (FileNotFoundException e) {
            System.out.println("El archivo no a sido encontrado");;
        } catch (IOException e){
            System.out.println("No se tiene los permisos requeridos\npara realizar alguna accion");
        }
    }
}
