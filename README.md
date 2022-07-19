# python-api-tests-sandbox

Playing with python, pytest, etc and send requests to [https://reqres.in] website.

## What?

This project is only an example that is covering the following concepts, principles and technologies.

Technologies:
- python (3.9)
- pytest
- tox
- docker

Principles and concepts:
- API Wrappers
- API Contracts
- Configuration File (YAML)
- Positive and negative testing
- Narrow or Broad Integration testing

## Who?

This project is mainly for my own usage but anybody who would like an example about using python to test APIs. This testing suite could be used to test either the application running in a `docker-compose` environment (narrow integration testing) or in a `cluster` (broad integration testing).

## How?

First thing is to clone the GitHub project on the local.

If python 3.9 is installed on the local:

```sh
py -3.9 -m pip install --upgrade pip
py -3.9 -m pip install tox
py -3.9 -m tox --recreate --
```

If python 3.9 isn't installed on the local, then docker can be used:

```sh
docker build -t python-api-tests-sandbox:local .
docker run -t python-api-tests-sandbox:local
```
