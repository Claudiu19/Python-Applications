import sys
import os
from os.path import join as pjoin

def pr1(argv):
        a = int(argv[0])
        b = int(argv[1])
        return [a-b,a+b,a/b,a*b]


# numbers = sys.argv[1:]
# print(pr1(numbers))


def pr2(path):
    try:
        if os.path.isdir(path):
            print(os.listdir(path))
        else:
            if os.path.isfile(path):
                file = open(path, 'r')
                count = 1;
                byte = file.read(1)
                print(byte)
                while byte and count <=4096:
                    byte = file.read(1)
                    print(byte)
                    count += 1
            else:
                print("Not a valid path")
    except OSError:
        print("Not a valid path")

# pr2("E:\Facultate\Engleza\Games\The Elder Scrolls V Skyrim Legendary Edition")


def pr3(path):
    file = open(path,'w')
    for i in os.environ:
        file.write(i + "     " + os.environ[i] + "\n")
    file.close()

# pr3("abc")


def pr4(path):
    files = os.listdir(path)
    for i in files:
        abs_path = os.path.join(path,i)
        if os.path.isfile(abs_path):
            print(abs_path)
        if os.path.isdir(abs_path):
            pr4(abs_path)


# pr4("E:\Facultate\Python\Recap_test\\test")

def pr5(path,result):
    file = open(result, 'w')
    for root, dirs, files in os.walk(path):
        for fileName in files:
            abs_path = os.path.join(root, fileName)
            if os.path.isfile(abs_path):
                file.write(abs_path + "|FILE\n")
            else:
                file.write(abs_path + "|UNKNOWN\n")

        for dir in dirs:
            abs_path = os.path.join(root, dir)
            if os.path.isdir(abs_path):
                file.write(abs_path + "|FOLDER\n")
            else:
                file.write(abs_path + "|UNKNOWN\n")
    file.close()


# pr5("E:\Facultate\Engleza\Games\Yu-Gi-Oh! Legacy of the Duelist", "E:\Facultate\Python\Recap_test\\pr5_result.txt")


def pr6(file, path, buffer):
    name = os.path.basename(file)
    abs_path = pjoin(path, name)
    if not os.path.exists(path):
        os.makedirs(path)
    dest = open(abs_path, "at")
    src = open(file, 'r')
    content = src.read(buffer)
    while content:
        dest.write(content)
        content = src.read(buffer)
    print("Done")
    dest.close()
    src.close()


pr6("E:\Facultate\DAWNC Proiect\pacman.js", "E:\\", 1024)


def pr8(path,tree_depth,filesize,filecount,dircount):
    filename = "file"
    dirname = "dir"
    for i in range(0, filecount):
        abs_path = os.path.join(path, filename + str(i))
        file = open(abs_path, "w+")
        for j in range (0, filesize):
            file.write("a")
        file.close()
    if tree_depth > 1:
        for i in range (0, dircount):
            abs_path = os.path.join(path, dirname + str(i))
            os.makedirs(abs_path)
            pr8(abs_path, tree_depth-1, filesize, filecount,dircount)
    print("Done")

pr8("E:\Facultate\Python\lan5_test\\test", 2, 1024, 3, 3)
