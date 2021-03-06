"""
Experimental tests that play with thin-edge.io.
See https://thin-edge.io

"""

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
    assert help.get_stdout() == "tedge 0.5.2"


def test_use_connect(process_factory):

    con = process_factory(["sudo", "tedge", "connect", "c8y"])
    con.run()

    print(con.get_stdout())
    print(con.get_stderr())
    assert con.returncode == 0

    discon = process_factory(["sudo", "tedge", "disconnect", "c8y"])
    discon.run()

    print(discon.get_stderr())
    print(discon.get_stdout())

    assert discon.returncode == 0


def test_use_case_connect_and_observe(process_factory):

    mos = process_factory(["/usr/bin/mosquitto_sub", "-v", "-t", "#"], name="mos")
    mos.run_bg()

    con = process_factory(["sudo", "tedge", "connect", "c8y"], name="con")
    con.run()

    print(con.get_stdout())
    print(con.get_stderr())
    assert con.returncode == 0

    discon = process_factory(["sudo", "tedge", "disconnect", "c8y"], name="discon")
    discon.run()

    print(discon.get_stderr())
    print(discon.get_stdout())

    assert discon.returncode == 0

    mos.kill()
    print(mos.get_stdout())
    print(mos.get_stderr())
    assert "tedge/commands/req/software/list" in mos.get_stdout()


# TODO tedge connect in the background ?
# TODO inverse gherkin here?
