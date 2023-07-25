import streamlit as st
import numpy as np
import pandas as pd


st.title('Intoduced you one of the best Anime in the universe')
st.header('One Piece')
st.subheader('This article is about the manga series. For the anime series adaptation, see One Piece (TV series).')
st.markdown('One Piece is a Japanese manga series written and illustrated by Eiichiro Oda.')
st.success("Success : If you have read this much then, it means now you are ready to be king of the Pirates")
st.info("Information : Mugiwara")
st.warning("Be Aware : Monkey D. Dragon better known as Dragon the Revolutionary and labelled as The Worlds Worst's Criminal in One Piece.")
st.error('Error: Buggy the Star Clown is the captain of the Buggy Pirates as well as the co-leader of the Buggy and Alvida Alliance, and a former apprentice of the Roger Pirates')
exp=ZeroDivisionError("!!!!!No one can kill LUFFY!!!!!!")
st.write(exp)
#st.help("Someone please help GARP!!!")
st.write("Till Epsoides -> Range(1,1070)")
st.write(1+2+3+4)
st.write("x=10\n"
        "for i in range (1,10):\n"
        "\tprint(i)")
st.write("range(1,10)")                                 
st.write(range(1,10))
st.write(1*2*3)

#-------------------------------------------------IMPORTANT--------------------------------------------

st.subheader("Select your 3 Favourite Character")

st.checkbox("Luffy")
st.checkbox("Zoro")
st.checkbox("Sanji")
st.checkbox("Chhoper")
st.checkbox("Nami")
st.checkbox("Franky")
st.checkbox("Brook")
st.checkbox("Usopp")

if(st.checkbox("Robin")):
    st.write("You have a very Seductive Taste!!")


st.subheader("Select your 3 Favourite Crew")
Selectk=st.radio("select : ",("Luffy Crew"," Revolutionary Army","Navy", "WhiteBeard","BlackBeard"))
if(Selectk == "Luffy Crew"):
    st.write("The Straw Hat Pirates, also known as the Mugiwara Pirates, Straw Hat Crew or simply the Straw Hats, are a very infamous and powerful pirate crew that originated from the East Blue.")
elif(Selectk == " Revolutionary Army"):
    st.write("The Revolutionary Army is an extremely powerful military organization led by Monkey D. Dragon")
elif(Selectk == "Navy"):
    st.write("Marines are allowed to wield whatever weapon they are most comfortable with, no matter how unusual they may be")
elif(Selectk == "WhiteBeard"):
    st.write("Edward Newgate, more commonly known as Whitebeard, was the captain of the Whitebeard Pirates and was widely known as the Strongest Man in the World")
elif(Selectk == "BlackBeard"):
    st.write("Marshall D. Teach, most commonly referred to by his epithet Blackbeard, is the captain-turned-admiral of the Blackbeard Pirates, and one of the Four Emperors. ")


st.subheader('Devil Fruit You Want To Eat') 

Fruit =  st.selectbox("Devil Fruits : ", [  'Gura no Mi', 'Gura Gura no Mi','Mera Mera no Mi',
                                                'Soru Soru no Mi','Uta Uta no Mi',
                                                'Bari Bari no Mi','Mane Mane no Mi'])
st.write("You've selected : ", Fruit)

st.subheader('Multiple Devil Fruit You Want To Eat') 

Fruit =  st.multiselect("Devil Fruits : ", [  'Gura no Mi', 'Gura Gura no Mi','Mera Mera no Mi',
                                                'Soru Soru no Mi','Uta Uta no Mi',
                                                'Bari Bari no Mi','Mane Mane no Mi'])
st.write("You've selected : ", len(Fruit),Fruit)

st.subheader('Click Here! If You Are Still Scrolling') 


if(st.button("Onii Chan!")):
    st.write("Yademe Kudasai!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Aha")


st.subheader('Rate Me') 
rate=st.slider("Rate Your Experiance: ",1,10,step=1)
if (rate >=7):
    st.write("You Got Robin")
elif(rate <=5):
    st.write("Come On Bro Raise The Bar !!!")
else:
    st.write("Thank You So Much!")

st.subheader("!------Crew Join'in Form----!")                              
username = st.text_input('Username : ')
password = st.text_input('Password : ', type = 'password')
st.button("Join!")


st.subheader("Why we Should Hire You?")


st.text_area("")
st.button("That is why you should hire me!")


st.subheader("Age")

Age= st.number_input("Your Should be Alive! Your Age :",7,110)
st.write(Age)

st.subheader("Match Your Date of Birth with One Piece Characters")

dob=st.date_input("This is the time ... Push Pass Your limit")
st.write(dob)




