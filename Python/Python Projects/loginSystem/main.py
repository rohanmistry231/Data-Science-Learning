import re
import hashlib
import csv 
import sys 
from pathlib import Path



# hashing the password with sha1
def hash_password(password):
    hsh = hashlib.sha1(
        password.encode('utf-8')
    ).hexdigest()
   
    return hsh
    

# path to the password_check.dat file
password_file = Path(__file__).with_name('password_check.txt')

def read_file():
    """
    reading username and password from the file for authentication 
    """
    db = open(password_file, 'r')
          
    password_lst = []
    users_lst = []
    for i in db:
        # print(i.split(", "))
        x, y = i.split(",")
        y = y.strip()
        users_lst.append(x)
        password_lst.append(y)
    data = dict(zip(users_lst, password_lst))
    return data

                    



def password_policy(password):
    """
    # password policy function is to validate the password length, special characters and cases conditions.
    takes password as an argument
    """
    pattern = re.compile("(?=(.*[a-z]){2,})(?=(.*[A-Z]){2,})(?=(.*[0-9]){1,})")
    special_characters = """
                "!@#$%^&*()-+?_=,<>/`\/.}]{["]}'
    """        
    if any(char in special_characters for char in password) and len(password) >= 8 and len(password) <= 12 and pattern.match(password):
        return True            
    else:
        return False
        
    
def register(username, password1, password2):
     db = read_file()
    #  print(db)
     if username  in db:
          print("Error: user already exists")
     else:
        if password1== password2:
            if password_policy(password1):
                password1=hash_password(password1)
                db = open("./password_check.dat", 'a', newline='')
                db.write(username+","+password1+'\n')
                print('Success: user registered')
            else:
                print("Error: password policy failure")
        else:
            print("Error: password doesn't match!")

    
          

               
                
 

def authenticate(username, password):
        """
        # authentication function for users
        take two arguments username and password
        """
        if not len(username or password)<1:
            data = read_file()
            try:
                if username in data:
                        if hash_password(password) == data[username]:
                            print("Sucess! login")
                        else:
                                print("Error! incorrect password.") 
                                 
                else:
                     print("Error! no such user")
                     
            except:
                 print("Error! no such user")
                  
    


def changepassword(username, password, new_password):
        """
            To change the user's password.
            changepassword takes three arguments.
            username
            password and
            a new password
        """
        reader = read_file()
        # file = open(password_file,'r')
        # reader = csv.reader(file)
        
        lst = []
                           
        Found=False
        for row in reader.items():
            # print(list(row))
            
           
            if username in row:
                # print(row[0])
                # print(row[1])
                
                row = list(row)         
                Found=True   
                if row[1]== hash_password(password):
                    if password_policy(new_password):
                        print("password policy success")
                        print("password matched") 
                    #  print(len(new_password))
                        # print(type(row[1]))
                        row[1]=  hash_password(new_password)
                        print("Success") 
                    else:
                        print("Error: password policy failure")

                else:
                     print("Error: wrong password")
                                                                                            
            lst.append(row)
        # file.close()

        if Found==False:
            print("Error: no such user")
        else:
            file = open(password_file,'w+', newline='')
            writer = csv.writer(file)
            writer.writerows(lst)
            file.seek(0)
            reader= csv.reader(file)
            
        
            file.close()
            


     
# main function and creating a command line interface
if __name__ =="__main__":

     args = sys.argv[1:]
     if args:
          function_name = args[0]
          if function_name == authenticate.__name__:
               if not len(args) == 3:
                    print("authenticate username password")
                    
               else:
                    x = args[1]
                    y = args[2]
                    authenticate(x,y)
          elif function_name == changepassword.__name__:
               if not len(args) == 4:
                    print("password_check username password new_password")
                    
               else:
                    x = args[1]
                    y = args[2]
                    z = args[3]
                    changepassword(x,y, z)
          elif function_name == register.__name__:
               if not len(args)== 4:
                    print("register username password1 password2")
               else:
                    x = args[1]
                    y = args[2]
                    z= args[3]
                    register(x,y, z)
     else:
          print("No argument provided")
     

