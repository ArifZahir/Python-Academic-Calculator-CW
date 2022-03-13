# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20200880         
  
# Date:  4/30/2021

#PART 2



print('''

This is a program to predict progression outcomes at the end of each academic year.''')#purpose of program highlighted at start

v_pass = 0#defining variables at start
v_defer = 0
v_fail = 0
total = 0
runLoop = True#condition for the loop to run


    


 

while runLoop is True :
         
    try :#in case if they enter something other than an integer
        
        v_pass = int(input('''

Please enter your credits at pass: '''))#multi line to make it easier to read
        if v_pass > 120 or v_pass < 0 :#checking if the user entered within the range
            print("Out of range")
            continue
        v_defer = int(input('''
        
Please enter your credits at defer: '''))
        if v_defer > 120 or v_defer < 0 :
            print("Out of range")
            continue
        v_fail = int(input('''

Please enter your credits at fail: '''))
        if v_fail > 120 or v_fail < 0 :
            print("Out of range")
            continue

            
    except ValueError :#if they entered integer then this should print and loop back to start
        print("Integer required")
        continue

    
    
    total = v_pass + v_defer + v_fail#checking total
    
    if total != 120 :
        print("Total incorrect")
        continue
    else :
        break


    

#taking in consideration pass marks and fail marks in accordance to table and printing relevant result
if v_fail >= 80 :
        print("Exclude")
elif v_pass <= 80 and v_fail < 80 :
        print("Do not progress - module retriever")
elif v_pass == 100 :
        print("Progress(module trailer)")
elif v_pass == 120 :
        print("Progress")



    


    



