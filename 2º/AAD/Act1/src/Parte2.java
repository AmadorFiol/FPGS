import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Parte2 {
    public static void main(String[] args) {
        //File creation
        File file = new File("reservas_maestro.txt");

        try {
            file.createNewFile();

            //Master file writing
            FileWriter fileWriter = new FileWriter(file.getName());
            fileWriter.write("12A, Juan Perez, Economy, Madrid\n" +
                    "14B, Maria Lopez, Business, Paris\n" +
                    "21C, Carlos Garcia, Economy, Madrid\n" +
                    "05D, Ana Sanchez, Business, Londres\n" +
                    "19E, Luis Gomez, Economy, Paris\n" +
                    "08F, Sofia Vargas, Economy, Londres");
            fileWriter.close();

            //Master file reading & child file/s writing
            Scanner fileReader = new Scanner(file);
            Integer i;
            List<String> destinies = new ArrayList<>();
            while (fileReader.hasNextLine()){ //Loop to read the file's lines
                String line=fileReader.nextLine();
                String destiny = "";
                /*
                * In this for loop we search for the reservation destiny
                * by going from the end of the line and adding each char
                * to a string var until we find a space meaning
                * we already read all the destiny's name.
                * Then we'll check if that destiny was already encountered,
                * if it was nothing happens aside from breaking the for
                * but if not we add it to a List and also break the for
                * */
                for (i=line.length()-1; i>0; i--) {
                    if(line.charAt(i)==' '){
                        if (!destinies.contains(destiny)){
                            destinies.add(destiny);
                        }
                        break;
                    }

                    destiny = line.charAt(i)+destiny;
                }
                /*
                * We try to create a new file of the line's destiny, if it was already
                * one we simply add the line to the file, if not a file is created for
                * that destiny, and we show a message stating it, and we add the line
                * to the file
                * */
                file=new File("reservas_"+destiny+".txt");
                if(file.createNewFile()){
                    System.out.println("Se ha creado el archivo " + file.getName());
                }
                fileWriter = new FileWriter(file.getName(), true);
                fileWriter.write(line+"\n");
                fileWriter.close();
            }

            //For loop to show the information of each destniy
            for(String destiny:destinies){
                i=0;
                System.out.println("\nReservas para "+destiny);
                fileReader = new Scanner(new File("reservas_"+destiny+".txt"));
                while (fileReader.hasNextLine()){
                    i++;
                    System.out.println(fileReader.nextLine());
                }
                System.out.println("Nº reservas: "+i.toString());
            }
            fileReader.close();

        } catch (FileNotFoundException e) {
            System.out.println("El archivo no a sido encontrado");;
        } catch (IOException e){
            System.out.println("No se tiene los permisos requeridos\npara realizar alguna accion");
        }
    }
}
