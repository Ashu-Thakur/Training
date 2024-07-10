import Module.cutomemodule as cutomemodule


main = cutomemodule.Library(PythonBeginner = 2,PythonIntermediate = 1, pythonAdvance = 8, HeadfirstJava = 4, MachineLearning = 5, DsawithCpp = 6,LearningC = 4)

while True:
    main.info()
    menu = """
            1.See Books Availability
            2.for Borrow books
            3.create account
            4.see Your Acount View
            5.for Return books
            6.Exit
            """
    print(menu)
    choice = int(input("Enter Your Choice :"))
    if choice == 1:
        main.show()
    
    elif choice == 2:
        main.borrow_book()

    elif choice == 3:
        main.add_user()

    elif choice == 4:
        main.user_view()

    elif choice == 5:
        username = input("Enter Your Username")
        book_name = input("Book Name:")
        main.return_book()
    
    elif choice == 6:
        print("Thanks for visiting...")
        break
    else:
        print("Invalid Choice...")
