import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Random;
import java.util.Scanner;
//Escribir 100 palabras, luego encontrar la mas buscada
//Encontrar y controlar las posibles excepciones: FileNotFound, IOException, Permisos

public class Main {
    public static void main(String[] args) {
        File file = new File("a.txt");
        try {
            file.createNewFile();
            FileWriter fileWriter = new FileWriter(file.getName());
            String[] words = new String[5];
            words[0]="Hola";
            words[1]="Chao";
            words[2]="Miau";
            words[3]="Guau";
            words[4]="Dunno";
            Random random = new Random();
            for(int i=0;i<100;i++){
                fileWriter.write(words[random.nextInt(0,4)]+"\n");
            }

            fileWriter.close();
            HashMap<String, Integer> wordCount = new HashMap<>();
            Scanner fileReader = new Scanner(file);
            while (fileReader.hasNextLine()){
                System.out.println(fileReader.nextLine());
                if(wordCount.containsKey(fileReader.nextLine())){
                    if (fileReader.nextLine()!=null){
                        wordCount.put(fileReader.nextLine(), wordCount.get(fileReader.nextLine())+1);
                    }
                } else {
                    wordCount.put(fileReader.nextLine(),1);
                }
            }

            System.out.println(wordCount);

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
