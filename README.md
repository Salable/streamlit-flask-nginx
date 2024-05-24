# Streamlit & Flask with Docker and nginx

This is an example of a Docker-based approach to running Streamlit and Flask together. The goal of this project is to showcase a few ways of running a Streamlit setup that has the ability to act as a free-standing API provider. 

Use this at your own risk!

Run this project with Docker!

`docker build -t st_app . && docker run -it -p 8080:8080 st_app`

The Streamlit app is located in `app/`, the Flask app is located in `api/`. Simply modify each of the `app.py` files to get started! The magic of this comes from the nginx proxy, and the configuration (inspired by https://github.com/lballore/streamlit-nginx). 

The requirements for Flask and Streamlit are shared, and you could presumably share local libraries/conf as well if desired.

Nginx can also act as a webserver, specifically for React applications. in the `web/` folder is a sample React application using `npx create-react-app`, modified to act in relative path mode (see `package.json` and the 'homepage' param), and mapped to the path `web/` in nginx. 

In streamlit we are embedding this as a iframe (using v1.components), but you can also run this as a standalone website. 