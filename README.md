PIE (Personal Information Eraser)
==============================
*Let's bake!*
<img src='media/pie-logo.png'>

A GenAI-based API micro-services to remove PII (Person identifiable Information) from text. Wrapped in a half-baked allegory.

## Example
This is an example of local use. Serving directly through fastapi is preferable.
``` python
from pie import Pie

text = "hej, jeg hedder Martin, jeg bor på Skiltevej"

pie = Pie()

pie.bake(text)
# 'hej, jeg hedder {PERSON}, jeg bor på {LOCATION}'
```


## Get started
TBA

### Run as docker container.
Install [`docker`](https://docs.docker.com/get-docker/). Then run
```
docker compose up --build
```

### Run locally
TBA
