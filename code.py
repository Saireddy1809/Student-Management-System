print("STUDENT MANAGEMENT SYSTEM") 
 
while True: 
    print("\n1. Add Students") 
    print("2. Display Students") 
    print("3. Search Students") 
    print("4. Count Students") 
    print("5. Exit") 
 
    option = int(input("Enter your option: ")) 
 
    if option == 1: 
       with open('students.txt','a') as f: 
            roll_no = input('enter roll no: ') 
            name = input('enter name: ') 
            fee = input('enter fee: ') 
            f.write(roll_no + "," + name + "," + fee + "\n") 
            print("Students added successfully") 
 
    elif option == 2: 
       with open('students.txt','r') as f: 
           print(f.read()) 
 
    elif option == 3: 
       search = input ('enter name to search: ') 
       with open('students.txt','r') as f: 
        n = False 
        for i in f: 
            if search in i: 
                print('student found') 
                print(i) 
                n = True          
        if n == False:             
            print('student not found')         
 
    elif option == 4: 
        count = 0 
        with open('students.txt','r') as f: 
            for i in f: 
                count += 1 

        print('total students:', count)  
 
    elif option == 5: 
        print("Thank you!") 
        break 
 
    else: 
        print("Invalid Option")