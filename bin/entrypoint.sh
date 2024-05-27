#!/usr/bin/env bash

set -euo pipefail

readonly NGINX_CONFIG=/home/streamlitapp/.nginx/nginx.conf
readonly NGINX_P="/tmp/nginx.pid"

nginx -c "$NGINX_CONFIG" -p "$NGINX_P" -g "daemon off;" &
cd /home/streamlitapp/app/ && streamlit run streamlit-p5.py & 
wait