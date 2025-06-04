import mysql.connector
import random




class DbManagement:
    
    
    def __init__(self):
        self.make_connection_with_sql()
        self.generate_account_number()
        # self.home_window()
        
    def generate_account_number(self):
        self.cursor.execute("select acc_no from customer_account;")
        print(self.cursor.fetchall())
        return random.randint(1_000_000, 9_999_999)
        
    def sign_up(self):
        acc_no   = "1234567"
        name     = "sunil"
        pin      = "1234"
        balance  = 0
        dob      = "2000-03-30"
        password = "q3er23qe32r43rsy453"
        
        values = (acc_no, name, pin, balance, password, dob)
        
        sql_query = """INSERT INTO `bankdb`.`customer_account`
                                         (`acc_no`, `name`, `pin`, `balance`, `password`, `dob`)
                                         VALUES (%s, %s, %s, %s, %s, %s);"""
        
        self.cursor.execute(sql_query, values)
        self.connection.commit()
        

        print("account created" )
        
        
    def login(self):
        pass
    
    
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
    
    def withdraw_balance(self):
        pass
    
    def transfer_money(self):
        pass    
    
    
