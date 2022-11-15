from dotenv import load_dotenv
import json
import psycopg2
import os

load_dotenv()


class database:

    def postegres_connection(self):

        conn = psycopg2.connect(
        host = os.getenv('HOST'),
        database = os.getenv('DATABASE'),
        user = os.getenv('USER'),
        password = os.getenv('PASSWORD'))
    
        return conn




class user_signup(database):

    def __init__(self,data):

        self.data=data
     

    def dump_into_database(self):

        conn = self.postegres_connection()
        cur = conn.cursor()

        data = self.data['body']
        uid = data['uuid']
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']

        insert_col = 'insert into signup(uid,email,first_name,last_name) values (%s,%s,%s,%s)'
        insert_value = (uid,email,first_name,last_name)

        cur.execute(insert_col,insert_value)

        conn.commit()


        print(data)

        print('data loading completed')


class user_signout(database):

    def __init__(self,data):
        self.data=data
    

   

    def dump_into_database(self):

        conn = self.postegres_connection()
        cur = conn.cursor()

        data = self.data['body']
        uid = data['uuid']
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']

        insert_col = 'insert into signOut(uid,email,first_name,last_name) values (%s,%s,%s,%s)'
        insert_value = (uid,email,first_name,last_name)


        cur.execute(insert_col,insert_value)

        conn.commit()

        print('data loading completed')






class user_subscribe(database):

    def __init__(self,data):
        self.data=data

   

    def dump_into_database(self):

        conn = self.postegres_connection()
        cur = conn.cursor()
        
        data = self.data['body']
        uid = data['uuid']
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']

        insert_col = 'insert into subscribe(uid,email,first_name,last_name) values (%s,%s,%s,%s)'
        insert_value = (uid,email,first_name,last_name)

        cur.execute(insert_col,insert_value)

        conn.commit()

        print('data loading completed')






class no_database(database):

    def __init__(self):
        pass

    def dump_into_database(self):        
        print('please try again')