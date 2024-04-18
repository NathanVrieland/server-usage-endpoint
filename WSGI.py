from flask import Flask, request, abort
import psutil
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route("/")
def return_sysinfo():
    if request.args.get("key") == os.environ.get("apikey"):
        return {
            "cpu":psutil.cpu_percent(interval=1),
            "cpucores":psutil.cpu_percent(interval=1, percpu=True),
            "memory":psutil.virtual_memory().percent
        }
    else:
        abort(403)
