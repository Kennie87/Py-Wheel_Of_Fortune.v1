'''
Name: Kenneth Johnson
Course: CIS 123
Assignment:  2.7 Performance Assessment

'''
import os
import csv
import random
user = []
tries = []  #import random to generate number, assigns the user and tries as arrays, imports operating system and csv to create game results file
results = []

path = "C:\\Users\\kenjoh6361\\Desktop\\CIS123"
fileName = "games.csv"                                      #sets path and filename to read and write file



def gameRound(randomNumber, name, user):
      attempts = 0            #initializes attempts to 0
      solved = False          #sets the games value to false so the game can begin
      while solved == False:  #while the game value remains false it will continue when it is changed to true a new game will be prompted
            guess=int(input("Please guess a number between 1 and 10.."))
            attempts = attempts + 1             #starts the count for attempts taken
            if guess == randomNumber:
                  print(f"Congratulations, {name}!!! You guessed the correct number in {attempts} tries.")
                  tries.append(attempts)
                  solved = True                 #when the user guess's correctly the value of the game changes to true and congratulates them
            else:
                  if guess > randomNumber:
                        print("You guessed too high...")
                  else:                         #if the user guesses too high the game will prompt a lower answer
                        print("You guessed too low...")
      scores(user, tries)                       #if the user guesses to low the game will prompt a high answer
      return name, user, tries                  #passes the needed values to the next function 
      
def greetUser():
      name=input("Please enter your name: ")    #greets the user and prompts for a name
      user.append(name)                         #appends the name given to the variable name
      randint(name, user)                       #starts the next function to generate the random number

      return name, user       

def randint(name, user):
      randomNumber = random.randint(1, 10)      #generates a random number between 1 and 10
      gameRound(randomNumber, name, user)       #starts the next function to enter a game round

      return randomNumber, user

def scores(user, tries):
      user = []                                 #takes in user and tries and stores the two list 
      tries = []



def getGamesList():                                   #this function reads information from game file
      myList = []                                     #defines stored data as an array myList
      os.chdir(path)                                  #changes directory to the path previously established
      if os.path.exists(fileName):                    #if the filename exist in the path this statement will open and read the file or create a new
            with open(fileName) as gameFile:
                  gameReader = csv.reader(gameFile)
                  myList = list(gameReader)           
                  print("Previous Game")              #Prints previous game on screen
                  for game in myList:                 
                        game[1] = int(game[1])        #Coverts list into integar
                        print(game)                   #Prints prior game results
                  print("*"*20)                       #Seprates content by printing a line of astriks
      return(myList)

            
def saveFile(gameList):                                           #this functon save the results as a viewable game file
      with open(fileName,'w',newline='') as gameFile:             
            gameWriter=csv.writer(gameFile)                       #opens a writing feature so the original file can be updated


            for game in gameList:                                 
                  gameWriter.writerow(game)                       #wries results for the game on it's own row
      return


# Main()
games = getGamesList()
var_continue = "Y"
while var_continue == "Y" or var_continue == "Yes" or var_continue == "Yeah":             #prompts user to deciede whether to continue by typing
      greetUser()                                                                         #"Y" "Yes" or "Yeah" and inputs the variable
      print("Should I start another game? (Y/Yes/Yeah to continue) ")
      var_continue = input()
print("Here is a list of the names and scores for each users that has played.")           #if the user types anything but an appropriate answer

for user,tries in sorted(zip(user, tries), key=lambda x: x[1], reverse=True):             #sorts the zip list for user's and trie's taken from most to least amount of attempts
      print(user, tries)                                                                  #prints out the sorted list
score = (user, tries)                                                                     #assigns user and tries to the variable tries
games.append(score)                                                                       #appends data to from varable score to games file and saves
saveFile(games)
