FROM python:3.11.4-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive
ENV IS_BROWSER_INSIDE_CONTAINER=TRUE

RUN apt-get update && apt-get install -y --no-install-recommends \
    firefox-esr=102.13.0esr-1~deb12u1 \
    xvfb=2:21.1.7-3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt requirements.txt

RUN python -m venv .venv \
    && . .venv/bin/activate \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY ./lib ./lib
COPY ./configs ./configs
COPY ./features ./features

ENTRYPOINT ["bash"]

CMD ["-c", ". .venv/bin/activate && behave features/backend; behave features/frontend"]
