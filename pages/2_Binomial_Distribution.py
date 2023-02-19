import streamlit as st
import numpy as np
from math import comb
from matplotlib import pyplot as plt
from sys import float_info

st.set_page_config(page_title='Binomial Distribution')

st.title('Binomial Distribution')
st.subheader('by Ken Mueller')

parameters = st.radio('Parameters', ('n and π', 'μ and σ^2'))

left, right = st.columns(2)

if parameters == 'n and π':
    with left:
        max_n = st.number_input('Maximum n value', 1, value=100)
        n = st.slider('n', 0, max_n, value=int(max_n / 2))

    with right:
        p = st.slider('π', 0.0, 1.0, 0.5)
elif parameters == 'μ and σ^2':
    with left:
        mean = st.slider('μ', float_info.epsilon, 1.0, value=0.5)

    with right:
        max_variance = st.number_input('Maximum σ^2 value', 1, value=100)
        variance = st.slider('σ^2', 0.0, float(max_variance), value=50.0)

    p = 1 - variance / mean
    n = mean / p


def binomial(k):
    return comb(int(n), k) * p ** k * (1 - p) ** (n - k)


x = np.arange(0, 100, 1)
y = [binomial(k) for k in x]

plt.plot(x, y)
st.pyplot(plt.gcf())

st.latex(r'''
	\binom{%d}{k} \cdot %.3f^k \cdot (1 - %.3f)^{%.3f - k}
''' % (int(n), p, p, n))
