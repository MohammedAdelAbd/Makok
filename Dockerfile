FROM python:3.14-slim
WORKDIR /opt/makok

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .
ENV CORESETTINGS_IN_DOCKER True

RUN set -ex && \
    apt-get update &&\
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        && pip install virtualenvwrapper poetry \
        && apt-get autoremove -y \
        && apt-get clean -y \
        && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY ["README.md", "Makefile", "manage.py", "./"]
COPY core core
COPY local local
COPY makok_backend makok_backend

EXPOSE 8000

COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
