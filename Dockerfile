# Use a more specific base image
FROM python:3.11

ENV DEBIAN_FRONTEND noninteractive
ENV GECKODRIVER_VER v0.33.0 
ENV FIREFOX_VER 108.0 
ENV POETRY_VERSION=1.6.1 
ENV POETRY_HOME=/opt/poetry 
ENV POETRY_VENV=/opt/poetry-venv 
ENV POETRY_CACHE_DIR=/opt/.cache


ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# FROM python-base as poetry-base

RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends curl \
#     && curl -sSL https://install.python-poetry.org | python3 -

# FROM poetry-base as sber-app

ENV PATH="${PATH}:${POETRY_VENV}/bin"

RUN set -x \
   && apt update \
   && apt upgrade -y \
   && apt install -y \
       firefox-esr

RUN set -x \
   && apt install -y \
       libx11-xcb1 \
       libdbus-glib-1-2 \
   && curl -sSLO https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VER}/linux-x86_64/en-US/firefox-${FIREFOX_VER}.tar.bz2 \
   && tar -jxf firefox-* \
   && mv firefox /opt/ \
   && chmod 755 /opt/firefox \
   && chmod 755 /opt/firefox/firefox

RUN set -x \
   && curl -sSLO https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VER}/geckodriver-${GECKODRIVER_VER}-linux64.tar.gz \
   && tar zxf geckodriver-*.tar.gz \
   && mv geckodriver /usr/bin/

WORKDIR /app

COPY poetry.lock pyproject.toml ./

# RUN poetry check

# RUN poetry install 

# COPY . /app
# Install Python dependencies using Poetry
RUN poetry export -f requirements.txt --output requirements.txt \
    && pip install --no-cache-dir -r requirements.txt

# # Add geckodriver
# RUN curl -sSL https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VER/geckodriver-$GECKODRIVER_VER-linux64.tar.gz | tar xz -C /usr/local/bin

COPY . /app

CMD ["poetry", "run", "python", "-m", "./bot_run.py"]
