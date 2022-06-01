import random

number = 0
presents = 0
students = 0
quesitons = 0
option = ""
a = {0}
b = {0}
c = {0}
d = {0}
e = {0}
f = {0}

absents = {0}
allStudents = {0}

def generateRandomNumber(min, max):
    global allStudents, students
    randomNumber = random.randint(min, max)
    ##allStudents.add(randomNumber)
    if randomNumber not in allStudents:
        print(randomNumber)
        allStudents.add(randomNumber)
        allStudents.discard(0)
        return randomNumber
    else:
        if len(allStudents) == students:
            return "Nao ha numeros disponiveis"
        else:    
            return generateRandomNumber(1, students)

def removeStudent(number):
    global a, b, c, d, e, f, all
    if number in a:
        a.discard(number)
        allStudents.discard(number)
        print(a)
        return "Numero removido de A"
    elif number in b:
        b.discard(number)
        allStudents.discard(number)
        print(b)
        return "Numero removido de B"
    elif number in c:
        c.discard(number)
        allStudents.discard(number)
        print(c)
        return "Numero removido de C"
    elif number in d:
        d.discard(number)
        allStudents.discard(number)
        print(d)
        
        return "Numero removido de D"
    elif number in e:
        e.discard(number)
        allStudents.discard(number)
        print(e)
        return "Numero removido de E"
    elif number in f:
        f.discard(number)
        allStudents.discard(number)
        print(f)
        return "Numero removido de F"
    elif number in absents:
        absents.discard(number)
        allStudents.discard(number)
        print(absents)
        return "Numero removido de Faltas"
    else:
        return "Numero nao encontrado"


def allocateNumbers(number):
    global a, b, c, d
    while len(a) < (presents//quesitons):
        if number not in a and number not in absents:
            a.add(number)
            print(a)
            a.discard(0)
            return "Numero adicionado em A"
        elif number in a :
            return "Numero ja adicionado em A"
        elif number in absents:
            return "Numero faltou"
    while len(b) < (presents//quesitons):
        if number not in b and number not in absents:
            b.add(number)
            print(b)
            b.discard(0)
            return "Numero adicionado em B"
        elif number in b :
            return "Numero ja adicionado em B"
        elif number in absents:
            return "Numero faltou"
    while len(c) < (presents//quesitons):
        if number not in c and number not in absents:
            c.add(number)
            print(c)
            c.discard(0)
            return "Numero adicionado em C"
        elif number in c :
            return "Numero ja adicionado em C"
        elif number in absents:
            return "Numero faltou"
    while len(d) < (presents//quesitons):
        if number not in d and number not in absents:
            d.add(number)
            print(d)
            d.discard(0)
            return "Numero adicionado em D"
        elif number in d :
            return "Numero ja adicionado em D"
        elif number in absents:
            return "Numero faltou"
    while len(e) < (presents//quesitons):
        if number not in e and number not in absents:
            e.add(number)
            print(e)
            e.discard(0)
            return "Numero adicionado em E"
        elif number in e :
            return "Numero ja adicionado em E"
        elif number in absents:
            return "Numero faltou"
    while len(f) < (presents//quesitons):
        if number not in f and number not in absents:
            f.add(number)
            print(f)
            f.discard(0)
            return "Numero adicionado em F"
        elif number in f :
            return "Numero ja adicionado em F"
        elif number in absents:
            return "Numero faltou"

print("Welcome to the student selector!")

print("How many students are in total?")
students = int(input())
print("How many are present?")
presents = int(input())
print("How many quesitons are there?")
quesitons = int(input())
print("Para remover um numro digite 'rm'")

while len(a)+len(b)+len(c)+len(d)+len(absents) < students:
    number = generateRandomNumber(1, students)
    print("The number is: " + str(number) + ".  Type N if the number is absent or press B to print another number")
    option = input()
    if option == "b" or option == "B":
        allocateNumbers(number)
    elif option == "n" or option == "N":
        absents.add(number)
        absents.discard(0)
        print(absents)
    elif option == "rm" or option == "RM":
        print(("Which student would you like to remove? "))
        removeStudent(int(input()))
    
    print("The numbers in A are: " + str(a))
    print("The numbers in B are: " + str(b))
    print("The numbers in C are: " + str(c))
    print("The numbers in D are: " + str(d))
    print("The numbers in E are: " + str(e))
    print("The numbers in F are: " + str(f))
    print("The numbers that are absent are: " + str(absents))
    print("All the students " + str(sorted(allStudents)))