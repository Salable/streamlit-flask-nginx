import streamlit as st
from streamlit_p5 import sketch
import random

st.title("Processing in Streamlit")
st.write("Check out some of the examples or create your own!")

value = sketch("""
let iter=0
function setup() {
    createCanvas(700, 500);
    noStroke();
    background(255)
}
function draw() {
    fill(random(255), random(255), random(255));
    if (iter===10) {   
        ellipse(random(width), random(height), 50, 50);
        iter=0
    }
    iter++
}
""", width=700, height=500)
