// текст программы -> компиляция (препроцессинг(текст программы -> текст программы, расшифровываются комманды #)
// -> трансляция -> компановка) -> исполняемый файл

// ./task_1 exe abc 1

#include <stdio.h>
#include <stdlib.h>

void decrypt(char * word, int shift);
void encrypt(char * word, int shift);

int main(int argc,  char * argv[])
{
    if (argc != 3) {
        printf("uncorrect count args");
        return 1;
    }
    char * word = argv[1];
    int shift = atoi(argv[2]);
    decrypt(word, -shift);
    printf("encrypt = %s\n", word);
    decrypt(word, shift);
    printf("encrypt = %s", word);
    printf(-10 % 2);
    return 0;
}

void encrypt(char * word, int shift) {
    for (int i = 0; word[i] != '\0'; ++i) {
        char current_char  = word[i];
        // char + int = a(97) + 1 = 98(b)
        // z + 1 =>
        if (current_char >= 'a' && current_char <= 'z') {
            word[i] = (((current_char - 'a') + shift) % 26) + 'a';
        }
        if (current_char >= 'A' && current_char <= 'Z') {
            word[i] = (((current_char - 'A') + shift) % 26) + 'A';
        }
    }
}

void decrypt(char * word, int shift) {
    for (int i = 0; word[i] != '\0'; ++i) {
        char current_char  = word[i];
        // char + int = a(97) + 1 = 98(b)
        // z + 1 =>
        if (current_char >= 'a' && current_char <= 'z') {
            word[i] = ((((current_char - 'a') - shift) % 26) + 26) % 26 + 'a';
        }
        if (current_char >= 'A' && current_char <= 'Z') {
            word[i] = ((((current_char - 'A') - shift) % 26) + 26) % 26 + 'A';
        }
    }
}