import numpy as np
import math
import streamlit as st

with st.sidebar:
    option_type = st.radio('Option Type', ['c', 'p'])
    
    stock_price = st.number_input('Enter stock price', min_value=0.1, step=0.1)
    strike_price = st.number_input('Enter strike price', min_value=0, step=20)
    days_to_expire = st.slider('Number of days to expire', value=1, min_value=1, max_value=30, step=1)
    interest_rate = st.number_input('Risk Free interest rate')
    hist_vol = st.number_input('Hist vol', min_value=0.01, step=0.001)
    num_reps = st.number_input('Enter number of reps', min_value=1000, step=500)
    
    maturity = days_to_expire/252
    
    
def mc_euro_options(option_type,stock_price,strike,maturity,interest_rate,hist_vol,num_reps):
    payoff_sum = 0
    for j in range(num_reps):
        price = stock_price
        price = price*math.e**((interest_rate-0.5*hist_vol**2)*maturity + hist_vol*np.sqrt(maturity)*np.random.normal(0, 1))
        if option_type == 'c':
            payoff = max(0,price-strike)
        elif option_type == 'p':
            payoff = max(0,strike-price)
        payoff_sum += payoff
    premium = (payoff_sum/float(num_reps))*math.e**(-interest_rate*maturity)
    return premium


option_premium = mc_euro_options(option_type,stock_price,strike_price,maturity,interest_rate,hist_vol,num_reps)  

st.write('Option Premium according to Monte Carlo method:')
st.write(option_premium)
 
