#!/usr/bin/env bash

set -euo pipefail

readonly NGINX_CONFIG=/home/streamlitapp/.nginx/nginx.conf
readonly NGINX_P="/tmp/nginx.pid"

echo "$@"
nginx -c "$NGINX_CONFIG" -p "$NGINX_P" -g "daemon off;" &
cd /home/streamlitapp/api/ && python app.py & 
cd /home/streamlitapp/app/ && streamlit run app.py & 
wait