import mysql.connector as connector 

#main coding
# helper = DBHelper()
# helper.insert_user(124, "Pardarshee Priya", "7061983895")
# helper.insert_user(125, "Anushka Rai", "1234567890")
# helper.insert_user(123, "Harshal Chauhan", "2345678901")
# helper.insert_user(121, "Saurav Janartha", "3456789012")
# helper.fetch_all()
# helper.delete_user(125)
# helper.fetch_all()
# helper.update_user(121, 'Saurav', '23456709810')
# helper.fetch_all()


from dbHelper import DBHelper

def main():
    db = DBHelper()
    while True:
        print("*********WELCOME**********")
        print()
        print("Press 1 to insert new user")
        print("Press 2 to display all user")
        print("Press 3 to delete  user")
        print("Press 4 to update user")
        print("Press 5 to exit")
        print()
        try:
            choice = int(input())
            if(choice == 1):
                #insert user
                uid = int(input("Enter user id: "))
                username = input("Enter User Name: ")
                userphone = input("Enter User Phone Number: ")
                db.insert_user(uid, username, userphone)
                pass
            elif choice == 2:
                #display user
                db.fetch_all()
                pass
            elif choice == 3:
                #delete user
                userid = int(input("Enter the User Id that you want to delete: "))
                db.delete_user(userid)
                
                pass
            elif choice == 4:
                #updata user
                uid = int(input("Enter user id to update: "))
                username = input("Enter New User Name: ")
                userphone = input("Enter New User Phone Number: ")               
                db.update_user(uid, username, userphone)
                pass
            elif choice == 5:
                break
            else:
                print("Invalid Input! Try again.")
          
        except Exception as e:
          print(e)
          print("Invalid Details! Try again")

              
if __name__ == "__main__":
    main()                