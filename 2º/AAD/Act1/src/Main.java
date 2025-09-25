import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Random;
//Escribir 100 palabras, luego encontrar la mas buscada
//Encontrar y controlar las posibles excepciones: FileNotFound, IOException, Permisos

public class Main {
    public static void main(String[] args) {
        File file = new File("a.txt");
        try {
            file.createNewFile();
            FileWriter fileWriter = new FileWriter(file.getName());
            FileReader fileReader = new FileReader(file.getName());
            String[] words = new String[5];
            words[0]="Hola";
            words[1]="Chao";
            words[2]="Miau";
            words[3]="Guau";
            words[4]="Dunno";
            Random r = new Random();
            for(int i=0;i<100;i++){
                fileWriter.write(words[r.nextInt(5-0)]);
            }
            HashMap<String, Integer> wordCount = new HashMap<>();
            for(String word:fileReader.readAllLines()){
                if(wordCount.containsKey(word)){
                    wordCount.put(word, wordCount.get(word)+1);
                } else {
                    wordCount.put(word,1);
                }
            }

            System.out.println(wordCount);

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
