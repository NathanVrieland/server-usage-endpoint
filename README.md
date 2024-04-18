# Server Usage Endpoint

a simple API endpoint for monitoring your server CPU and RAM usage

## Deployment
### I have only tested this on linux
- clone the repo

`$ git clone https://github.com/NathanVrieland/server-usage-endpoint.git`
- cd into directory

`$ cd server-usage-endpoint`
- make a virtual environment

`$ python3 -m venv venv`
- install dependencies

`$ pip install -r requirments.txt`
- run the server

`$ flask --app WSGI run --host <your host, 0.0.0.0 to bind to all addresses> --port <your port>`

### optionally run the server with a WSGI server

`$ pip install gunicorn`

`$ gunicorn WSGI:app -b <your host>:<your port>`
