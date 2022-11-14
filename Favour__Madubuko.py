def grid():
    first_line = "+----"
    second_line = (("|"  + (" " * 4)) * 2) + "|"
    the_line = (first_line * 2) + "+"
    for i in range(2):
        print(the_line)
        for i in range(4):
            print(second_line)
    print(the_line)
grid()
#for x in D:
#    print(x,D[x])
        
#word = input("Type in your desired word: \n")

#def length_of_word(word):
#    the_word = word.split()  #word = ['Hello','World']
#    length_of_last_word = len(the_word[-1]) #World
#    return length_of_last_word
#the_output = length_of_word(word)
#print(the_output)