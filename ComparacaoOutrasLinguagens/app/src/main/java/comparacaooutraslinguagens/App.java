package comparacaooutraslinguagens;

import java.util.Scanner;

public class App {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número: ");
        int numero = scanner.nextInt();

        // if
        if(numero > 8){
            System.out.println("O valor é maior que oito");
        } else {
            System.out.println("Menor que 8 ou igual");
        }

        // while
        int cont = 1;
        while(cont < 11){
            cont++;
            System.out.println(cont);
        }

        // for
        int teste;
        for(teste = 0; teste < cont; teste += 2){
            System.out.println(teste);
        }

        // vetor
        int vet[] = new int[4];
        int tamanho;
        for(tamanho = 0; tamanho < vet.length; tamanho++){
            System.out.print("Digite um valor para vet[" + tamanho + "]: ");
            vet[tamanho] = scanner.nextInt();
        }

        System.out.println("Valores do vetor:");
        for(tamanho = 0; tamanho < vet.length; tamanho++){
            System.out.println(vet[tamanho]);
        }

        scanner.close();
    }
}
