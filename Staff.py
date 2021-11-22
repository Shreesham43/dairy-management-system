import streamlit as st
import cx_Oracle
import pandas as pd
from datetime import date
from app import staff
#try:
 #   cx_Oracle.init_oracle_client(lib_dir= "c:\oraclexe\instantclient_19_9")
#except:
 #   st.write()
def create_seller(staff):
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    seller_id=st.text_input("Enter Seller id here",max_chars=6)
    f_name=st.text_input("Enter first name here",max_chars=10)
    l_name=st.text_input("Enter last name here",max_chars=10)
    s_address=st.text_area("Enter Seller Address here",max_chars=30)
    ph_no=st.text_input("Enter Seller Phone Number here",max_chars=10)
    dairy_id=staff[0:3]
    submit=st.checkbox("Create Seller")
    if submit:
        if(len(f_name)==0):
            st.error("First name cannot be null")
        elif(len(s_address)==0):
            st.error("Address Cannot be null")
        elif(len(seller_id)==6):
            if(seller_id[0]==dairy_id[0] and seller_id[1]==dairy_id[1] and seller_id[2]==dairy_id[2]):
                if(len(ph_no)==10):
                    try:
                        c.execute('insert into seller (seller_id,f_name,l_name,s_address,contact_number,dairy_id) values (:1,:2,:3,:4,:5,:6)',(seller_id,f_name,l_name,s_address,int(ph_no),dairy_id))
                        con.commit()
                        if c.rowcount:
                            st.write("successful")
                    except ValueError as a:
                        st.error('Enter Phone number')
                    except cx_Oracle.DatabaseError as e:
                        st.write('Seller ID/ Dairy ID is Invalid')
                else:
                    st.error("Check Phone number")
            else:
                st.error("Seller ID and Dairy ID doesn't match")
        else:
            st.error("Invalid Seller ID")

    c.close()

def delete_seller(staff):
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    seller_id=st.text_input('Enter seller id whose details to be deleted',max_chars=6)
    submit=st.checkbox("Delete")
    if submit:
        if(staff[0:3]==seller_id[0:3]):
            out=c.execute('delete from seller where seller_id=:1',[seller_id])
            con.commit()
            if c.rowcount:
                st.write("successful")
                st.write(c.rowcount," fields deleted")
            else:
                st.write(" Please enter valid dairy Id")
                st.write(c.rowcount," fields deleted")
        else:
            st.error("Access Denied")

def update_seller(staff):
    my_seller_id=st.text_input('Enter seller id ',max_chars=6)
    submit=st.checkbox("submit")
    if submit:
        if(staff[0:3]==my_seller_id[0:3]):
            try:
                con=cx_Oracle.connect('shreesha/1204@localhost')
                c=con.cursor()
                c.execute("select * from seller where seller_id=:1",[my_seller_id])
                data=c.fetchall()
                list1=[]
                list1.append(data[0][1])
                list1.append(data[0][2])
                list1.append(data[0][3])
                list1.append(data[0][4])
                list1.append(data[0][5])
                f_name=st.text_input('First Name',list1[0],max_chars=10)
                l_name=st.text_input('Last Name',list1[1],max_chars=10)
                s_Address=st.text_area("Seller Address",list1[2],max_chars=30)
                ph_no=st.text_input('Contact Number',list1[3],max_chars=10)
                dairy_id=st.text_input('Dairy ID',list1[4],max_chars=3)
                submit1=st.checkbox("Update Changes")
                if submit1:
                    if(len(f_name)==0):
                        st.error("First name cannot be null")
                    elif(len(s_Address)==0):
                        st.error("Address Cannot be null")
                    elif(len(ph_no)==10):
                        if(my_seller_id[0]==dairy_id[0] and my_seller_id[1]==dairy_id[1] and my_seller_id[2]==dairy_id[2]):
                            try:
                                c.execute('update seller set  f_name=:2 ,l_name=:3, s_address=:4, contact_number=:5, dairy_id=:6   where seller_id=:1' ,(f_name,l_name,s_Address,int(ph_no),dairy_id,my_seller_id))
                                con.commit()
                                if c.rowcount:
                                    st.write("successful")
                                    st.write(c.rowcount," fields updated")
                            except ValueError as e:
                                st.error('Enter Phone Number')
                            except cx_Oracle.IntegrityError:
                                st.write('Invalid Dairy ID')
                            c.close()
                        else:
                            st.error("Dairy ID does not match")
                    else:
                        st.error("check phone number")
            except:
                st.error("No fields found")
        else:
            st.error("Access Denied")

def view_all_seller(staff):
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    view=0
    search=st.radio('Search by',('Seller ID','View all'))
    if search=='Seller ID':
        sid=st.text_input('Enter Seller Id')
        option=st.checkbox('submit')
        if option:
            c.execute('select * from seller where seller_id=:1 and dairy_id=:2',[sid,staff[0:3]])
            view=1
            data=c.fetchall()
    if search=='View all':
        c.execute("select * from seller where dairy_id=:1 ",[staff[0:3]])
        view=1
        data=c.fetchall()
    if view:
        if c.rowcount:
            list1=[]
            list2=[]
            list3=[]
            list4=[]
            list5=[]
            list6=[]
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
                list5.append(data[m][n])
                n+=1
                list6.append(data[m][n])
        else:
            st.error('No values found')
    try:
        df = pd.DataFrame({"seller ID": list1, "First Name": list2,"Last Name":list3,"Address":list4,"Contact Number":list5,"Dairy ID":list6})
        st.write(df)
    except:
        st.write()
    c.close()

def create_milk(staff):
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    seller_id=st.text_input("Enter Seller id here",max_chars=6)
    date_=date.today()
    milk_type=st.selectbox("Enter type of milk here",('None','Cow','Buffallo'))
    fat=st.text_input("Enter fat here",max_chars=5)
    quantity=st.text_input("Enter Quantity here",max_chars=10)
    submit=st.checkbox("Submit")
    if submit:
        A=0
        if milk_type=='Cow':
            if float(fat)<3.5:
                st.write('Fat content not satisfied')
                return
        elif milk_type=='Buffallo':
            if float(fat)<6.0:
                st.write('Fat content not satisfied')
                return
        price=(425/(1000/(10*float(fat))))*float(quantity)
        A=1
        if(seller_id[0:3]==staff[0:3]):
            try:
                if A:
                    c.execute('insert into milk (seller_id,date_of_purchase,type,fat,quantity,price) values (:1,:2,:3,:4,:5,:6)',(seller_id,date_,milk_type,float(fat),float(quantity),price))
                    c.callproc('INSERT_COLLECT',[staff,seller_id,date_])

                    A=0
                    if c.rowcount:
                        c.execute('select * from milk m   where m.seller_id=:1 and m.date_of_purchase=:2 ',(seller_id,date_))
                        data=c.fetchall()
                        list1=[]
                        list2=[]
                        list3=[]
                        list4=[]
                        list5=[]
                        list6=[]
                        print(list1)

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
                            list5.append(data[m][n])
                            n+=1
                            list6.append(data[m][n])
                        A=1
                        if A:
                            df = pd.DataFrame({"seller ID": list1, "Date": list2,"Type":list3,"Fat":list4,"Quantity":list5,"Price":list6})
                            st.write(df)
            except cx_Oracle.IntegrityError:
                st.error('Check Seller ID')
        else:
            st.error("Invalid seller ID")
        c.close()

def update_milk(staff):
    my_seller_id=st.text_input('Enter seller id ',max_chars=6)
    new_date=st.date_input('Date')
    submit=st.checkbox("submit")
    try:
        if submit:
            if(my_seller_id[0:3]==staff[0:3]):
                con=cx_Oracle.connect('shreesha/1204@localhost')
                c=con.cursor()
                c.execute("select * from milk where seller_id=:1 and date_of_purchase=:2",[my_seller_id,new_date])
                data=c.fetchall()
                list1=[]
                list1.append(data[0][2])
                list1.append(data[0][3])
                list1.append(data[0][4])
                milk_type=st.selectbox('Type',('Cow','Buffallo'))
                fat=st.text_input('Fat',list1[1],max_chars=5)
                quantity=st.text_input("Quantity",list1[2],max_chars=5)
                submit1=st.checkbox("Update Changes")
                if milk_type=='Cow':
                    if float(fat)<3.5:
                        st.write('Fat content not satisfied')
                        return
                elif milk_type=='Buffallo':
                    if float(fat)<6.0:
                        st.write('Fat content not satisfied')
                        return
                price=(425/(1000/(10*float(fat))))*float(quantity)
                if submit1:
                    c.execute('update milk set type=:1, fat=:2,quantity=:3,price=:4   where seller_id=:5 and date_of_purchase=:6' ,(milk_type,float(fat),float(quantity),price,my_seller_id,new_date))
                    con.commit()
                    if c.rowcount:
                        st.write("successful")
                        st.write(c.rowcount," fields updated")
                    else:
                        st.write("No fields updated")
                c.close()
            else:
                st.error("Access Denied")
    except:
        st.error('No fields found')


def view_milk(staff):
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    a=0
    search=st.radio('Search by',('Seller ID','Date','Seller ID and Date','View all'))
    if search=='Seller ID and Date':
        sid=st.text_input('Enter Seller Id')
        tdate=st.date_input('Enter date')
        option=st.checkbox('submit')
        if option:
            a=1
            if(sid[0:3]==staff[0:3]):
                c.execute('select * from milk m  , collect c where m.seller_id = c.seller_id and m.date_of_purchase=c.date_of_collect and m.seller_id=:1 and c.date_of_collect=:2',[sid,tdate])
            else:
                st.error("Access Denied")
    if search=='Date':
         tdate=st.date_input('Enter date')
         option=st.checkbox('submit')
         if option:
            a=1
            c.execute('select * from milk m , collect c, seller s where m.seller_id = c.seller_id and m.date_of_purchase=c.date_of_collect and c.date_of_collect=:1 and m.seller_id = s.seller_id and s.dairy_id=:2',[tdate,staff[0:3]])
    if search=='Seller ID':
        sid=st.text_input('Enter Seller Id')
        option=st.checkbox('submit')
        if option:
            a=1
            if(sid[0:3]==staff[0:3]):
                c.execute('select * from milk m , collect c where m.seller_id = c.seller_id and m.date_of_purchase=c.date_of_collect and m.seller_id=:1',[sid])
            else:
                st.error("Access Denied")
    if search=='View all':
        a=1
        id=staff[0:3]
        c.execute('select * from milk m , collect c,seller s where m.seller_id = c.seller_id and m.date_of_purchase=c.date_of_collect and m.seller_id = s.seller_id  and s.dairy_id=:1',[id])
    if a:
        data=c.fetchall()
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5=[]
        list6=[]
        list7=[]
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
            list5.append(data[m][n])
            n+=1
            list6.append(data[m][n])
            n+=1
            list7.append(data[m][n])
        view=st.checkbox("Fetch details")
        try:
            if view:
                df = pd.DataFrame({"seller ID": list1, "Date": list2,"Type":list3,"Fat":list4,"Quantity":list5,"Price":list6,"staff ID":list7})
                st.write(df)
        except:
            st.write("No value exists")
    c.close()

def create_buyer(staff):
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    date_=date.today()
    name=st.text_input('Enter the name')
    quantity=st.text_input("Enter Quantity here",max_chars=10)
    if quantity:
        price=float(quantity)*20
        if float(quantity)==0:
            st.error('enter valid quantity')
            return
    submit=st.checkbox("Submit")
    if submit:
        A=1
        if A:
            c.execute('insert into buyer (buyer_id,name,quantity,price) values(buyer_id.nextval,:1,:2,:3)',(name,float(quantity),float(price)))
            c.execute('select buyer_id from buyer')
            b_id=c.fetchall()
            id=b_id[-1][0]
            c.callproc('SELL',[staff,id,date_])
            if c.rowcount:
                c.execute('select * from buyer where buyer_id=:1',[id])
                data=c.fetchall()
                list1=[]
                list2=[]
                list3=[]
                list4=[]
                list5=[]
                list6=[]
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
                A=1
                if A:
                    df = pd.DataFrame({"Buyer ID": list1, "Name": list2,"Quantity":list3,"Price":list4})
                    st.write(df)
            con.commit()
            A=0
            if c.rowcount:
                st.write('successful')
            else:
                st.write('unsuccessful')
    c.close()


def view_buyer(staff):
    con=cx_Oracle.connect('shreesha/1204@localhost')
    c=con.cursor()
    a=0
    search=st.radio('Search by',('Date','View All'))
    if search=='Staff ID and Date':
        sid=st.text_input('Enter Staff Id')
        tdate=st.date_input('Enter date')
        option=st.checkbox('submit')
        if option:
            a=1
            c.execute('select * from buyer b  , sell_milk s where b.buyer_id=s.buyer_id and s.staff_id=:1 and s.date_of_sale=:2 ',[sid,tdate])
    if search=='Date':
         tdate=st.date_input('Enter date')
         option=st.checkbox('submit')
         if option:
            a=1
            c.execute('select * from buyer b  , sell_milk s ,staff st where b.buyer_id=s.buyer_id and s.date_of_sale=:2 and s.staff_id=st.staff_id and st.dairy_id=:1',[tdate,staff[0:3]])
    if search=='Staff ID':
        sid=st.text_input('Enter Staff Id')
        option=st.checkbox('submit')
        if option:
            a=1
            c.execute('select * from buyer b  , sell_milk s where b.buyer_id=s.buyer_id and s.staff_id=:1',[sid])
    if search=='Dairy ID':
        did=st.text_input('Enter Dairy ID')
        option=st.checkbox('submit')
        if option:
            a=1
            c.execute('select * from buyer b,sell_milk m,staff s where b.buyer_id=m.buyer_id and m.staff_id=s.staff_id and s.dairy_id=:1',[did])
    if search=='View All':
        a=1
        c.execute('select * from buyer b  , staff st ,sell_milk s where b.buyer_id=s.buyer_id and st.staff_id=s.staff_id and st.dairy_id=:1',[staff[0:3]])
    if a:
        data=c.fetchall()
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5=[]
        list6=[]
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
            list5.append(data[m][n])
            n+=2
            list6.append(data[m][n])
        view=st.checkbox("Fetch details")
        try:
            if view:
                df = pd.DataFrame({"Buyer ID": list1, "Name": list2,"Quantity":list3,"Price":list4,"Staff ID":list5,"Date":list6})
                st.write(df)
        except:
            st.write("No value exists")
    c.close()

def default(staff):
    table=st.selectbox('Enter the table',("None","Seller","Milk","Buyer"))
    if table=="Seller":
        count=5
        option=st.selectbox('Select the operation',('None','Enter New Seller Details','Delete Seller Details','Update Seller Details','View All Seller Details'),key=count)
        count+=1
        if option=='Enter New Seller Details':
            create_seller(staff)
        if option=='Delete Seller Details':
            delete_seller(staff)
        if option=='Update Seller Details':
            update_seller(staff)
        if option=='View All Seller Details':
            view_all_seller(staff)
    if table=="Milk":
        count=6
        option=st.selectbox('Select The Operation',('None','Enter New Details','Update  Details','View All  Details'),key=count)
        count+=1
        if option=="Enter New Details":
            create_milk(staff)
        if option=='Update  Details':
            update_milk(staff)
        if option=='View All  Details':
            view_milk(staff)
    if table=="Buyer":
        count=7
        option=st.selectbox('Select The Operation',('None','Enter New Details','View All  Details'),key=count)
        count+=1
        if option=="Enter New Details":
            create_buyer(staff)
        if option=='View All  Details':
            view_buyer(staff)