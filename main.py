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


def ques():
    ask = input("Who are you? /1 - Boss/ 2 - BossHelper/ 3 - Employee/ 4 - EXIT: ")
    eploy_intance = eploye()
    #b_h_f = boss_helper()
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