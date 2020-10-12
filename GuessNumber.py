num=22
NoOfGuess=9
while NoOfGuess>0:
    val=int(input("Enter a no\n"))
    if val>22:
        print("Reduce it")
        NoOfGuess = NoOfGuess - 1
        print("No Of Guess left",NoOfGuess)
    elif val<22:
        print("Increase it")
        NoOfGuess = NoOfGuess - 1
        print("No of Guess left",NoOfGuess)
    elif val == 22:
        print("Correct ans")
        print("No of Guess you took",9-NoOfGuess)
        break
    else:
        print("Gae Over")
        break
