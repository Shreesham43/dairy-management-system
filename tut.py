import streamlit as st
import urllib.request
import webbrowser
import sqlite3
conn=sqlite3.connect('data.db')
c=conn.cursor

#headers and text
st.title("Login")

st.header("header")
st.subheader("subheader")

st.text("text")
st.markdown("markdown")

#colored message
st.success("successful")
st.warning("warning")
st.info("information")
st.error("error")

#error
st.exception("NameError('name three is not defined')")

#help python
st.help(range)

#checkbox
if st.checkbox("Show"):
    st.text("showing/hiding widget")

#radio
status=st.radio("What is your status",("Active","Inactive"))
if status=="Active":
    st.text("You are active")
else:
    st.text("you are inactive")

#selectbox
occupation=st.selectbox("Your Occupation",("--select--","programmer","datascientist","doctor","businessman"))
if occupation=="--select--":
    st.write("select your occupation")
else:
    st.write("you selected ",occupation)

#multiselect
location=st.multiselect("Select you work place",("London","New York","Mumbai"))
st.write("You selected ",len(location),"workplace")

#button
st.button("Simple Button")

if st.button("help"):
    webbrowser.open('https://www.google.com')

#textinput
name=st.text_input("Your name here")
if st.button("submit"):
    st.success(name)

#textarea
message=st.text_area("type something")
if st.button("Submit"):
    st.success(message)

import datetime
st.write("Today is",datetime.datetime.now())