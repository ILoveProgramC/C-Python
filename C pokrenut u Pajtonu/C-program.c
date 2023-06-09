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

    return 0;
}
