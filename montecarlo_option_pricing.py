import numpy as np
import math
import streamlit as st

with st.sidebar:
    option_type = st.radio('Option Type', ['Call', 'Put'])
    stock_price = st.text()
    strike_price = st.text()
    days_to_maturity = st.text()
    interest_rate = st.text()
    hist_vol = st.text()
    num_reps = st.text()
    
maturity = days_to_maturity/252
    
    
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
    premium = (payoff_sum/float(num_reps))*math.e**(-r*maturity)
    return premium
