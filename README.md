# Streamlit & Flask with Docker and nginx

This is an example of a Docker-based approach to running Streamlit and Flask together. The goal of this project is to showcase a few ways of running a Streamlit setup that has the ability to act as a free-standing API provider. 

Use this at your own risk!

Run this project with Docker!

`docker build -t st_app . && docker run -it -p 8080:8080 st_app`