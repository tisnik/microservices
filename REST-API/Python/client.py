import time

import requests
from requests_futures.sessions import FuturesSession

worker_count = 10
session = FuturesSession(max_workers=worker_count)


def test(session):

    for i in range(10):
        session.get(url="http://localhost:8080/api/v1/liveness")

    print(requests.get(url="http://localhost:8080/api/v1/liveness"))

    for i in range(10):
        session.get(url="http://localhost:8080/api/v1/liveness")


test(session)
print("About to exit???")
