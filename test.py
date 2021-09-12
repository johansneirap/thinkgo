import os
import platform
import cx_Oracle

# This is the path to the ORACLE client files
lib_dir = r"C:\Program Files\instantclient_19_12"

try:
    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
except Exception as err:
    print("Error connecting: cx_Oracle.init_oracle_client()")
    print(err);