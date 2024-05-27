import streamlit as st
from streamlit_p5 import sketch 

st.title("Getting started")

"""
streamlit-p5 brings together two awesome platforms, [Streamlit](https://www.streamlit.io) and [Processing](https://www.processing.org).
Specifically, this module uses Processing in Javascript (aka, [p5.js](https://p5js.org/)), and the power of the Streamlit custom component.

Getting started is easy! Just install the library: 
```sh
pip install streamlit_p5 streamlit
```
and create your first sketch: 
```python
import streamlit as st
from streamlit_p5 import sketch

response=sketch('''
let rad = 60; // Width of the shape
let pos = 1; // Speed of the shape   
function setup() {
    createCanvas(700, 100)
}
function draw() {
    background(14, 17, 23)
    if (mouseIsPressed) {
        fill(246,118,90)
        for (let i = 0; i < 50; i++) {
            for (let j = 0; j < 50; j++) {
                ellipse(mouseX + i * 30, mouseY, 20, 20)
                ellipse(mouseX - i * 30, mouseY, 20, 20)
                ellipse(mouseX , mouseY+ i * 30, 20, 20)
                ellipse(mouseX, mouseY - i * 30, 20, 20)
            }
        }
    }
    else {
        fill(246,118,90)
        ellipse(mouseX, mouseY, 30, 30)
        
    }
    fill(255)
    ellipse(mouseX, mouseY, 20, 20)
    
}
''', width: 700, height: 100)
```
"""
st.header("Try it out!")
response=sketch(
'''
let rad = 60; // Width of the shape
let pos = 1; // Speed of the shape   
function setup() {
    createCanvas(700, 100)
}
function draw() {
    background(14, 17, 23)
    if (mouseIsPressed) {
        fill(246,118,90)
        for (let i = 0; i < 50; i++) {
            for (let j = 0; j < 50; j++) {
                ellipse(mouseX + i * 30, mouseY, 20, 20)
                ellipse(mouseX - i * 30, mouseY, 20, 20)
                ellipse(mouseX , mouseY+ i * 30, 20, 20)
                ellipse(mouseX, mouseY - i * 30, 20, 20)
            }
        }
    }
    else {
        fill(246,118,90)
        ellipse(mouseX, mouseY, 30, 30)
        
    }
    fill(255)
    ellipse(mouseX, mouseY, 20, 20)
    
}
''', width=700, height=100)

st.write("Simply supply any p5 compatible script, including setup, draw, mousePressed and other built-in functions! streamlit-p5 picks up the script and executes it in an html frame.")

st.header("Get started with p5.js")

st.write("There are a wealth of resources to get you started:")

"""
- https://p5js.org/reference/
- https://p5js.org/examples/
"""