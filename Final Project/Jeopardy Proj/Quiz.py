import sqlite3

print ("Welcome to Jeopardy\n")
name = input("Please enter you name : ")

if name != "":
    print ("Hello", name, "..!!")
    print("Please read the instructions carefully before starting the game..!!")
    print("")
    print("1. Pick a category and a clue value for the question.")
    print("2. If you provide the correct response to a clue, you earn the value of the clue.")
    print("3. Incase of incorrect response, half of the value of the clue will be subtracted from the score.")
    print("4. Game will be over in case of (a). Three incorrect answers or (b) You win the maximum amout (15000$)")
    print("")
    res = input("Are you ready to play ? yes or no : ")

if res == "yes":
    
    # Connect to the Jeopardy databse
    connection = sqlite3.connect('jeopardy.db')
    cursor = connection.cursor()
    
    # Select the five random categories from catagory table
    cursor.execute("SELECT id, name FROM category ORDER BY RANDOM() LIMIT 5")
    results1 = cursor.fetchall()
    
    # initiating the variables
    i = 0
    j = "A"
    cat1 = 0
    cat2 = 0
    cat3 = 0
    cat4 = 0
    cat5 = 0
    score = 0
    counter = 0
    res_list = []
    
    # Keep playing untill you fail 3 times
    while (counter < 3):
    
        # Display the Catgories   
        i = 0
        j = "A"
        print ("Choose the Category:\n")
        for category in results1:
            i = i + 1
            cat1 = category[0]
            if i == 2:
                j = "B"
                cat2 = category[0]
            if i == 3:
                j = "C"
                cat3 = category[0]
            if i == 4:
                j = "D"
                cat4 = category[0]
            if i == 5:
                j = "E"
                cat5 = category[0]
            print ("Category", category[1])
            print ( j + "1", "-", '200$'  )
            print (j + "2", "-", '400$' )
            print (j + "3", "-", '600$'  )
            print (j + "4", "-", '800$' )
            print (j + "5",  "-", '1000$' )
            print ("\n")
        
        # Option for the user to pick a category
        response = input("You Chose : ")
        # Ask the user to pick new category, in case the catagory is being repeated
        if response in res_list:
            response = input("Please choose the new category : ")
        # Save the selected category to a list
        res_list.append(response)    
        lists = list(response)
        
        # Check whether the user is picking the valid category 
        if lists[0] in "ABCDE":
            pass
        else:
            response = input("Please choose the valid category : ")
            # Ask the user to pick new category, in case the catagory is being repeated
            if response in res_list:
                response = input("Please choose the new category : ")
            # Save the selected category to a list
            res_list.append(response)
            lists = list(response)
        
        if lists[0] == "A":
            val = (cat1,)
        if lists[0] == "B":
            val = (cat2,)
        if lists[0] == "C":
            val = (cat3,)
        if lists[0] == "D":
            val = (cat4,)
        if lists[0] == "E":
            val = (cat5,)  
        if lists[1] == "1":
            amt = 200
        if lists[1] == "2":
            amt = 400
        if lists[1] == "3":
            amt = 600
        if lists[1] == "4":
            amt = 800
        if lists[1] == "5":
            amt = 1000
    
        # Fetch the question as per the selected category
        answer = ""
        question = ""
        results = []
        cursor.execute("SELECT text, answer, value FROM clue WHERE category=?", val)
        results = cursor.fetchall()

        for values in results:
            if values[2] == amt:
                answer = values[1]
                question = values[0]
        
        # In case database has some discrepancy and particular record doesn't exist        
        if answer == "":
            results = []
            question = ""
            cursor.execute("SELECT text, answer, value FROM clue ORDER BY RANDOM() LIMIT 1")
            results = cursor.fetchone()
            answer = values[1]
            question = values[0]

        print(answer)        
        print ("Question for $", amt, ":", question)
                
        # Option for the user to input the answer
        response = input("Your Answer is : ")
        # If the given answer is correct
        if response == answer:
            score = score + amt
            print("")
            print("Correct Answer...!!")
            print("Your Current Score is: ", score)
        # If the given answer is incorrect
        else:
            score = score - (amt / 2)
            if score <= 0:
                score = 0
            print("")
            print("Incorrect Answer...!!")
            print("The correct answer is : ", answer)
            print("Your Current Score is: ", score)
            counter = counter + 1
        # break the while loop
        if score == 15000:
            break 
            
    # Game will be over if user gives 3 incorrect answers
    if counter == 3:
        print("Game over and your final score is : ", score)
    
    # Game will be over if user wins the max amount (15000)    
    if score == 15000:
        print("You won the game and your final score is : ", score)
        
    connection.close()