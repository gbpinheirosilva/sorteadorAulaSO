#include<stdio.h>
#include<stdlib.h>
#include<string.h>

main(int argv, char *argc[])
{   
    

}

int randomNumber(int min, int max)
{
    int random = rand() % (max - min + 1) + min;
    return random;
}


