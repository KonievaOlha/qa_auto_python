import pytest
import sqlite3


@pytest.fixture(scope="class")
def base_fixture():
    print("Setup")
    connection = sqlite3.connect("C:\Works\Study_qa_auto\qa_auto_python\lesson_31_SQL\carssbase.db",
                                 isolation_level=None)
    cursor = connection.cursor()
    base = ("C:\Works\Study_qa_auto\qa_auto_python\lesson_31_SQL\carssbase.db")
    yield cursor, connection, base
    print("Teardown")
    cursor.close()
    connection.close()

# import pytest
# import requests
#
#
# @pytest.fixture(scope="session")
# def postman_request():
#     # setup start  ---------------------
#     print("Setup")
#     url = "https://postman-rest-api-learner.glitch.me//info"
#     payload = {"name": "Add your name in the body"}
#     response = requests.request("POST", url, json=payload)
#     # setup end ---------------------
#     # func start -------------
#     yield response
#     # func end -------------
#     # teardown start ------
#     print("Teardown")
#     # teardown end ------
