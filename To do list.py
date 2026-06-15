tasks = []
def task():    
    print("WELCOME TO THE TO DO MANAGEMENT APP")

    total_task = int(input("Enter number of task you want to add in the list :"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n {tasks}")  

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        if operation == 1:
            add = input("Enter the task you want to add :")
            tasks.append(add)
            print(f"Task {add} has been successfully added in the list")

        elif operation == 2:
            updated_value = input("Enter the task you want to Update :")
            if updated_value in tasks:
                up=input ("Enter new task =")
                ind = tasks.index(updated_value)
                tasks[ind] = up
            print(f"Task{updated_value} has been successfully updated in the list") 

        elif operation == 3:
            del_val  = input("Enter the task you want to Delete :")
            if del_val in tasks:
                ind = tasks.remove(del_val)
                print(f"Task{del_val} has been successfully deleted from the list") 

        elif operation == 4:
            print(f"Total task ={task}") 

        elif operation ==5 :
            print(f"Closing the program....") 
            break
        else:
            print("Invlid Input")

task()