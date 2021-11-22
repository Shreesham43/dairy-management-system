import streamlit as st
import cx_Oracle
import pandas as pd
#try:
#cx_Oracle.init_oracle_client(lib_dir= "c:\oraclexe\instantclient_19_12")
#except:
 #   st.write()
def create_dairy():
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    dairy_id=st.text_input("Enter Dairy id here",max_chars=3)
    Dairy_Address=st.text_area("Enter Dairy Address here",max_chars=30)
    submit=st.checkbox("Create Dairy")
    if submit:
        try:
            c.execute('insert into dairy (dairy_id,dairy_address) values (:1,:2)',(dairy_id,Dairy_Address))
            con.commit()
            if c.rowcount:
                st.write("successful")
        except cx_Oracle.IntegrityError as e:
            x=e.args[0]
            if hasattr(x,'code') and hasattr(x,'message') and x.code == 1400 and 'ORA-01400' in x.message:
                st.error("Fill All the fields")
            else:
                st.error("Check Dairy ID")
    c.close()

def delete_dairy():
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    dairy_id=st.text_input('Enter dairy id whose details to be deleted',max_chars=3)
    submit=st.checkbox("Delete")
    if submit:
        out=c.execute('delete from dairy where dairy_id=:1',[dairy_id])
        con.commit()
        if c.rowcount:
            st.write("successful")
            st.write(c.rowcount," fields deleted")
        else:
            st.write(" Please enter valid dairy Id")
            st.write(c.rowcount," fields deleted")
    c.close()

def update_dairy():
    my_dairy_id=st.text_input('Enter dairy id ',max_chars=3)
    submit=st.checkbox("submit")
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    c.execute("select * from dairy where dairy_id=:1",[my_dairy_id])
    data=c.fetchall()
    if submit:
        if c.rowcount:
            list2=[]
            list2.append(data[0][1])
            dairy_Address=st.text_area("Dairy Address",list2[0],max_chars=30)
            submit1=st.checkbox("Update Changes")
            if submit1:
                try:
                    c.execute('update dairy set  dairy_address=:2  where dairy_id=:3' ,(dairy_Address,my_dairy_id))
                    con.commit()
                    if c.rowcount:
                        st.write("successful")
                        st.write(c.rowcount," fields updated")
                except:
                    st.error("Address cannot be null")
        else:
            st.write("No fields found")
    c.close()

def retrieve_all_dairy():
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    c.execute("select * from dairy ")
    data=c.fetchall()
    list1=[]
    list2=[]
    for i in range(c.rowcount):
        m=i
        n=0
        list1.append(data[m][n])
        n+=1
        list2.append(data[m][n])
    view=st.checkbox("Fetch details")
    try:
        if view:
            df = pd.DataFrame({"dairy_id": list1, "Dairy_address": list2})
            st.write(df)
    except:
        st.write("No value exists")
    c.close()

def create_staff():
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    staff_id=st.text_input("Enter Staff id here",max_chars=5)
    dairy_id=st.text_input("Enter Dairy id here",max_chars=3)
    f_name=st.text_input("Enter First name here",max_chars=10)
    l_name=st.text_input("Enter Last name here",max_chars=10)
    submit=st.checkbox("Create staff")
    if submit:
        if(len(staff_id)!=5):
            st.error("Invalid staff id")
        elif(len(f_name)==0):
            st.error("First name cannot be null")
        elif(staff_id[0]==dairy_id[0] and staff_id[1]==dairy_id[1] and staff_id[2]==dairy_id[2]):
            try:
                c.execute('insert into staff (staff_id , dairy_id, f_name, l_name) values (:staff_id,:dairy_id,:f_name,:l_name)',(staff_id,dairy_id,f_name,l_name))
                con.commit()
                if c.rowcount:
                    st.write("successful")
                    c.execute('update staff set password=:1 where staff_id=:2' ,(staff_id,staff_id))
                    con.commit()
            except:
                st.error('Please check Staff ID/Dairy ID values')
        else:
            st.error("Dairy id does not match with staff id")
    c.close()

def delete_staff():
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    staff_id=st.text_input('Enter satff id whose details to be deleted',max_chars=5)
    submit=st.checkbox("Delete")
    if submit:
        out=c.execute('delete from staff where staff_id=:staff_id',[staff_id])
        con.commit()
        if c.rowcount:
            st.write("successful")
            st.write(c.rowcount," fields deleted")
        else:
            st.write(" Please enter valid Staff Id")
            st.write(c.rowcount," fields deleted")
    c.close()

def update_staff():
    my_staff_id=st.text_input('Enter satff id ',max_chars=5)
    submit=st.checkbox("submit")
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    c.execute("select * from staff where staff_id=:staff_id",[my_staff_id])
    data=c.fetchall()
    if submit:
        if c.rowcount:
            list1=[]
            list1.append(data[0][1])
            list1.append(data[0][2])
            list1.append(data[0][3])
            dairy_id=st.text_input("Dairy ID",list1[0],max_chars=3)
            First_Name=st.text_input("First Name",list1[1],max_chars=10)
            Last_Name=st.text_input("Last Name",list1[2],max_chars=10)
            submit1=st.checkbox("Update Changes")
            if submit1:
                if(len(dairy_id)==0):
                    st.error("Dairy ID cannot be null")
                elif(my_staff_id[0]==dairy_id[0] and my_staff_id[1]==dairy_id[1] and my_staff_id[2]==dairy_id[2]):
                    try:
                        c.execute('update staff set  dairy_id=:2 , f_name=:3,l_name=:4 where staff_id=:5' ,(dairy_id,First_Name,Last_Name,my_staff_id))
                        con.commit()
                        if c.rowcount:
                            st.write("successful")
                            st.write(c.rowcount," fields updated")
                    except cx_Oracle.DatabaseError:
                        st.error("First Name cannot be empty")
                else:
                    st.error("Dairy ID does not match")
        else:
            st.error("No fields found")
    c.close()

def retrieve_all_staff():
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    view=0
    search=st.radio('Search by',('Staff ID','Dairy ID','View all'))
    if search=='Staff ID':
        sid=st.text_input('Enter Staff Id')
        option=st.checkbox('submit')
        if option:
            c.execute('select * from staff where staff_id=:1 ',[sid])
            view=1
    if search=='Dairy ID':
        did=st.text_input('Enter Dairy Id')
        option=st.checkbox('submit')
        if option:
            c.execute('select * from staff where dairy_id=:1',[did])
            view=1
    if search=='View all':
        c.execute("select * from staff ")
        view=1
    if view:
        data=c.fetchall()
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        for i in range(c.rowcount):
            m=i
            n=0
            list1.append(data[m][n])
            n+=1
            list2.append(data[m][n])
            n+=1
            list3.append(data[m][n])
            n+=1
            list4.append(data[m][n])
            n+=1
    view=st.checkbox("Fetch details")
    try:
        if view:
            df = pd.DataFrame({"Staff_id": list1, "Dairy_id": list2,"First name":list3,"Last Name":list4})
            st.write(df)
    except:
        st.write("No value exists")
    c.close()

def change_password():
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    my_staff_id=st.text_input('Enter satff id ',max_chars=5)
    new_password=st.text_input('Enter new password',max_chars=10,type='password')
    submit=st.checkbox('change password')
    if submit:
        c.execute('update staff set password=:1 where staff_id=:2' ,(new_password,my_staff_id))
        con.commit()
        if c.rowcount:
            st.write('Successfully changed')
        else:
            st.write("inavlid staff id")


def default():
    table=st.selectbox('Select the table',("None","Dairy","Staff"),key=6)
    if table=="Dairy":
        option=st.selectbox('Select Operations',("None","Enter New Dairy details","Delete Dairy Details","Update Dairy Details","View all Details"),key=7)
        if option=="Enter New Dairy details":
            create_dairy()
        if option=="Delete Dairy Details":
            delete_dairy()
        if option=="Update Dairy Details":
            update_dairy()
        if option=="View all Details":
            retrieve_all_dairy()
    if table=="Staff":
        option=st.selectbox('Select Operations',("None","Enter New Staff details","Delete Staff Details","Update Staff Details","View all Details","Change Staff Login Password"),key=8)
        if option=="Enter New Staff details":
            create_staff()
        elif option=="Delete Staff Details":
            delete_staff()
        elif option=="View all Details":
            retrieve_all_staff()
        elif option=="Update Staff Details":
            update_staff()
        elif option=="Change Staff Login Password":
            change_password()


