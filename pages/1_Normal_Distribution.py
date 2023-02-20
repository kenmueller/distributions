import streamlit as st
import numpy as np
from math import sqrt, pi, e
from matplotlib import pyplot as plt
from sys import float_info

st.set_page_config(page_title='Binomial Distribution')

st.title('Binomial Distribution')
st.subheader('by Ken Mueller')

left, right = st.columns(2)

with left:
    max_mean = st.number_input('Maximum μ value', 1, value=50)
    mean = st.slider('μ', -float(max_mean), float(max_mean), value=0.0)

with right:
    max_variance = st.number_input('Maximum σ^2 value', 1, value=100)
    variance = st.slider('σ^2', 0.0, float(
        max_variance), value=max_variance / 2)

std = sqrt(variance)


def normal(x):
    return 1 / (std * sqrt(2 * pi)) * e ** (-0.5 * ((x - mean) / std) ** 2)


x = np.arange(mean - 50, mean + 50, 1)
y = [normal(x) for x in x]

plt.plot(x, y)
st.pyplot(plt.gcf())

st.latex(r'''
	\frac{1}{%.3f \sqrt{2 \pi}} e^{-\frac{1}{2}\left(\frac{x - %.3f}{%.3f}\right)^2}
''' % (std, mean, std))
