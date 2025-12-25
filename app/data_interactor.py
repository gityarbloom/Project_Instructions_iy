import mysql.connector
import os
from dotenv import load_dotenv
from fastapi import HTTPException

class Contact:
    def __init__(self, first_name:str, last_name:str, phone_number:str, id:int|None = None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def to_dict(self):
        return self.__dict__

load_dotenv()

class DataConnector:
    def __init__(self):
        self.config = {
            "password": os.getenv("DB_PASSWORD", ""),
            "host": os.getenv("DB_HOST", "db"),
            "database": os.getenv("DB_NAME", "contacts_db"),
            "port": 3306,
            "user": "root",
        }

    def connecting(self):
        try:
            conn =  mysql.connector.connect(**self.config)
            return conn
        except Exception as e:
            raise HTTPException(
                status_code=400, detail=f"Error creating connection:\n{e}"
            )
            
    def create_contact(self, contact_dict:dict):
        sql = "INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)"
        params = (contact_dict["first_name"], contact_dict["last_name"], contact_dict["phone_number"])
        try:
            conn = self.connecting()
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            new_id = cursor.lastrowid
            cursor.close()
            return new_id
        except mysql.connector.Error as e:
                conn.rollback()
                raise f"Error in creation: {e}"
    
    def get_all_contacts(self):
        try:
            conn = self.connecting()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contacts")
            contact_list = cursor.fetchall()
            cursor.close()
            return contact_list
        except mysql.connector.Error as e:
            raise f"Selection error: {e}"
    
    def update_contact(self, id, contact_dict:dict):
        try:
            conn = self.connecting()
            crs = conn.cursor()
            updates = []
            for key, value in contact_dict:
                updates.append(f"{key} = {value}")

            query = f"""UPDATE contacts SET
            {', '.join(updates)}
            WHERE id = {id};"""
            crs.execute(query)
            conn.commit()
            crs.close()
            return {
                "message": "Contact updated successfully"
            }
        except mysql.connector.Error as e:
            print(f"Failed updating contact: {e}")
            return {
                "message": "Failed updating contact: {e}"
            }
        
    def delete_contact(self, id):
        try:
            conn = self.connecting()
            crs = conn.cursor()
    
            query = f"""DELETE FROM contacts
            WHERE id = {id};"""
            crs.execute(query)
            conn.commit()
            crs.close()
            return {
                "message": "Contact deleted successfully"
            }
        except mysql.connector.Error as e:
            print(f"Failed removing contact: {e}")
            return {
                "message": "Failed removing contact: {e}"
            }
