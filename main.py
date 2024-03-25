from abc import ABCMeta, abstractmethod
import sqlite3
import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO

connect = sqlite3.connect('WR.db')
cursor = connect.cursor()
#create DataBase
table = cursor.execute("""CREATE TABLE IF NOT EXISTS WR (
                    Email VARCHAR(255) NOT NULL,
                    First_Name CHAR(25) NOT NULL,
                    Last_Name CHAR(25),
                    Password VARCHAR(255),
                    Payment INT,
                    Status CHAR(25)
                )""")


#cursor.execute("INSERT INTO WR VALUES ('Bossy@gmail.com', 'Ondy', 'Landj', 'Ltbs_3562', '50000','Boss')")
#connect.commit()



class eploye():
    @classmethod
    @abstractmethod

    #Checker to check if people with inputed name and surname is with status employee
    def chack_emp(cls):
        f_name = input("Your first name: ")
        s_name = input("Your second name: ")
        password = input("Your password: ")
        chack_stat = cursor.execute("SELECT Status FROM WR WHERE First_Name= ? AND Last_Name = ? AND Password = ?",
                             (f_name, s_name, password)).fetchall()
        if chack_stat:
          print(chack_stat[0][0])
          chack_stat = chack_stat[0][0]
        else:
          print("No status found for the provided information.")
        if chack_stat == "Employee":
            eploy_intance = eploye()
            ask = input("What would you like to do?\n 1. Change your Email \n 2. Check your payment \n Answer:  ")
            if int(ask) == 1:
                eploy_intance.change_email(f_name, s_name)
            elif int(ask) == 2:
                eploy_intance.see_my_payment(password, f_name, s_name)
        else:
            print("You are not Employee")
            ques()

    #Code to check emploe`s payment
    def see_my_payment(cls, password, f_name, s_name):
        s_name = s_name
        f_name = f_name
        password = password
        f_d = cursor.execute("SELECT Email, First_Name, Last_Name, Payment FROM WR WHERE First_Name = ? AND Last_Name = ? AND Password = ?",
                             (f_name, s_name, password)).fetchall()
        if not f_d:
            print("Can`t find")
        if f_d:
            s_name = s_name
            f_name = f_name
            password = password
            data = cursor.execute("SELECT Payment FROM WR WHERE First_Name = ? AND Last_Name = ? AND Password = ?",
                             (f_name, s_name, password)).fetchall()

            print(f"Your payment is: {data[0][0]} UAN")
            ques()


    #Code to change emploe`s Email
    def change_email(self,f_name, s_name):

        f_name = f_name
        s_name = s_name
        password = input("Your password: ")
        f_d = cursor.execute("SELECT Email, First_Name, Last_Name, Payment FROM WR WHERE  First_Name= ? AND Last_Name = ? AND Password = ?",
                             (f_name, s_name, password)).fetchall()

        if not f_d:
            print("Can`t find")
        if f_d:
            em = input("Your new email address: ")
            data = cursor.execute("UPDATE WR SET Email = ? WHERE First_Name= ? AND Last_Name = ? AND Password = ?",
                                  (em, f_name, s_name, password)).fetchall()
            print("Your Email has been changed")
            connect.commit()
            ques()


#Create class boss_helper
class boss_helper(eploye):
    @classmethod
    @abstractmethod

    #Same like chacker in employee but chacking if people with entered
    #name and surname has status of Boss Helper
    def boss_helper(cls):
            bss_h = boss_helper
            f_name = input("Your first name: ")
            s_name = input("Your second name: ")
            password = input("Your password: ")
            chack_stat = cursor.execute("SELECT Status FROM WR WHERE First_Name= ? AND Last_Name = ? AND Password = ?",
                                        (f_name, s_name, password)).fetchall()
            if chack_stat:
              print(chack_stat[0][0])
              chack_stat = chack_stat[0][0]
            else:
              print("No status found for the provided information.")
            if chack_stat == "Boss_Helper":
                eploy_intance = eploye()
                ask = input("What would you like to do?\n 1. Change your Email \n 2. Check your payment \n 3. Check number of stuff\n Answer:  ")
                if int(ask) == 1:
                    eploy_intance.change_email(f_name, s_name)
                elif int(ask) == 2:
                    eploy_intance.see_my_payment(password, f_name, s_name)
                elif int(ask) == 3:
                    bss_h.b_h(cls)
                    ques()
            else:
                print("You are not Boss Helper")
                ques()

    #Code to count number of stuff
    def b_h(cls):
        count = cursor.execute("SELECT COUNT(*) FROM WR").fetchone()[0]
        print(f"Number of people in the database: {count}")

# Create class Boss
class boss(boss_helper):
    @classmethod
    @abstractmethod
    # Same checker but for BOSS
    def chacker(cls):
            bss = boss()
            bss_h = boss_helper
            f_name = input("Your first name: ")
            s_name = input("Your second name: ")
            password = input("Your password: ")
            chack_stat = cursor.execute("SELECT Status FROM WR WHERE First_Name= ? AND Last_Name = ? AND Password = ?",
                                        (f_name, s_name, password)).fetchall()

            #Questions what would to do
            if chack_stat:
              chack_stat = chack_stat[0][0]
            else:
              print("No status found for the provided information.")
            if chack_stat == "Boss":
                eploy_intance = eploye()
                ask = input("What would you like to do?\n 1. Change your Email \n 2. Check your payment \n 3. Check number of stuff \n 4. Delete some member"
                            " \n 5. Update Information of member \n 6. Watch all members information \n 7. Add member \nAnswer:  ")
                if int(ask) == 1:
                    eploy_intance.change_email(f_name, s_name)
                elif int(ask) == 2:
                    eploy_intance.see_my_payment(password, f_name, s_name)
                elif int(ask) == 3:
                    bss_h.b_h(cls)
                    ques()
                elif int(ask) == 4:
                    bss.del_mem()
                elif int(ask) == 5:
                    bss.up_dat_mem()
                elif int(ask) == 6:
                    bss.ch_al_on()
                elif int(ask) == 7:
                    bss.add_mem()

            else:
                print("You are not Boss Helper")
                ques()

                # Code to delete a member of stuff
                def del_mem(self):
                    F_n = input("Input first name of people who you would like delete: ")
                    S_n = input("Input second name of people who you would like delete: ")
                    E_a = input("Input Email of people who you would like delete: ")

                    data = ("SELECT * FROM WR")

                    row = cursor.execute("SELECT * FROM WR WHERE First_Name = ? AND Last_Name = ? AND Email = ?",
                                         (F_n, S_n, E_a))
                    for data in row:
                        print(data)

                    cursor.execute("DELETE FROM WR WHERE First_Name = ? AND Last_Name = ? AND Email = ?",
                                   (F_n, S_n, E_a))

                    for data in row:
                        print(data)

                    ques()

                # Chacnge Email OR First Name OR Second Name OR Payment for staff
                def up_dat_mem(self):
                    f_n = input("Input first name of people who you would like update information: ")
                    s_n = input("Input second name of people who you would like update information: ")
                    e_a = input("Input Email of people who you would like update information: ")
                    q_on = input(
                        "What you would like change? \n 1. Email \n 2. First Name \n 3. Second Name \n 4. Payment \n Answer: ")
                    if int(q_on) == 1:

                        f_d = cursor.execute(
                            "SELECT Email, First_Name, Last_Name, Payment FROM WR WHERE  First_Name= ? AND Last_Name = ? AND Email = ?",
                            (f_n, s_n, e_a)).fetchall()

                        if not f_d:
                            print("Can`t find")
                        if f_d:
                            em = input("Employee`s new email address: ")
                            data = cursor.execute(
                                "UPDATE WR SET Email = ? WHERE First_Name= ? AND Last_Name = ? AND Email = ?",
                                (em, f_n, s_n, e_a)).fetchall()
                            print("Employee`s Email has been changed")
                            connect.commit()
                            ques()

                    if int(q_on) == 2:

                        f_d = cursor.execute(
                            "SELECT Email, First_Name, Last_Name, Payment FROM WR WHERE  First_Name= ? AND Last_Name = ? AND Email = ?",
                            (f_n, s_n, e_a)).fetchall()

                        if not f_d:
                            print("Can`t find")
                        if f_d:
                            em = input("Employee`s new name: ")
                            data = cursor.execute(
                                "UPDATE WR SET First_Name = ? WHERE First_Name= ? AND Last_Name = ? AND Email = ?",
                                (em, f_n, s_n, e_a)).fetchall()
                            print("Employee`s First Name has been changed")
                            connect.commit()
                            ques()
                    if int(q_on) == 3:

                        f_d = cursor.execute(
                            "SELECT Email, First_Name, Last_Name, Payment FROM WR WHERE  First_Name= ? AND Last_Name = ? AND Email = ?",
                            (f_n, s_n, e_a)).fetchall()

                        if not f_d:
                            print("Can`t find")
                        if f_d:
                            em = input("Employee`s new Second Name: ")
                            data = cursor.execute(
                                "UPDATE WR SET First_Name = ? WHERE Last_Name= ? AND Last_Name = ? AND Email = ?",
                                (em, f_n, s_n, e_a)).fetchall()
                            print("Employee`s Second Name has been changed")
                            connect.commit()
                            ques()

                    if int(q_on) == 4:
                        f_d = cursor.execute(
                            "SELECT Email, First_Name, Last_Name, Payment FROM WR WHERE  First_Name= ? AND Last_Name = ? AND Email = ?",
                            (f_n, s_n, e_a)).fetchall()

                        if not f_d:
                            print("Can`t find")
                        if f_d:
                            em = input("Employee`s new Payment: ")
                            data = cursor.execute(
                                "UPDATE WR SET Payment = ? WHERE First_Name= ? AND Last_Name = ? AND Email = ?",
                                (em, f_n, s_n, e_a)).fetchall()
                            print("Employee`s Payment has been changed")
                            connect.commit()
                            ques()


#-------------------------------------------------------------------------------------------------------------

def ques():
    ask = input("Who are you? /1 - Boss/ 2 - BossHelper/ 3 - Employee/ 4 - EXIT: ")
    eploy_intance = eploye()
    b_h_f = boss_helper()
    #bs = boss()
    if int(ask) == 3:
        print("Fine")
        eploy_intance.chack_emp()

    elif int(ask) == 2:
        b_h_f.boss_helper()

    elif int(ask) == 1:
        bs.chacker()

    elif int(ask) == 4:
        exit()


ques()