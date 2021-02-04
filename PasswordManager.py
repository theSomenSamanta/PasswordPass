import os
import sqlite3

path = os.environ["userprofile"]
try:
    os.mkdir(path + "\\Documents\\Password Database")
except FileExistsError:
    pass

con = sqlite3.connect(path + "\\Documents\\Password Database\\passdb.db")
cur = con.cursor()

con.execute("create table if not exists Password(passwordfor varchar(20) primary key,Password varchar(8))")


def wkstate():
    global password
    print("[1] saving Password")
    print("[2] retriving Password")
    print("[3] updating Password")
    print("[4] deleting Password")
    print("[0] or any value for exit")
    while True:
        Choice = int(input("Enter your Choice>>>"))
        if Choice == 1:
            print("enter data below to save it securely")
            pass_for = input("enter the site or software name: ")
            password = input("enter password: ")
            sql = "INSERT into Password values ('" + pass_for + "','" + password + "');"
            cur.execute(sql)
            con.commit()
            print("Successfully added your password :D")
            continue
        elif Choice == 2:
            print("your data is safe You can retrive it from here")
            pass_for = input("enter site or software name: ")
            sql = "select passwordfor, password from Password where passwordfor = '" + pass_for + "';"
            try:
                cur.execute(sql)
                for i in cur:
                    pass_for = i[0]
                    password = i[1]
                print("password found")
                print("for ", pass_for, " password is ", password)
            except:
                print("no data found")
            continue
        elif Choice == 3:
            print("ok so you want to update your pasword")
            print("Let we know for which site or software you want to update your password")
            pass_for = input("Enter software or site: ")
            password = input("enter new password: ")
            sql = "UPDATE Password set password = '" + password + "' where passwordfor = '" + pass_for + "';"
            cur.execute(sql)
            con.commit()
            print("successfully updated your password :D")
            continue
        elif Choice == 4:
            print("Ok You want to delete your password")
            print("Let we know for which site or software you want to delete your password")
            del_for = input("enter sofware or site you want to delete your password: ")
            sql = "DELETE from Password where passwordfor = '" + del_for + "';"
            cur.execute(sql)
            con.commit()
            print("Successfully deleted password :D")
            continue
        else:
            print("thank you for using securepass")
            break


master_pass = "0000"

tries = 1
if __name__ == '__main__':
    while tries <= 5:
        pas = input("enter password: ")
        if pas != master_pass:
            print("wrong password")
            print("you have", 5 - tries, " chances left")
            tries += 1
            continue
        else:
            print("access granted")
            wkstate()
            break
