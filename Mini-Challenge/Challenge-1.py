while True:
    dict_list = {}
    Stu_name = input("Please enter the student's name:")
    if not Stu_name.isalpha():
        print("Please enter a valid student's name.")
        continue
    else:
        while True:
            num_sub = input("Enter the number of subjects: ")
            if not num_sub.isnumeric():
                print("Please enter a valid number.")
                continue
            else:
                while True:
                    num_sub = int(num_sub)
                    for num in range(1,num_sub+1):
                        while True:
                            sub_name = input(f"Please enter the subject {num} name: ")
                            if not sub_name.isalpha():
                                print("Please enter a valid subject name.")
                                continue
                            else:
                                while True:
                                    sub_score = input(f"enter the subject {num} score: ")
                                    if not sub_score.isnumeric():
                                        print(f"Please enter a valid score for the subject {num}")
                                        continue
                                    else:
                                        sub_score = int(sub_score)
                                        dict_list[sub_name] = sub_score
                                        break
                            break
                    break
                print(f"{"Student Name" :<10} : {Stu_name}")
                print("---------------")
                print(f"   Subjects ")
                for keys,values in dict_list.items():
                    print(f"{keys :<10}: {values}")
                print("---------------")
                print(f"{"Total" :<10}: {sum(dict_list.values())} / {num_sub*100}")
                Average = sum(dict_list.values())/num_sub
                print(f"{"Average":<10}: {Average}")
                if Average >= 90:
                    print(f"{"Grade" :<10}: A")
                    print("---------------")
                    print("      ")
                elif Average >=80:
                    print(f"{"Grade":<10}: B")
                    print("---------------")
                    print("      ")
                elif Average >= 70:
                    print(f"{"Grade" :<10}: C")
                    print("---------------")
                    print("      ")
                elif Average >= 60:
                    print(f"{"Grade" :<10}: D")
                    print("---------------")
                    print("      ")
                else:
                    print(f"{"Grade" :<10}: E")
                    print("---------------")
                    print("      ")
            break
        another_stu = input("Enter marks for another student(Yes/No):")
        if another_stu.lower() == "yes":
            continue
        else:
            print("Thank You")
    break

