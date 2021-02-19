#!/usr/bin/env python
# coding: utf-8

# In[1]:


## importing the necessary libraries
import pandas as pd
import numpy as np
import pickle
import streamlit as st


# In[2]:


## loading the saved model

saved_model = pickle.load(open("final_model.pkl","rb"))


# In[3]:


def default_prediction(features):
    
    features = np.array(features).astype(np.float64).reshape(1,-1)
    
    prediction = saved_model.predict(features)
    probability = saved_model.predict_proba(features)
    
    return prediction,probability
    


# In[4]:


def main():
    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <center><h1>Credit Card Default Prediction App</h1></center>
    </div><br>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    LIMIT_BAL = st.text_input("Enter Limit Balance in NT Dollar")
    
    education_status = ["Graduate school", "University", "High School", "Others"]
    
    marital_status = ["Married","Single", "Others"]
    
    payment_status = [
        "Zero balance account, and credit never used",
        "Account with balance and was paid in full",
        "Minimum payment was made, but the entire balance wasn't paid",
        "Payment delay for 1 month",
        "Payment delay for 2 month",
        "Payment delay for 3 month",
        "Payment delay for 4 month",
        "Payment delay for 5 month",
        "Payment delay for 6 month",
        "Payment delay for 7 month",
        "Payment delay for 8 month",   
    ]
    
    EDUCATION = education_status.index(st.selectbox(
        "Select Education Level",
        tuple(education_status)
    )) + 1
    
    MARRIAGE = marital_status.index(st.selectbox(
        "Select Marital Status",
        tuple(marital_status)
    )) + 1
    
    AGE = st.text_input("Age (in Years)")
    
    PAY_1 = payment_status.index(st.selectbox( 
        "Select last month payment status",
        tuple(payment_status)
    )) - 2
    
    BILL_AMT1 = st.text_input("Last month Bill Amount in NT dollar")
    BILL_AMT2 = st.text_input("Last 2nd month Bill Amount NT dollar)")
    BILL_AMT3 = st.text_input("Last 3rd month Bill Amount NT dollar)")
    BILL_AMT4 = st.text_input("Last 4th month Bill Amount NT dollar)")
    BILL_AMT5 = st.text_input("Last 5th month Bill Amount NT dollar)")
    BILL_AMT6 = st.text_input("Last 6th month Bill Amount NT dollar)")

    PAY_AMT1 = st.text_input("Amount paid in Last Month (NT) dollar)")
    PAY_AMT2 = st.text_input("Amount paid in Last 2nd month (NT) dollar)")
    PAY_AMT3 = st.text_input("Amount paid in Last 3rd month (NT) dollar)")
    PAY_AMT4 = st.text_input("Amount paid in Last 4th month (NT) dollar)")
    PAY_AMT5 = st.text_input("Amount paid in Last 5th month (NT) dollar)")
    PAY_AMT6 = st.text_input("Amount paid in Last 6th month (NT) dollar)")
    
    if st.button("Predict"):
            features = [LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]
            prediction, probability = default_prediction(features)
            
            if prediction[0] == 1:
            # counselling_html = """
            #     <div style = "background-color: #4f8bf9; font-weight:bold;padding:10px;border-radius:7px;">
            #         <p style = 'color: #721c24;'>This account will be defaulted with a probability of {round(np.max(probability)*100, 2))}%.</p>
            #     </div>
            # """
            # st.markdown(counselling_html, unsafe_allow_html=True)
                st.success("This account will be defaulted with a probability of {}%.".format(round(np.max(probability)*100, 2)))
            
            else:
                st.success("This account will not be defaulted with a probability of {}%.".format(round(np.max(probability)*100, 2)))
                # counselling_html = """
                #     <div style = "background-color: #4f8bf9; font-weight:bold;padding:10px;border-radius:7px;">
                #         <p style = 'color: ;'>This account will be defaulted with a probability of {round(np.max(probability)*100, 2))}%.</p>
                #     </div>
                # """
                # st.markdown(counselling_html, unsafe_allow_html=True)
                
    html_temp = """
    <div style = "padding: 10px;">
    <center><h2> Made with <span style="font-size:100%;color:red;">&hearts;</span> by </h2>
    <b><i>Abhishek Dubey<span style="font-size:100%;</span></i><b></center>
    </div><br>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
                

if __name__ == '__main__':
    main()

