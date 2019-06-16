def pr1():
    file = open("sample.txt", 'r')
    list = []
    for line in file:
        list.append(line.strip())
    for i in range (0, len(list)):
        for j in range (i, len(list)):
            try:
                list1 = list[i].split('-')
                list2 = list[j].split('-')
                if list1[1] >= list2[1]:
                    s = list[i]
                    list[i] = list[j]
                    list[j] = s
            except Exception as e:
                if '-' not in list[i]:
                    s = list[i]
                    h = i
                    i -= 1
                else:
                    s = list[j]
                    h = j
                    j -= 1
                print(s)
                count = 0
                s2 = ""
                for l in range (0,len(s)):
                    s2 += s[l]
                    count += 1
                    if count == 8 or count == 12 or count == 16 or count == 20:
                        s2 += '-'
                print(s2)
                list[h] = s2
    file.close()
    file2 = open("results.txt", 'w+')
    for i in list:
        file2.write(i + "\n")
    file2.close()


# pr1()


def pr2():
    file = open("sample.txt", 'r')
    list = []
    for line in file:
        list.append(line.strip())
    for i in range (0,len(list)):
        if '-' not in list[i]:
            list[i] = "|INVALID_UUID|"
    file.close()
    file2 = open("sample2.txt", 'w+')
    for i in list:
        file2.write(i + "\n")
    file2.close()


# pr2()


def pr3():
    a = input("Enter a number: ")
    check_number = False
    while not check_number:
        try:
            a = float(a)
            check_number = True
        except:
            print("This is not a number")
            a = input("Please enter a real number:")

    b = input("Enter another number: ")
    check_number = False
    while not check_number:
        try:
            b = float(b)
            check_number = True
        except:
            print("This is not a number")
            b = input("Please enter a real number:")

    print(a-b)
    print(a+b)
    print(a/b)
    print(a*b)


# pr3()