# HSA8
Web servers caching

You can access 3 images:
- Cat: `http://localhost:8080/cat`
- Dog: `http://localhost:8080/dog`
- Rabbit: `http://localhost:8080/rabbit`

Also, you can request current datetime at `http://localhost:8080/datetime`

For each GET and HEAD request with status codes 200, 301, 302, and 304, Nginx caching response for 1h
For other responses, NGINX caching response for 5m
