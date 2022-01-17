
# pip install ../pytest_system_test_plugin 

import logging
import os
import time
import pytest

CURL = "/usr/bin/curl -X POST http://localhost:{} -d hello_my_plugins"

import pytest


def test_go():
    pass

#def test_use_case_ry(process_factory):
#    # TODO: Find bette way of getting an interpreter in the current env
#     interpreter = os.path.abspath("./env-plugin/bin/python")
#     server = process_factory(
#         [
#             interpreter,
#             "-m",
#             "restapi_echo_server",
#             "--host",
#             "0.0.0.0",
#             "--port",
#             "8080",
#         ],
#         "server_",
#     )
#     server.run_bg()
#     assert server.get_status() == "Running"  # make sure it still runs
#     # give the server 100ms to start in the background
#     time.sleep(0.1)
#     client = process_factory(
#         CURL.format(8080).split(),
#         "client_",
#     )
#     client.run_bg()
#     assert client.get_status() == 0
#     server.kill()
#     assert server.get_status() == "NotExisting"
# 
#     # For weird reasons the echoserver logs to stderr
#     assert server.get_stdout() == ""
#     assert "hello_my_plugins" in server.get_stderr()
# 

def test_use_case_help(process_factory):

    help = process_factory(["tedge", "-V"])
    help.run()
    assert help.get_stdout() == "tedge 0.5.1"

