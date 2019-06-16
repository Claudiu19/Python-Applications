def pr1(n):
    list=[0,1]
    for i in range (2, n):
        a = list[i-1]+list[i-2]
        list.append(a)
    return list

# list=pr1(100)
# print(list)
# print(len(list))

def pr2(list):
    result = []
    for i in list:
        if i == 2:
            result.append(i)
        else:
            prime = True
            for j in range(2,int(i/2)):
                if i%j==0:
                    prime = False
                    break
            if prime:
                result.append(i)

    return result

# print(pr2([2,3,56,39,21,13,2]))

def pr4(a, b):
    union = []
    dif1 = []
    dif2 = []
    inter = []
    for i in a:
        if i in b:
            inter.append(i)
        else:
            dif1.append(i)
        union.append(i)
    for i in b:
        if i not in a:
            dif2.append(i)
            union.append(i)
    return (inter,union,dif1,dif2)


# print(pr4([1,2,3,4],[3,4,5,6]))


def pr6(x, *liste):
    full_list=[]
    result = []
    for i in liste:
        full_list.extend(i)
    for i in full_list:
        if full_list.count(i) == x:
            if i not in result:
                result.append(i)
    print(result)


# pr6(2,[1,2,3,4],[5,6,7,8,9],[346,2356,32115,23,2,3,4])

def pr7(*chars, x=1,flag=True):
    result = ()
    for i in chars:
        result1=[]
        for j in i:
            if flag:
                if ord(j) % x == 0:
                    result1.append(j)
            else:
                if ord(j) % x !=0:
                    result1.append(j)
        result += (result1,)
    print(result)


# pr7("test", "hello", "lab002",x=2,flag=False)

def pr8(*lists):
    max = 0
    result = []
    for i in lists:
        if len(i)>max:
            max = len(i)
    for i in range(0, max):
        tuple = ()
        for j in lists:
            if i >= len(j):
                tuple += (None,)
            if i < len(j):
                tuple += (j[i],)
        result.append(tuple)
    print(result)


# pr8([1,2,3],[1,2,3,4,5],[1,2],[1,2,3,4],[5,6,7],[5,6,7,8,9])

def pr9(list):
    list.sort(key=lambda tup: tup[1][2])
    print(list)

# pr9([('abc', 'bcd'), ('abc', 'zza')] )

