import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.util.*;

public class Parte3 {
    public static File file;
    public static FileWriter fileWriter;

    public static void main(String[] args) {
        //File creation
        file = new File("reservas_maestro_corrupto.txt");

        try {
            file.createNewFile();

            //Master file writing
            FileWriter fileWriter = new FileWriter(file.getName());
            fileWriter.write("12A, Juan Perez, Economy, Madrid\n" + //OK                        (numData=4)
                    "14B, Maria Lopez,, Paris\n" +                      //FlightClass null          (numData=1)
                    "21C, Carlos Garcia, Economy,\n" +                  //Destiny null              (numData=0)
                    "05D, Ana Sanchez, Business, Londres\n" +           //OK                        (numData=4)
                    ",Luis Gomez, Economy, Paris\n" +                   //SeatNum null              (numData=3)
                    "08F,, Economy, Londres\n"+                         //Name null                 (numData=2)
                    "08F, Pablito, Economy, Madrid, AlgoMas");          //More data than expected   (numData>4)
            fileWriter.close();

            //Master file reading & child file/s writing
            Scanner fileReader = new Scanner(file);
            Integer i;
            List<String> destinies = new ArrayList<>();

            while (fileReader.hasNextLine()){ //Loop to read the file's lines
                String line=fileReader.nextLine();

                String strData="";
                Integer numData=0;
                for (i=line.length()-1; i>=0; i--) {
                    if(line.charAt(i)==',' && !strData.isEmpty()){
                        numData++;
                        strData="";
                    } else if (line.charAt(i)==',' && strData.isEmpty()) {
                        break;
                    }else if(i==0){
                        numData++;
                    } else {
                        strData=line.charAt(i)+strData;
                    }
                }
                if(numData!=4){
                    ErrorFound(line, numData);
                } else {
                    destinies=NoErrorFound(line,destinies);
                }

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

        } catch (FileNotFoundException e) {
            System.out.println("El archivo no a sido encontrado");;
        } catch (IOException e){
            System.out.println("No se tiene los permisos requeridos\npara realizar alguna accion");
        }
    }

    public static List<String> NoErrorFound(String line, List<String> destinies) throws IOException {
        /*
         * In this for loop we search for the reservation destiny
         * by going from the end of the line and adding each char
         * to a string var until we find a space meaning
         * we already read all the destiny's name.
         * Then we'll check if that destiny was already encountered,
         * if it was nothing happens aside from breaking the for
         * but if not we add it to a List and also break the for
         * */
        String destiny = "";
        Integer i=0;

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
        return destinies;
    }

    public static void ErrorFound(String line, Integer errorCode) throws IOException {
        file = new File("registro_errores.log");
        if (file.createNewFile()) {
        }

        fileWriter = new FileWriter("registro_errores.log", true);

        String errorMessage;
        switch (errorCode) {
            case 0:
                errorMessage = "Destino nulo";
                break;
            case 1:
                errorMessage = "Clase vuelo nulo";
                break;
            case 2:
                errorMessage = "Nombre pasajero nulo";
                break;
            case 3:
                errorMessage = "Numero asiento nulo";
                break;
            default:
                errorMessage = "Hay mas informacion de la necesaria";
        }

        fileWriter.write("[" + LocalDate.now().toString() + "], [" + line + "], [" + errorMessage + "]\n");
        fileWriter.close();
    }
}
