import streamlit as st
from streamlit_p5 import sketch
import random

st.title("Processing in Streamlit")
st.write("Getting started with Processing and Streamlit was never easier! Have a play with the embedded examples, or create your own!")

data_to_pass=st.text_input('Pass along a message')
value = sketch("""
let word=""
function setup() { 
  createCanvas(700, 500);
  noStroke();
  word=dataToPass.name
    sendDataToPython({
        value: {
        mouseX: 0,
        mouseY: 0
        },
        dataType: "json",
    })
}

function draw() {
  background(204, 120);
  fill(0)
  textFont('Courier New')
  textSize(50)
  if (word==="") {
    textSize(12)
    text("Type something in the input box, click to send mouse pos to Streamlit", 0, height / 2)
  } else {
    text(word, mouseX, mouseY)
  }
}

function mousePressed() {
  sendDataToPython({
        value: {
        mouseX: mouseX,
        mouseY: mouseY
        },
        dataType: "json",
    })
}
""", data={
  "name" : data_to_pass
}, width=700, height=500)
st.write(value)
st.write("*Code:*")
st.code("""
let word=""
function setup() { 
  createCanvas(700, 500);
  noStroke();
  word=dataToPass.name
    sendDataToPython({
        value: {
        mouseX: 0,
        mouseY: 0
        },
        dataType: "json",
    })
}

function draw() {
  background(204, 120);
  fill(0)
  textFont('Courier New')
  textSize(50)
  if (word==="") {
    textSize(12)
    text("Type something in the input box, click to send mouse pos to Streamlit", 0, height / 2)
  } else {
    text(word, mouseX, mouseY)
  }
}

function mousePressed() {
  sendDataToPython({
        value: {
        mouseX: mouseX,
        mouseY: mouseY
        },
        dataType: "json",
    })
}
""")
