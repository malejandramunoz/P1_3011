##!/usr/bin/python
# Filename: munozmaria_sec086_P1.py
# NAME: Maria Alejandra Muñoz Valenzuela
# STUDENT ID: 802-18-8690
# SECTION: 086

#This function validates if a file is found for the entered name
def is_file(filename):
    try:
        foriginal = open(filename, 'r')
        return True
    except FileNotFoundError:
        return False

#this function simply finds everything and saves it in the new file.
def open_file(filename):
    fnew = open("employees_payment.txt", "w")  # the new file that will present in the end of the file
    try:
        foriginal = open(filename)
        for line in foriginal:
            if not line.startswith('time'):  # deletes anything that has anything.
                line = line.rstrip()
                firstFind = line.find(",")  # finds hours and rate
                hrsrt = line[firstFind + 1:]  # saves hours and rate
                secondFind = hrsrt.find(",")  # finds the division between the two numbers
                hrs = hrsrt[:secondFind]  # saves the hours
                rate = hrsrt[secondFind + 1:]  # saves the rate
                names = line[:firstFind]  # saves the names
                hrs = float(hrs)  # turns the hours into an integer
                rate = float(rate)  # turns the rate into an integer
                fnew.write(names + " $")  # starts writing the new file with the names and the pay to be given
                fnew.write(computepay(hrs, rate) + "\n")
        fnew.close()
        foriginal.close()
    except:
        return False


# This function prints the menu
def print_program_menu():
    print("\n")
    print("Welcome to payment calculator. Please, choose an option:")
    print("To make sure that you get the correct outcome every time, please enter the file you want accessed each time!")
    print("1. Employees payment")
    print("2. Employee name with maximum number of work hours")
    print("3. Employee name with minimum number of work hours")
    print("4. Employee name with maximum rate")
    print("5. Employee name with minimum rate")
    print("6. Exit")




# This function allows to verify the entered option
def identify_option(option):
    if option.isdigit():  # Verify if this is a number
        numeric_option = int(option)
        # check if in range
        if numeric_option >= 1 and numeric_option <= 6:
            return numeric_option
        else:
            return -1  # invalid option
    else:
        return -1  # invalid option

#This function calculates the hours and rate, returning the pay to be used in another function
def computepay(hrs, rate):
   if hrs > 40:
        if rate > 50:
            pay = (hrs * rate)
            return str(pay)
        else:
            pay = (40 * rate) + (hrs - 40) * (1.5 * rate)
            return str(pay)
   else:
       pay = (hrs * rate)
       return str(pay)

#This function processes all the options
def process_request(option):
    #variables to be used to find the employees with the biggest hours and rate, and the smallest hours and rate and if there's any second names with the same rate/hour
    hsmallest = None
    hlargest = None
    hlargestname = None
    hsmallestname = None
    rsmallest = None
    rlargest = None
    rlargestname = None
    rsmallestname = None
    secondrlargestname = None
    secondrsmallestname = None
    secondhlargestname = None
    secondhsmallestname = None
    if option == 1: #checks the option
        filename = input("Enter the name of the file to be processed: ") #asks the user por the file name that is to be processed
        if is_file(filename): #checks if it's true
            open_file(filename) #calls the other function so it can save the file
            print("A file employees_payment.txt containing the payment information has been created​. ") #tells the user that the file has been created
        else: #if it can't open the file
            print("Illegal file name. Input file was not found") #it tells the user that can't be done because the file doesn't exist
    elif option > 1: #if the option is more than 1, it checks who's smallest and how's bigger
        filename = input("Enter the name of the file to be processed: ")
        if is_file(filename):
            foriginal = open(filename)
            for line in foriginal:
                if not line.startswith('time'):  # deletes anything that has anything.
                    #file = line
                    firstFind = line.find(",")  # finds hours and rate
                    hrsrt = line[firstFind + 1:]  # saves hours and rate
                    secondFind = hrsrt.find(",")  # finds the division between the two numbers
                    hrs = hrsrt[:secondFind]  # saves the hours
                    rate = hrsrt[secondFind + 1:]  # saves the rate
                    names= line[:firstFind]  # saves the names
                    deciding_hrs = float(hrs) #turns this into integers
                    deciding_rate = float(rate)
                    # finds the smallest/biggest rate and associates the names
                    if rsmallest is None and rlargest is None: #checks if there is something inside the variables
                        if rlargestname is None and rsmallestname is None: #since there's nothing in the two upper variables, this is just to check
                            rsmallest = deciding_rate #saves the value
                            rlargest = deciding_rate #saves the value
                            rlargestname = names #saves the name associated
                            rsmallestname = names #saves the name associated
                    elif deciding_rate > rlargest: #checks if it's bigger than the value already stored
                        rlargest = deciding_rate #saves the value
                        rlargestname = names #saves the name associated to the value
                    elif deciding_rate < rsmallest: #checks if it's smaller than the value already stored
                        rsmallest = deciding_rate #saves the value
                        rsmallestname = names #saves the name associated
                    elif deciding_rate == rlargest: #if two employees have the same rate it saves it to a different variable
                        secondrlargestname = names #saves the value that has the same rate
                    elif deciding_rate == rsmallest: #if two employees have the same rate it saves it to a different variable
                        secondrsmallestname = names #saves the value that has the same rate
                    # finds the smallest/biggest hours and associates the names
                    if hsmallest is None and hlargest is None: #this checks if there's something inside the variable
                        if hsmallestname is None and hlargestname is None:
                            hsmallest = deciding_hrs #saves the value
                            hlargest = deciding_hrs #saves the value
                            hsmallestname = names #saves the name associated
                            hlargestname = names #saves the name associated
                    elif deciding_hrs > hlargest: #checks if the value is bigger
                        hlargest = deciding_hrs #saves value
                        hlargestname = names #saves the name associated
                    elif deciding_hrs < hsmallest: #checks if the value is smaller
                        hsmallest = deciding_hrs #saves the value
                        hsmallestname = names #saves the name associated to it
                    elif deciding_hrs == hlargest: #if two employees have the same hours it saves it to a different variable
                        secondhlargestname = names #saves the name with the same hours
                    elif deciding_hrs == hsmallest: #if two employees have the same hours it saves it to a different variable
                        secondhsmallestname = names #saves the name with the same hours
            foriginal.close()
        else:
            print("Illegal file name. Input file was not found")

    #this is where the optitons start
    if hsmallest and rsmallest is not None: #checks if there's nothing on two main variables so it prints the best thing
        if option == 2:
            #this checks the second name variable so it can print the correct thing.
            if secondhlargestname is None: #if the variable has nothing, it simply prints the employee with the bigger hours
                print("The employee with the most hours is", hlargestname, end="") #it's divided because there's two different variables to print
                print(" with", hlargest, end="")
                print(" hours")
            #also check the variable to decide what to print
            elif secondhlargestname is not None: #if it does have something, it prints the two names and the hours
                print("The employee with the most hours is", hlargestname, end="") #it's divided because there's two different variables to print
                print(" with", hlargest, end="")
                print(" hours")
                print("The employee", secondhlargestname, end = "")
                print(" has the same hours")
        elif option == 3:
            #this checks the second name variable so that it can print the correct thing
            if secondhsmallestname is None:
                print("The employee with the least hours is", hsmallestname, end="") #it's divided because there's two different variables to print
                print(" with", hsmallest, end="")
                print(" hours")
            #also checks the variable to decide what to print
            elif secondhsmallestname is not None:
                print("The employee with the least hours is", hsmallestname, end="")
                print(" with", hsmallest, end="")
                print(" hours")
                print("The employee", secondhsmallestname, end="")
                print(" has the same hours")
        elif option == 4:
            #this checks the second name variable so that it can print the correct thing
            if secondrlargestname is None:
                print("The employee with the highest rate is", rlargestname, end="")
                print(" with $" + str(rlargest))
            elif secondrlargestname is not None:
                print("The employee with the highest rate is", rlargestname, end="")
                print(" with $" + str(rlargest))
                print("The employee", secondrlargestname, end="")
                print(" has the same rate")
        elif option == 5:
            if secondrsmallestname is None:
                print("The employee with the lowest rate is", rsmallestname, end="")
                print(" with $" + str(rsmallest))
            elif secondrsmallestname is not None:
                print("The employee with the lowest rate is", rsmallestname, end="")
                print(" with $" + str(rsmallest))
                print("The employee", secondrsmallestname, end="")
                print(" has the same rate")


# This function invokes all the necessary functions
def main():
    done = False
    while not done:
        print_program_menu()
        user_option = input("Enter option: ")
        option_info = identify_option(user_option)
        if option_info != -1:
            #option was valid
            if option_info == 6:
                done = True
                print( "Thanks for using the payment calculation program")
            else:
                process_request(option_info)
        else:
            #option invalid
            print("Invalid Option\n")

#The code below makes Python start from the main function
#whenever our program is invoked as a "standalone program"
#(as opposed to being imported as a module).
if __name__ == "__main__":
    main()