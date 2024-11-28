import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Customer Lifetime Value (CLV) Calculator")

# User Input
st.header("Input Customer Data")
avg_purchase_value = st.number_input("Average Purchase Value ($)", min_value=0.0)
avg_purchase_frequency = st.number_input("Average Purchase Frequency (per year)", min_value=0)
customer_lifespan = st.number_input("Customer Lifespan (years)", min_value=0)

# Calculate CLV
if st.button("Calculate CLV"):
    clv = avg_purchase_value * avg_purchase_frequency * customer_lifespan
    st.success(f"Customer Lifetime Value: ${clv:.2f}")

    # Visualization
    st.header("CLV Visualization")
    categories = ['Home Health', 'Primary Care', 'Pharmacy', 'Behavioral Health', 'Social Determinants of Health']
    values = [clv * np.random.uniform(0.8, 1.2) for _ in categories]  # Simulated values for visualization

    fig, ax = plt.subplots()
    ax.bar(categories, values)
    ax.set_ylabel('CLV ($)')
    ax.set_title('CLV by Product Category')
    st.pyplot(fig)

# Insights
st.header("Insights")
if clv > 1000:
    st.write("This customer is highly valuable!")
else:
    st.write("Consider strategies to increase customer value.")
