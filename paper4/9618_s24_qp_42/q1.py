WordArray = []

#a #d
def ReadWords(filename):
    global num
    global WordArray
    file = open(filename, 'r')
    for line in file:
        if line.strip() != "":
            WordArray.append(line.strip())
        else:
            break

    num = len(WordArray) -1

    Play()
    
#c
def Play():
    global WordArray
    global num
    print(f"Main word: {WordArray[0]}\n{num} answers")
    count = 0

    while True:
        ans = str(input("Enter word: "))

        if ans == "no":
            perc = 100*count / num
            print(f"You got {perc:.2f}% of the answers!")
            print("Remaining answers:")
            for word in WordArray:
                if word != None and word != WordArray[0]:
                    print(word.strip())
            break
        
        if ans in WordArray:
            print("Correct")
            count += 1
            index = WordArray.index(ans)
            WordArray[index] = None
            

        else:
            print("Incorrect")

#main
#b
x = str(input("Please enter (easy), (medium), (hard): "))
file_name = "9618_s24_qp_42/" + x.capitalize() + ".txt"
ReadWords(file_name)
