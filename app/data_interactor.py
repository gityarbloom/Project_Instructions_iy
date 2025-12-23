import mysql.connector

class DataConnector:
    def __init__(self):
        self._connection = self.get_connection()

    def get_connection(self):
        if self._connection.is_connected():
            return self.connection

        connection = mysql.connector.connect({
            "host": "",
            "root":
        })

        self._connection = connection

        return self._connection
    
    def disconnect(self):
        if self._connection != None:
            self._connection.disconnect()