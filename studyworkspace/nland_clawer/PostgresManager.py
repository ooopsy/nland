import psycopg2
import psycopg2.extensions




class PostgresManager:
    connectionURL = ''
    userName = ''
    passwd= ''
    port = '5432'


    @staticmethod
    def connection():
        return psycopg2.connect()