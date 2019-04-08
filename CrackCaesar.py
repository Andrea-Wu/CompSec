def main():
    #read in all the dictionary stuff


    dic_txt = open("dictionary.txt", "r")
    
    dic  = {}
    for line in dic_txt:
        line  = line.strip()
        dic[line] = 0

    ayy = "a"
    print(chr(ord(ayy) + 2))
    
    ctrArr = []

    for i in range(26):

        word_in_dic_ctr = 0

        ciph_txt = open("ciphertext.txt", "r")
        for line in ciph_txt:
            for word in line.split():
                word = word.lower()
                decodedWord = ""
                for c in word:
                    if c.isalpha():
                        decodedWord += chr(((ord(c) + i - ord('a')) % 26) + ord('a'))
                    
                if decodedWord in dic:
                    word_in_dic_ctr+=1
            
        ctrArr.append(word_in_dic_ctr)



    ind_max = 0
    num_max = -1
    for i in range(len(ctrArr)):
        
        if ctrArr[i] > num_max:
            num_max = ctrArr[i]
            ind_max = i
   
    print(ind_max)
    ciph_txt = open("ciphertext.txt", "r")
    for line in ciph_txt:
        for word in line.split():
            word = word.lower()
            decodedWord = ""
            for c in word:
                if c.isalpha():
                    decodedWord += chr((ord(c) + ind_max - ord('a')) % 26 + ord('a'))
                else:
                    decodedWord += c
            
            print(decodedWord, end=" ")
        print("")

                    
                

if __name__ == "__main__":
    main()


