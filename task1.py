#question 1(assigned by Golden): 
#Create a console application that collects age from a user. Display the age collected.
#To take this some steps further, please consider the following:

# 1) Ensure the user inputs a number (You should be able to convert the input to an integer)
# 2) Keep asking for the user's input till the user inputs a number
# 3) The asking should be done 10 times after which an error should be thrown telling the user that a number is what is expected
# 4) if the user is not up to 10 years, display: you're too young.
# 5) If the user is between 10 and 15 years, display: you're a still young
# 6) If the user is between 16 and 20 years, display: you're mid-aged
# 7) If the user is more than 20 but not up to 30 years, display: you're fairly young
# 8) If the user's age is not covered here, display: we couldn't find a good match for you

# Goodluck guys😊

def trying(collectage):
    class User:
        def __init__(self, age):
            self.age = age
            
        def collect_age(self):
            '''This function is to notify user that I want to collect their age'''

            print('Hi there, I\'m trying to collect ages with this app...do you mind a minute of your time?!\n')
    #Number of times a user can input a wrong value
            trials = 10
    #for loop to indicate the number of times the question can be asked if user gives the wrong input
            while True:
                if trials == 0:
                    break
                try: 
                    userage = int(input('Enter your age: ')) 
                except ValueError:
    #deducting the user trial from the total trials available for user input
                    trials-= 1
                    print(f'you have {trials} trials left, you can only enter a number,try again!\n') 
                else:
                    if userage < 10:
                        print("You're too young!\n")  
                    elif userage >= 10 and userage <=15:
                        print("You're still young!\n")
                    elif userage >=16 and userage <=20:
                        print("You're mid-aged!\n")
                    elif userage >= 21 and userage <30:
                        print("You're fairly young!\n")
                    else:
                        print("We couldn't find a good match for you!\n")
                    break
    userage = User('getage')
    userage.collect_age()

