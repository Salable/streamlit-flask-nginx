import streamlit as st
from streamlit_p5 import sketch
st.title("Sending data from Streamlit to Processing")

"""
With the power of Streamlit components, you can share data between Streamlit and Processing. Passing data is as easy as supplying a `data` parameter to the `sketch` function. This can be a static variable, or one that is returned from a Streamlit function (e.g. st.text_input())

```python
import streamlit as st
from streamlit_p5 import sketch

data_to_pass=st.text_input('Pass along a message')
value = sketch('''
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
''')
"""
st.header("Try it out!")
data_to_pass=st.text_input('Pass along a message')
value = sketch('''
let word=""
function setup() { 
  createCanvas(700, 500);
  word=dataToPass
}
function draw() {
    background(204, 120);
    fill(0)
    textFont('Courier New')
    textSize(50)
    if (word==="") {
      textSize(12)
      text("Type something in the input box", width/2, height / 2)
    } else {
      text(word, mouseX, mouseY)
    }
}
''', data=data_to_pass, width=700, height=500)