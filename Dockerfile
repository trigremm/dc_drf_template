# Dockerfile
FROM python:3.11.5-slim-bullseye

# Set the version of Poetry to install
ARG POETRY_VERSION=1.8.5

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libpq-dev \
        git \
        gcc \
        python3-dev \
        python3-pip \
        python3-cffi \
        libcairo2 \
        libcairo2-dev \
        libpango1.0-0 \
        libpangocairo-1.0-0 \
        libgdk-pixbuf2.0-0 \
        libffi-dev \
        shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"
COPY poetry.lock pyproject.toml ./

# Install project dependencies
RUN poetry install --no-dev --no-root

# make sure dirs exists
RUN mkdir -p static media logs

# Copy application code to container
COPY --chmod=755 entrypoint.sh /usr/local/bin/
COPY . .

# run app
EXPOSE 80
CMD [ "sh", "/usr/local/bin/entrypoint.sh" ]
