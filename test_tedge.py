
# pip install ../pytest_system_test_plugin 

import logging
import os
import time
import pytest

CURL = "/usr/bin/curl -X POST http://localhost:{} -d hello_my_plugins"

import pytest


def test_go():
    pass

def test_use_case_help(process_factory):

    help = process_factory(["tedge", "-V"])
    help.run()
    assert help.get_stdout() == "tedge 0.5.1"

def test_use_case_help(process_factory):

    con = process_factory(["sudo", "tedge", "connect", "c8y"])
    con.run()

    print( con.get_stdout() )
    print( con.get_stderr( ))
    assert con.returncode == 0

    discon = process_factory(["sudo", "tedge", "disconnect", "c8y"])
    discon.run()

    print( discon.get_stderr() )
    print( discon.get_stdout() )

    assert discon.returncode == 0



