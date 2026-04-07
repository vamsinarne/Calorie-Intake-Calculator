import streamlit as st
import pandas as pd
import numpy as np

#Title
st.title("📊 Streamlit Calorie Intake App")

#Text
st.write("This is a simple Streamlit app deployed on Streamlit Cloud.")

#User input
name = st.text_input("Enter your name")

#gender input
gender=st.radio("Select your Gender",["Male","Female"])

#age input
age=st.slider("Select your age",1,100)

#height input
height=st.number_input("Select your height in cm",min_value=75.0,max_value=300.0,step=0.1)

#weight input
weight=st.number_input("Enter your weight in Kilograms",min_value=0.0,step=0.1)

#activity level
activity_level=st.selectbox("Select Activity Level",["Sedentary(0 days/week)","Light(1-2 days/week)","Moderate(3-5 days/week)","Active(6-7 days/week)","Very Active(2x/day)"])

#taking user input for weight loss goal
goal=st.selectbox("Enter your Weight Loss goal",["Maintain Weight","Normal Weight Loss","Extreme Weight Loss"])

#taking user input for weight loss commitment period
n=st.slider("Enter period of commitment in weeks",1,16)

#height in meters
h_in_m=height/100

#BMI calculation
bmi=weight/(h_in_m)**2

if st.button("Calculate"):
    #Displaying BMI value
    st.write(f"\nYour BMI is {bmi:.2f}\n")

    #BMI to fitness level display
    if bmi<18.5:
        st.write("You are Underweight!")
    elif 18.5<=bmi<=24.9:
        st.write("You have a healthy weight")
    elif 24.9<bmi<=29.9:
        st.write("You are Overweight")
    elif 29.9<bmi<=34.9:
        st.write("Obese (Class 1)")
    elif 34.9<bmi<=39.9:
        st.write("Obese (Class 2)")
    elif bmi>39.9:
        st.write("Severe Obesity")

    #Calculating Basic Metabolic Rate
    if gender=="Male":
        bmr= (10*weight)+(6.25*height)-(5*age)+5
    else:
        bmr= (10*weight)+(6.25*height)-(5*age)-161

    #storing activity multiplier values in a dictionary based on activity level
    activity_multiplier={"Sedentary(0 days/week)":1.2,"Light(1-2 days/week)":1.375,"Moderate(3-5 days/week)":1.55,"Active(6-7 days/week)":1.725,"Very Active(2x/day)":1.9}

    #accessing multiplier values based on the user input for activity level
    multiplier=activity_multiplier[activity_level]

    #Calculating Total Daily Energy Expenditure
    TDEE=bmr*multiplier

    #calorie calculator for different weight loss goals
    maintain=TDEE
    normal_loss=TDEE-500
    extreme_loss=TDEE-1000

    st.write(f"\nMaintain Weight: {maintain:.0f} Calories/day")
    st.write(f"\nNormal Weight Loss: {normal_loss:.0f} Calories/day")
    st.write(f"\nExtreme Weight Loss: {extreme_loss:.0f} Calories/day")

    #storing weight after every month in a dictionary
    n_weight={}
    if goal=="Maintain Weight":
        st.write(f"No change in weight after {n} weeks")
    elif goal=="Normal Weight Loss":
        for i in range(1,int(n)+1):
            k=weight-i*(0.5) #0.5kg/week
            n_weight[i]=k
    elif goal=="Extreme Weight Loss":
        for i in range(1,int(n)+1):
            k=weight-i*(1) #1kg/week
            n_weight[i]=k
    
    st.write(f"With a goal of {goal}")
    for k,v in n_weight.items():
        st.write(f"Weight after week {k} = {v} Kgs")
    data=pd.DataFrame(n_weight)
    st.subheader("Goal Chart")
    st.line_chart(data)







