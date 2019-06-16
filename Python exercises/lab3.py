dict1 = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b
}



def pr1(a,b):
    return (set().union(a,b), set(a) & set(b), set(a) - set(b),set(b) - set(a))


# print(pr1([1,2,3,4],[3,4,5,6]))

def pr2(string):
    dict = {}
    for i in string:
        if i not in dict:
            dict.update({i:string.count(i)})
    return dict


# print(pr2("Ana are mere."))

def pr4(tag, content, **elems):
    s = ""
    s += "<" + tag + " "
    for elem, value in elems.items():
        s += elem + "=" + "\"" + value + "\"" + " "
    s = s.rstrip(' ')
    s += ">" + content + "</" + tag + ">"
    return s


# print(pr4("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))

def pr5(rules, dictionary):
    if len(rules) != len(dictionary.keys()):
        return False
    for rule in rules:
        if rule[0] not in dictionary:
            return False
        else:
            if not dictionary.get(rule[0]).startswith(rule[1]):
                return False
            if not dictionary.get(rule[0]).endswith(rule[3]):
                return False
            if rule[2] not in dictionary.get(rule[0]):
                return False
    return True

# a = {"key2": "starting the engine in the middle of the winter", "key1": "come inside, it's too cold outside"}
# print(pr5([("key1", "", "inside", ""), ("key2", "start", "middle", "winter")], a))


def pr6(operator, a, b):
    if operator in dict1:
        print(dict1[operator](int(a),int(b)))
    else:
        print("Unrecognized operation")

# pr6("+",2,3)