FROM python:3.12.3-slim-bullseye as dependencies


ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /opt/stactools-uci-cycling-races
COPY pyproject.toml ./
COPY src/stactools/uci_cycling_races/__init__.py src/stactools/uci_cycling_races/
RUN apt-get -y -q update \
    && apt-get -y -q install build-essential \
    && rm -rf /var/lib/apt/lists/ && \
    python -m venv /opt/venv && \
    pip install . &&\
    && ls /opt/venv \
    && rm -r /opt/venv/lib/python3.12/site-packages/stactools/uci_cycling_races


FROM dependencies as builder

ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /opt/stactools-uci-cycling-races
COPY --from=dependencies /opt/venv /opt/venv
COPY pyproject.toml ./
COPY src ./src
RUN pip install -U pip \
    && pip install .
WORKDIR /
RUN rm -rf /opt/stactools-uci-cycling-races
CMD [ "stac", "ucicyclingraces" ]


FROM dependencies as dev-dependencies

RUN apt-get update -q && \
    apt-get install -y -q --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /opt/stactools-uci-cycling-races
COPY --from=dependencies /opt/venv /opt/venv
COPY pyproject.toml .
RUN pip install -e '.[dev]' \
    && git init


FROM dev-dependencies as dev-builder

ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /opt/stactools-uci-cycling-races
COPY --from=dependencies /opt/venv /opt/venv
COPY . .
CMD [ "stac", "ucicyclingraces" ]
