FROM python:3.12-slim

LABEL maintainer="Neal Riley <neal@salable.app>"

USER root

# Install dependencies and nginx
RUN apt-get -qq update && \
    apt-get -y install wget gnupg && \
    wget https://nginx.org/keys/nginx_signing.key && \
    cat nginx_signing.key | apt-key add - && \
    apt-get -qq update && \
    apt-get -y install nginx && \
    rm nginx_signing.key && \
    rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt --no-cache-dir --timeout 1000

# Create streamlitapp user
RUN useradd -m -u 1000 -d /home/streamlitapp streamlitapp
RUN chown -R streamlitapp /var/log/nginx /var/lib/nginx

# Config and exec files
COPY --chown=streamlitapp ./config/nginx /home/streamlitapp/.nginx/
COPY --chown=streamlitapp ./config/streamlit /home/streamlitapp/.streamlit/
COPY --chown=streamlitapp ./bin /home/streamlitapp/bin/
COPY --chown=streamlitapp ./app /home/streamlitapp/app/
COPY --chown=streamlitapp ./api /home/streamlitapp/api/

# Set Python paths
ENV PYTHONPATH "${PYTHONPATH}:/home/streamlitapp/src"
ENV PATH "${PATH}:/home/streamlitapp/src/bin:/home/streamlitapp/src/server/bin"

# Initialize Working dir and user
WORKDIR /home/streamlitapp/app
USER streamlitapp

ENTRYPOINT ["/home/streamlitapp/bin/start-nginx.sh"]