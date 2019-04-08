def main():

    #get frequency of knowns
    known_dic = {}
    knownTxt = open("knowntext.txt", "r")
    while True:
        c = knownTxt.read(1).lower()

        if not c: break

        if  not c.isalpha() and c != " ":
            continue

        if c not in known_dic:
            known_dic[c] = 1
        else:
            known_dic[c] +=1
    
    #get freq of unknowns
    u_dic = {}
    uTxt = open("ciphertext.txt", "r")
    while True:
        c = uTxt.read(1).lower()
        if not c: break

        if not c.isalpha() and c != " ":
            continue

        if c not in u_dic:
            u_dic[c] = 1
        else:
            u_dic[c] +=1

    kList = []
    uList = []

    for key,val in known_dic.items():
        kList.append((key, val))

    for key,val in u_dic.items():
        uList.append((key, val))

    #sort both by 2nd thing in tuple
    s_kList = sorted(kList, key = lambda x : x[1])
    s_uList = sorted(uList, key = lambda x : x[1])

    #do a dic mapping unknown: known
    freqDic = {}
    for i in range(len(s_uList)):
        freqDic[s_uList[i][0]] = s_kList[i][0]
    
    uTxt = open("ciphertext.txt", "r")
    while True:
        c = uTxt.read(1).lower()
        if not c: break

        if not c.isalpha() and c != " ":
            print(c, end="")
        else:
            print(freqDic[c], end="")


if __name__ == "__main__":
    main()
