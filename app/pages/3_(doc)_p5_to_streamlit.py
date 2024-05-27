import streamlit as st
from streamlit_p5 import sketch
st.title("Sending data from Processing to Streamlit")

"""
With the power of Streamlit components, you can share data between Processing and Streamlit. The return value of the 'sketch' function can be called at any time using the function `sendDataToPython()`.

```python
import streamlit as st
from streamlit_p5 import sketch

value = sketch('''
let word=""
function setup() { 
  createCanvas(700, 300);
  noStroke(); 
  sendDataToPython({
    value: {
      mouseX: 0,
      mouseY: 0
    },
    dataType: "json",
  })
}
function draw() {
  background(14, 17, 23)
  ellipse(mouseX, mouseY, 30, 30)
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
''', width=700, height=300)
"""
st.header("Try it out!")
value = sketch('''
let word=""
function setup() { 
  createCanvas(700, 300);
  noStroke(); 
  sendDataToPython({
    value: {
      mouseX: 0,
      mouseY: 0
    },
    dataType: "json",
  })
}
function draw() {
  background(14, 17, 23)
  ellipse(mouseX, mouseY, 30, 30)
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
''', width=700, height=300)

st.slider('Mouse X', 0, 700, value['mouseX'])
st.slider('Mouse Y', 0, 300, value['mouseY'])
 
st.write(value)