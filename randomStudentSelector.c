#include<stdio.h>
#include<stdlib.h>
#include<string.h>

main(int argv, char *argc[])
{   
    int students, questions, number;
    char option;
    printf("Enter the number of students: ");
    scanf("%d", &students);
    printf("Enter number of questions:\n");
    scanf("%d", &questions);
    
    int set1 = [];
    int set2 = [];
    int set3 = [];
    int set4 = [];
    int absents = [];
    
    printf("Pressione N para gerar um novo numero"    )
    scanf("%c", &option);
    int number = randomNumber(0, students);

}

int randomNumber(int min, int max)
{
    int random = rand() % (max - min + 1) + min;
    return random;
}


