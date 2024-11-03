import pandas as pd

def name():                             #Fungsi Def
    print("-------------------")
    print("Happy Shopping Mini Apps")
    print("-------------------\n")
    name1 = input("First Name : ")
    name11 = input("Last Name : ")
    return f"{name1} {name11}"

def displayname(fullname):
    print(f"\n Welcome {fullname} \n") 

fullname = name()
displayname(fullname)
   
def menu():
    print("1. Add Item")
    print("2. Show Item")
    print("3. Delete Item")
    print("4. Exit")

def data():
       n = int(input("Enter number of items: "))
       for _ in range(n):                              #Fungsi For Loop
              item_ = input("Enter item_: ")
              price = int(input("Enter price: "))
              stock = input("Enter stock: ")
              key_value_list.append({"item_": item_, "price": price, "stock": stock}) #DIctionary di dalam List

def delete():
    key_value_list_delete = int(input("Delete item number: ")) - 1      #Fungsi Input
    key_value_list.pop(key_value_list_delete)
    return main()
    

def display():
        #num = 1
        #print(f"There are your items:")
        #for i in key_value_list:
         #   print(f"{num}.{i}")
          #  num += 1
        print(f"Hello {fullname}, you have: {len(key_value_list)} items\n")
        df = pd.DataFrame(key_value_list)
        df.index += 1
        print(df)
        print("\n")
        return main()

def _exit():    
    exit_ = input("Do you want to exit (y/n) : ")
    if exit_ == 'y':
        print("Thank you :)")
        exit()
    else:
        print("Please add your items: ")
        data()
        display()

     
def main():
    menu()
    try:                                                        #Fungsi Try Except
            user_input = int(input("Insert your choice : "))
            if user_input == 4:
             _exit()
            if user_input in [1,2,3]:
                if user_input == 1:    #Fungsi If,Elif dan else
                    data()
                    main()
                elif user_input == 2:
                    display()
                    try:
                     if not key_value_list:
                        print("No item added, please input your items\n")
                        return main()
                    except NameError:
                        print("No item added, please input your items")          
                elif user_input == 3:
                    if not key_value_list:
                        print("No item added, please input your items")
                        return main()
                    else:
                     delete()
    except ValueError:
        print("Input must be a number")


if __name__ == "__main__":   #Fungsi Main
 user_input = int
 key_value_list = []
 main()
