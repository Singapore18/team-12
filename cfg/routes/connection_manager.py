import pymysql
import os
import csv
import sys

import config

class connection_manager(object):
    '''
    Class solely deals with handling connections to the database. Think of it like a connection factory
    limits connections based on certain settings as follows bellow in settings section
    '''

    def __init__(self, read_timeout=30, write_timeout=30, connect_timeout=30, local_infile=True, cursorclass=pymysql.cursors.DictCursor):

        host            = config.LOCAL_HOST
        if sys.platform == 'linux': host = ""
        port            = config.DBPORT
        database        = config.DBSCHEMA
        username        = config.DBUSERNAME
        password        = config.DBPASSWORD

        # LOOK INTO CURSORS
        self.connection = pymysql.connect(host=host,
                                          port=port,
                                          db=database,
                                          read_timeout=read_timeout,        # Timeout for reading from the connection in seconds
                                          write_timeout=write_timeout,
                                          connect_timeout=connect_timeout,
                                          local_infile=local_infile,        # Allows SQL "LOAD DATA LOCAL INFILE" command to be used
                                          user=username,
                                          passwd=password,
                                          cursorclass=cursorclass,
                                          autocommit=True)
        # Note: Cursors are what pymysql uses interact with databases, its the equivalent to a Statement in java


    def close_all(self, cursor=None, connection=None):
        '''
        Helper method to close cursor and connection
        '''
        if cursor is not None:
            cursor.close()
        connection.close()
