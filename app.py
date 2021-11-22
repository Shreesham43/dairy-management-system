import streamlit as st
import cx_Oracle
import Admin
import Staff
import queries
#//try:
#cx_Oracle.init_oracle_client(lib_dir= "c:\oraclexe\instantclient_19_12")
#//except:
#  st.write()

#queries.run_query()

def authentication(name,psd):
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    c.execute('select * from info where staff_id=:name and staff_password=:psd',(name,psd))
    data=c.fetchall()
    c.close()
    return data

def authentication_staff(name,psd):
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    c.execute('select * from staff where staff_id=:name and password=:psd',(name,psd))
    data=c.fetchall()
    c.close()
    return data


count=1
staff=''
choice1=''
try:
    choice1=st.selectbox(" Main Menu",("Select","Admin","Staff"),key=count)
except:
    st.write()
count+=1
if choice1=="Admin":
    name=st.text_input("Admin id",max_chars=5)
    psd=st.text_input("password",type="password")
    if st.checkbox("Login"):
        value=authentication(name,psd)
        if value:
            st.write("Login is successful as ",name)
            Admin.default()
        else:
            st.write("Invalid Username/Password")
if choice1=="Staff":
    name=st.text_input("Staff id")
    psd=st.text_input("password",type="password")
    if st.checkbox("Login"):
        value=authentication_staff(name,psd)
        if value:
            st.write("Login is successful as ", name)
            staff=name
            Staff.default(staff)
        else:
            st.write("Invalid Username/Password")



