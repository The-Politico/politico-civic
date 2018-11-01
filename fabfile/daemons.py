import requests
import server_config
import sys

from fabric.api import task
from time import sleep, time


@task
def bake():
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)


def main():
    start = 0

    while True:
        now = time()

        if (now - start) > server_config.LAMBDA_RESULTS_INTERVAL:
            start = now
            r = requests.get(server_config.LAMBDA_ENDPOINT)
            print(r.text)

            sleep(1)
