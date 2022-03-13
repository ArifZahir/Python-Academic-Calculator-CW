# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20200880         
  
# Date:  4/30/2021

#PART 1


print('''

This is a program to predict progression outcomes at the end of each academic year.''')#purpose of program highlighted at start



v_pass = int(input('''

Please enter your credits at pass: '''))#multi line to make it easier to read

v_defer = int(input('''

Please enter your credits at defer: '''))

v_fail = int(input('''

Please enter your credits at fail: '''))
            

#taking in consideration pass marks and fail marks in accordance to table
if v_fail >= 80 :
    print("Exclude")
elif v_pass <= 80 and v_fail < 80 :
    print("Do not progress(module retriever)")
elif v_pass == 100 :
    print("Progress(module trailer)")
elif v_pass == 120 :
    print("Progress")
    



