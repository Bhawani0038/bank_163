import mysql.connector
import random
from datetime import datetime

from zxcvbn import zxcvbn



class DbManagement:
    
    
    def __init__(self):
        self.make_connection_with_sql()
        self.home_window()
        
    def generate_account_number(self):
        return random.randint(1_000_000, 9_999_999)
    
    def check_password_strength(self):
        while True:
            password = input("password:")
            result = zxcvbn(password)
            score = result['score']  # 0 to 4

            print(f"Password strength score: {score} / 4")

            if score < 4:
                print("❌ Weak password.")
            else:
                return password
        
    def verify_pin(self):
        while True:
            pin_no = input("Enter 4 digit pin: ")
            if len(pin_no) == 4 and pin_no.isdigit():
                return pin_no
            else:
                print("wrong pin try again")
            
    def get_valid_date(self):
        while True:
            date_input = input("Enter a date (YYYY-MM-DD): ")
            try:
                # Try to parse the date
                valid_date = datetime.strptime(date_input, "%Y-%m-%d")
                return str(valid_date.date())
            except ValueError:
                print("❌ Invalid date format or date. Please enter again in YYYY-MM-DD format.")
        
    def sign_up(self):
        try:
            acc_no   = self.generate_account_number()
            name     = input("name: ")
            pin      = self.verify_pin()
            balance  = 0
            dob      = self.get_valid_date()
            password = self.check_password_strength()
            
            values = (acc_no, name, pin, balance, password, dob)
            sql_query = """INSERT INTO `bankdb`.`customer_account`
                                            (`acc_no`, `name`, `pin`, `balance`, `password`, `dob`)
                                            VALUES (%s, %s, %s, %s, %s, %s);"""
                                            
            
            self.cursor.execute(sql_query, values)
            self.connection.commit()
            print(f"account created {name = }  {acc_no = }  {pin = } {balance = } {dob = }  {password = }")
        except Exception as e:
            print("internal error...please try again")
            print(f"Debug Info: {e}")
            # self.sign_up()
        
    def login(self):
        self.acc_no = input("Account no: ")
        self.password = input("Password:  ")   
        self.cursor.execute(f"select * from customer_account where acc_no = '{self.acc_no}' and password = '{self.password}'") 
        if self.cursor.fetchone():
            self.customer_process_window()
        else:
            print("wrong credential")
    
    def home_window(self):
        choice = input("""
                       1: Sign Up
                       2: Login
                       3: Exit
                """)
        
        if choice == "1":
            self.sign_up()
            
        elif choice == "2":
            self.login()
            
        elif choice == "3":
            exit()       
                    
    def make_connection_with_sql(self):
        self.connection = mysql.connector.connect(
            host="localhost",       
            user="root", 
            password = '1234'          
        )

        self.cursor = self.connection.cursor()
        
        #make database query
        self.cursor.execute("create database if not exists bankdb;")
        self.cursor.execute("use bankdb;")  #select  DATABASE
        
        
        #CREATE BANKDB
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS customer_account (
                                acc_no CHAR(7),
                                name VARCHAR(100) NOT NULL,
                                pin CHAR(4) NOT NULL,
                                balance FLOAT DEFAULT 0 CHECK (balance >= 0),
                                password VARCHAR(100) NOT NULL CHECK (
                                    LENGTH(password) >= 8),
                                dob DATE NOT NULL,
                                primary key(`acc_no`)
                            );""")
    
        self.connection.commit()
                
        
    def create_table_into_database(self):
        pass
    
    def connect_to_database(self):
        pass
    
    def check_balance(self):
        pass
    
    def deposit(self):
        pass
    
    def withdraw_balance(self):
        pass
    
    def transfer_money(self):
        pass    
    
    def change_password(self):
        pass
    
    def customer_process_window(self):
        while True:
            choice = input("""
                        1: Withdraw
                        2: Chceck Balance
                        3: Deposit
                        4: Transfer money
                        5: Change Password
                        6: Exit
                        
                        """)

            if choice == "1":
                self.withdraw_balance()
                
            elif choice == "2":
                self.check_balance()
                
            elif choice == "3":
                self.deposit()
                
            elif choice == "4":
                self.transfer_money()
            
            elif choice == "5":
                self.change_password()
                
            elif choice == "6":
                print("exitting the app.........")
                exit()