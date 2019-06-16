def pr1(*number):
    numbers=sorted(number)
    found = 1
    divizor = numbers[0]
    while divizor > 1:
        found = 1
        for i in numbers:
            if i%divizor != 0:
                found = 0
                break
        if found == 1:
            return divizor
        divizor -= 1
    return divizor


# print(pr1(4,16,8,56))

def pr2(string):
    count=0
    for i in string:
        if i in 'AEIOUaeiou':
            count+=1
    return count

# print(pr2("PNEUMONOULTRAMICROSCOPICSILICOVOLCANICONIOZA"))


def pr3(string):
    print(string)
    string = string.replace(',', ' ')
    string = string.replace(';', ' ')
    string = string.replace('?', ' ')
    string = string.replace('!', ' ')
    string = string.replace('.', ' ')
    words = string.strip().split(' ')
    return words

# print(pr3("Sunt,Claudiu.Burlacu!Emil si;am restanta;la!Python?"))

def pr4(string, substring):
    return string.count(substring)

# print(pr4("Am avut niste amuzamente amunitie am uzat", "am"))

def pr5(string):
    if "\a" in string:
        return False
    elif "\b" in string:
        return False
    elif "\f" in string:
        return False
    elif "\v" in string:
        return False
    elif "\r" in string:
        return False
    elif "\t" in string:
        return False
    elif "\n" in string:
        return False
    else:
        return True

# print(pr5("Hello World!"))

def pr6(string):
    string=string[0].lower() + string[1:]
    a = len(string)
    i=0
    while(i<a):
        if string[i].isupper():
            string = string[:i] + "_" + string[i:]
            i += 1
            a += 1
        i += 1
    return string.lower()


# print(pr6("AmLuatExamenul"))


def pr7(char_len, *words):
    if len(words) == 1: return True
    a = words[0][-1*char_len:]
    for i in range (1, len(words)):
        if char_len > len(words[i]):
            return False
        if words[i].startswith(a):
            a = words[i][-1*char_len:]
        else:
            return False
    return True


# print(pr7(2,"Claudiu", "iubire", "aegenerat", "atacat", "atentionat"))