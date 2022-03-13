# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20200880         
  
# Date:  4/30/2021

#PART 5



progressCount = 0#assigning variables at start
trailerCount = 0
retrieverCount = 0
excludeCount = 0

dataList = [{"Pass": 120, "Defer": 0, "Fail": 0},#data list accoring to the question
    {"Pass": 100, "Defer": 20, "Fail": 0},
    {"Pass": 100, "Defer": 0, "Fail": 20},
    {"Pass": 80, "Defer": 20, "Fail": 20},
    {"Pass": 60, "Defer": 40, "Fail": 20},
    {"Pass": 40, "Defer": 40, "Fail": 40},
    {"Pass": 20, "Defer": 40, "Fail": 60},
    {"Pass": 20, "Defer": 20, "Fail": 80},
    {"Pass": 20, "Defer": 0, "Fail": 100},
    {"Pass": 0, "Defer": 0, "Fail": 120},]


for row in dataList :
    passMark = row.get("Pass")#taking the information from the list to use in the loop
    failMark = row.get("Fail")
    if (passMark == 120):
        print("Progress")
        progressCount += 1
    elif (passMark == 100):
        print("Progress (module trailer)")
        trailerCount += 1
    elif (passMark < 100 and failMark < 80):
        print("Do not progress (module retriever)")
        retrieverCount += 1
    else:
        print("Exclude")
        excludeCount += 1

print('''
Horizontal Histogram\n''')


print("Progress",progressCount,": ","*" * progressCount)
print("Progress (module trailer)",trailerCount,": ","*" * trailerCount)
print("Do not progress (module retriever)",retrieverCount,": ","*" * retrieverCount)
print("Exclude",excludeCount,": ","*" * excludeCount)
print("")
print(len(dataList),"Outcomes in total.")#by using len() function we will know the number of outcomes(as number of outcomes will always be equal to the number of rows in the data list
