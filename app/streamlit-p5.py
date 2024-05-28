import streamlit as st
from streamlit_p5 import sketch
import random

st.title("streamlit-p5")
st.write("Building interactive data apps, experiences, and visualizations with Processing.org and Streamlit")

value = sketch("""
let iter=0
function setup() {
    createCanvas(700, 500);
    noStroke();
    background(14, 17, 23)
}
function draw() {
    fill(random(255), random(255), random(255));
    if (iter===9) {   
        size=random(10, 50)
        ellipse(random(width), random(height),size,size );
        iter=0
    }
    iter++
}
function mousePressed() {
    background(14, 17, 23)
}
""", width=700, height=500)

st.header("Streamlit and Processing together at last")

"""Both Streamlit and Processing excel in their own areas, but together they compliment each other perfectly. Streamlit, and the power of Python (and integrations with Snowflake, for example), can do some awesome things with relatively minimal code. Processing does the same, with an awesome interactive capability, driven by Javascript, the HTML canvas, and a library called P5.js."""

with st.sidebar:
    st.header("Links")

    st.write("""
    - [pypi.org/project/streamlit-p5](https://pypi.org/project/streamlit-p5/)
    - [github.com/salable/streamlit-p5](https://github.com/salable/streamlit-p5)
    """)

st.header("What is Processing?")

"""Processing (also known as Processing.org, P5, or P5.js) started as the brainchild of Ben Fry and Case Reas. Back in the early 2000s this manifest itself as a Java applet and language base, but has grown over the years. Check them out at [Processing.org](https://www.processing.org) and the Javascript/HTML5 offshot [P5.js](https://p5js.org/).

Processing made its mark by being very easy and intuitive to get started, yet powerful enough to power complex visualisations and interactive experiences. With Streamlit and Processing together, the possiblities are endless!"""

st.header("How do I get started?")

"""Head over to [Getting Started](/%28doc%29_getting_started) to get started with your first sketch. From there, you can explore the other examples in the documentation, and start building your own interactive data apps, experiences, and visualizations with Processing and Streamlit!"""

