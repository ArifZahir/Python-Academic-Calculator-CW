# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20200880         
  
# Date:  4/30/2021

#PART 3



print('''

This is a program to predict progression outcomes at the end of each academic year.''')#purpose of program highlighted at start

v_pass = 0#defining variables at start
v_defer = 0
v_fail = 0
total = 0
runLoop = True#condition for the loop to run
excludeCount = 0
retrieverCount = 0
trailerCount = 0
progressCount = 0
outcomeCount = 0
 

while runLoop is True :
         
    try :#in case if they enter something other than an integer
        
        v_pass = int(input('''

Please enter your credits at pass: '''))#multi line to make it easier to read
        if v_pass > 120 or v_pass < 0 :#checking if the user entered within the range
            print("Out of range.")
            continue
        v_defer = int(input('''
        
Please enter your credits at defer: '''))
        if v_defer > 120 or v_defer < 0 :
            print("Out of range.")
            continue
        v_fail = int(input('''

Please enter your credits at fail: '''))
        if v_fail > 120 or v_fail < 0 :
            print("Out of range.")
            continue

            
    except ValueError :
        print("Integer required.")
        continue

    
    
    total = v_pass + v_defer + v_fail#checking total
    
    if total != 120 :
        print("Total incorrect.")
        continue
    #taking in consideration pass marks and fail marks in accordance to table and printing relevant result
    if v_fail >= 80 :
        print("Exclude")
        excludeCount += 1
        outcomeCount += 1
    elif v_pass <= 80 and v_fail < 80 :
        print("Do not progress - module retriever")
        retrieverCount += 1
        outcomeCount += 1
    elif v_pass == 100 :
        print("Progress(module trailer)")
        trailerCount += 1
        outcomeCount += 1
    elif v_pass == 120 :
        print("Progress")
        progressCount += 1
        outcomeCount += 1

    print('''
Would you like to enter another set of data?''')
    answer = str(input("Enter 'y' for yes or 'q' to quit and view results: "))
    if answer == "y" :
        continue
    elif answer == "q" :
        break
    
        

#histogram
print("Progress", progressCount, ": ", "*" * progressCount)
print("Trailer", trailerCount, ": ", "*" * trailerCount)
print("Retriever", retrieverCount, ": ", "*" * retrieverCount)
print("Excluded", excludeCount, ": ", "*" * excludeCount)
print("")
if outcomeCount != 1 :#printing outcome singular or plural based on number of outcomes
    print(outcomeCount," outcomes in total.")
else :
    print(outcomeCount," outcome in total.")
    



