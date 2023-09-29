PIE (Personal Information Eraser)
==============================

<img src='media/pie-logo.png' width="200"/>

A GenAI-based API micro-services to remove PII (Personally Identifiable Information) from text. Wrapped in a half-baked allegory.

## Example
This is an example of local use. Serving directly through fastapi is preferable.
``` python
from pie import Pie

text = "hej, jeg hedder Martin, jeg bor på Skiltevej"

pie = Pie()

pie.bake(text)
# 'hej, jeg hedder {PERSON}, jeg bor på {LOCATION}'
```

## Getting started
Create a `config.cfg` file in the root directory. Make the necessary adjustments to pie/filling.py.Note that the current system is set up to use OpenAI. Please do not remove the OpenAI


## Changing the LLM
The LLM specification is found in `pie/filling.py` and in your config.cfg. If changing the LLM, please do not remove the OpenAI implementation. Instead, add your own implementation and update the `pie/filling.py` to use your implementation.

### Run as docker container.
Install [`docker`](https://docs.docker.com/get-docker/). Then run
```
docker compose up --build
```

### Run locally
TBA
