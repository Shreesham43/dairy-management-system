import streamlit as st
import cx_Oracle
import pandas as pd
#try:
 #   cx_Oracle.init_oracle_client(lib_dir= "c:\oraclexe\instantclient_19_12")
#except:
 #   st.write()
def run_query():
    try:
        con=cx_Oracle.connect('shreesha/1204@localhost')
        c=con.cursor()
        c.execute("""CREATE TABLE DAIRY(
        DAIRY_ID VARCHAR(3),
        DAIRY_ADDRESS VARCHAR(30),
        PRIMARY KEY (DAIRY_ID))""")
    except:
        st.write("error")

    try:
        con=cx_Oracle.connect('shreesha/1204@localhost')
        c=con.cursor()
        c.execute("""CREATE TABLE STAFF(
        STAFF_ID VARCHAR(5),
        DAIRY_ID VARCHAR(3),
        F_NAME VARCHAR(10),
        L_NAME VARCHAR(10),
        PRIMARY KEY (STAFF_ID),
        FOREIGN KEY (DAIRY_ID) REFERENCES DAIRY(DAIRY_ID) ON DELETE CASCADE)""")
    except:
        st.write()

    try:
        con=cx_Oracle.connect('shreesha/1204@localhost')
        c=con.cursor()
        c.execute("""CREATE TABLE SELLER(
        SELLER_ID VARCHAR(5),
        F_NAME VARCHAR(10),
        L_NAME VARCHAR(10),
        S_ADDRESS VARCHAR(30),
        CONTACT_NUMBER INT,
        PRIMARY KEY (SELLER_ID))""")
    except:
        st.write()

    try:
        con=cx_Oracle.connect('shreesha/1204@localhost')
        c=con.cursor()
        c.execute("""CREATE TABLE BUYER(
        BUYER_ID INT ,
        NAME VARCHAR(10),
        QUANTITY FLOAT(2),
        PRICE FLOAT(2),
        PRIMARY KEY (BUYER_ID))""")
    except:
        st.write()

    try:
        con=cx_Oracle.connect('shreesha/1204@localhost')
        c=con.cursor()
        c.execute(""""CREATE TABLE MILK(
        SELLER_ID VARCHAR(5),
        DATE_OF_PURCHASE DATE,
        TYPE VARCHAR(10),
        FAT NUMBER(32,30),
        QUANTITY NUMBER(32,30),
        PRICE NUMBER(32,30),
        PRIMARY KEY(SELLER_ID,DATE_OF_PURCHASE),
        FOREIGN KEY (SELLER_ID) REFERENCES SELLER(SELLER_ID) ON DELETE CASCADE);""")
    except:
        st.write()

    try:
        con=cx_Oracle.connect('shreesha/1204@localhost')
        c=con.cursor()
        c.execute("""CREATE TABLE COLLECT(
        STAFF_ID VARCHAR(5),
        SELLER_ID VARCHAR(5),
        DATE_OF_COLLECT DATE,
        PRIMARY KEY (STAFF_ID,SELLER_ID,DATE_OF_COLLECT),
        FOREIGN KEY (SELLER_ID) REFERENCES SELLER(SELLER_ID) ON DELETE CASCADE,
        FOREIGN KEY(STAFF_ID) REFERENCES STAFF(STAFF_ID) ON DELETE CASCADE)""")
    except:
        st.write()

    try:
        con=cx_Oracle.connect('shreesha/1204@localhost')
        c=con.cursor()
        c.execute("""CREATE TABLE SELL_MILK(
        STAFF_ID VARCHAR(5),
        BUYER_ID INT,
        DATE_OF_SALE DATE,
        PRIMARY KEY(STAFF_ID,BUYER_ID,DATE_OF_SALE),
        FOREIGN KEY (BUYER_ID) REFERENCES BUYER(BUYER_ID) ON DELETE CASCADE,
        FOREIGN KEY(STAFF_ID) REFERENCES STAFF(STAFF_ID) ON DELETE CASCADE)""")
    except:
        st.write()

    try:
        con=cx_Oracle.connect('shreesha/1204@localhost')
        c=con.cursor()
        c.execute("""CREATE TABLE INFO(
        STAFF_ID VARCHAR(3),
        STAFF_PASSWORD VARCHAR(10),
        PRIMARY KEY(STAFF_ID));
        INSERT INTO INFO VALUES('&STAFF_ID','&STAFF_PASSWORD')""")
    except:
        st.write()

    try:
        con=cx_Oracle.connect('shreesha/1204@localhost')
        c=con.cursor()
        c.execute("""CREATE OR REPLACE PROCEDURE SELL(
        ST_ID STAFF.STAFF_ID%TYPE,
        B_ID INT,
        DATE_COLLECT DATE)
        IS
        BEGIN INSERT INTO SELL_MILK (STAFF_ID,BUYER_ID,DATE_OF_SALE) VALUES (ST_ID,B_ID, DATE_COLLECT);
        COMMIT;
        END;""")
    except:
        st.write()

    try:
        con=cx_Oracle.connect('shreesha/1204@localhost')
        c=con.cursor()
        c.execute("""CREATE OR REPLACE PROCEDURE INSERT_COLLECT (
        ST_ID STAFF.STAFF_ID%TYPE,
        S_ID SELLER.SELLER_ID%TYPE,
        DATE_COLLECT DATE)
        IS
        BEGIN INSERT INTO COLLECT (STAFF_ID,SELLER_ID,DATE_OF_COLLECT) VALUES (ST_ID, S_ID, DATE_COLLECT);
        COMMIT;
        END;""")
    except:
        st.write()


    try:
        con=cx_Oracle.connect('shreesha/1204@localhost')
        c=con.cursor()
        c.execute("""CREATE SEQUENCE BUYER_ID MINVALUE 1 START WITH 1 CACHE 10;""")
    except:
        st.write()