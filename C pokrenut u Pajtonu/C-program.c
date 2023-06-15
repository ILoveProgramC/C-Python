#include <stdio.h>

int kvadrat(int i) {
	return i * i;
}

void ispis(){
    printf("Ovo je program napisan u C-u\n");

}

void unos(){
    int n;
    printf("Unesite n: ");
    scanf("%d", &n);
    for (int i =0;i<n;i++){
        printf("C program u pajtonu\n");
    }

}

int main(){
    FILE *izlaz = fopen("C-dokument.txt", "w");
    if (izlaz==NULL){
        printf("Greska pri kreiranju datoteke!\n");
        return 1;
    }
    fprintf(izlaz,"Ovo je tekst pisan u C-u ali je napravljen pokretanjem C programa preko Pythona :)\n");
    printf("Main funkcija u C programu, kreirana je teksutalna datoteka /C-dokument.txt/\n");
    fclose(izlaz);

    return 0;
}
