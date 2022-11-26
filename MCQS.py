
print("~~~~ The Project game ~~~~~~~")
while (True):
    print('''
    Press 1. For "Start"
    Press 2. For "Exit" \n ''')

    choice = int(input("Enter your choice: \n"))

    if choice == 1:

        print(''' 
        Instuction of this game:

        ~~~~*** Every participant/user will attempt '5' rounds 
            and in each round random  quiz question will appear and they have to answer***~~~~~ \n ''')
        quiz={0:"Q.Electrons move faster than the speed of light ?",1:"Q.All introverts are shy and socially anxious ?",
              2:"Q.Ethereum is the second-largest cryptocurrency after Bitcoin ?",3:"Q.A credit card and a debit card are the same ?",
              4:"Q.There are more ancient pyramids in Sudan than in Egypt ?"}
        list1 = [False, False, True, False, True]

        score = 0

        lossPoint = 0

        for i in range(0,5):


            print(" Guess what computer choice out of 'True / False'  ")
            print(quiz[i])
            userAns = int(input('''
                                Press 1. For True
                                Press 0. For False \n'''))
            if userAns == list1[i]:
                score += 1
                print("Congratulation you answer the question right")
            else:
                score -= 1
                print("Unfortunately you answer the question wrong")



        print("-------********---------- \n")

        print("Participant Details")
        print("Score:",score)

