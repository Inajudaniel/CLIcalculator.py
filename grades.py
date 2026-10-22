def get_grades():
    grade = int(input("Enter your score: "))

    if grade < 0 or grade > 100:
        print("invalid number") 
    if grade >= 70:
        print("A")
    elif grade >= 60:
        print("B")
    elif grade >= 50:
        print("C")
    elif grade <= 49:
        print("F")
    
    
   
 

get_grades()


