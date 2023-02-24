import streamlit as st
import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt
from sys import float_info
from math import sqrt

st.set_page_config(page_title='Beta Distribution')

st.title('Beta Distribution')
st.subheader('by Ken Mueller')

top_left, top_right = st.columns(2)

with top_left:
    parameters = st.radio(
        'Parameters', ('a and b', 'μ and κ', 'ω and κ', 'μ and σ'))

left, right = st.columns(2)

if parameters == 'a and b':
    with left:
        max_a = st.number_input('Maximum a value', 1, value=100)
        a = st.slider('a', 0, max_a, value=int(max_a / 2))

    with right:
        max_b = st.number_input('Maximum b value', 1, value=100)
        b = st.slider('b', 0, max_b, value=int(max_a / 2))
elif parameters == 'μ and κ':
    with left:
        mean = st.slider('μ', 0.0, 1.0, value=0.5)

    with right:
        max_concentration = st.number_input('Maximum κ value', 1, value=100)
        concentration = st.slider(
            'κ', 0, max_concentration, value=int(max_concentration / 2))

    a = mean * concentration
    b = (1 - mean) * concentration
elif parameters == 'ω and κ':
    with left:
        mode = st.slider('ω', 0.0, 1.0, value=0.5)

    with right:
        max_concentration = st.number_input('Maximum κ value', 1, value=100)
        concentration = st.slider(
            'κ', 0, max_concentration, value=int(max_concentration / 2))

    a = mode * (concentration - 2) + 1
    b = (1 - mode) * (concentration - 2) + 1
elif parameters == 'μ and σ':
    with left:
        mean = st.slider('μ', 0.0, 1.0, value=0.5)

    with right:
        standard_deviation = st.slider(
            'σ', float_info.epsilon, 1.0, value=0.05)

    a = mean * (mean * (1 - mean) / standard_deviation ** 2 - 1)
    b = (1 - mean) * (mean * (1 - mean) / standard_deviation ** 2 - 1)

with top_right:
    st.latex(r'''
        \begin{align*}
            a &= %.3f \\
            b &= %.3f \\
            \mu &= %.3f \\
            \omega &= %.3f \\
            \kappa &= %.3f \\
            \sigma &= %.3f
        \end{align*}
    ''' % (
        a,  # a
        b,  # b
        a / (a + b),  # mean
        (a - 1) / (a + b - 2),  # mode
        a + b,  # concentration
        sqrt((a * b) / ((a + b) ** 2 * (a + b + 1)))  # standard deviation
    ))


def beta_numerator(theta):
    return theta ** (a - 1) * (1 - theta) ** (b - 1)


def beta_denominator():
    return integrate.quad(beta_numerator, float_info.epsilon, 1 - float_info.epsilon)[1]


def beta(theta):
    return beta_numerator(theta) / beta_denominator()


x = np.linspace(float_info.epsilon, 1 - float_info.epsilon, 500)
y = [beta(theta) for theta in x]

plt.plot(x, y)
st.pyplot(plt.gcf())

st.latex(r'''
	\frac{\theta^{%.3f - 1} \cdot (1 - \theta)^{%.3f - 1}}{\int_0^1 \theta^{%.3f - 1} \cdot (1 - \theta)^{%.3f - 1} d\theta} = \frac{\theta^{%.3f - 1} \cdot (1 - \theta)^{%.3f - 1}}{%s}
''' % (a, b, a, b, a, b, beta_denominator()))
