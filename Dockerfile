FROM python:3.9-bullseye

RUN groupadd -r python && useradd --no-log-init -r -g python python
USER python
WORKDIR /home/python

COPY --chown=python:python . /home/python

RUN pip install --upgrade pip
RUN pip install tox
RUN python -m tox --recreate --notest

ENTRYPOINT ["python", "-m", "tox", "--"]
CMD []
