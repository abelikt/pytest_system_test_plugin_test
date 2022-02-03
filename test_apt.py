"""
Experimental tests that use apt

 To run the test
     pytest -s test_apt.py

 Make sure the package rolldice is not installed
     sudo apt remove -y rolldice
"""

import re
import pytest


def test_use_rolldice(process_factory):
    """This test installs a package via the package management, uses
    it and removes it again.
    """

    # TODO Calling binaries that are not installed is currently not good idea
    # call = process_factory(["rolldice"])
    # call.run()
    # print( call.get_stdout() )
    # print( call.get_stderr( ))
    # assert call.returncode == 0

    # make sure it is not installed
    call = process_factory(["whereis", "rolldice"])
    call.run()
    # print(call.get_stdout())
    # print(call.get_stderr())
    assert call.get_stdout() == "rolldice:"
    assert call.returncode == 0

    # Install package
    install = process_factory(["sudo", "apt-get", "install", "-y", "-q", "rolldice"])
    install.run()
    # print(install.get_stdout())
    # print(install.get_stderr())
    assert install.returncode == 0

    # Call and check output against a regex
    call = process_factory(["rolldice", "6"])
    call.run()
    # print(call.get_stdout())
    # print(call.get_stderr())
    # match a single digit
    assert re.match(r"^\d$", call.get_stdout()) is not None
    assert call.returncode == 0

    # deinstall it
    deinstall = process_factory(["sudo", "apt-get", "remove", "-y", "-q", "rolldice"])
    deinstall.run()
    # print(install.get_stderr())
    # print(install.get_stdout())
    assert install.returncode == 0

    # make sure it is not installed
    call = process_factory(["whereis", "rolldice"])
    call.run()
    # print(call.get_stdout())
    # print(call.get_stderr())
    assert call.get_stdout() == "rolldice:"
    assert call.returncode == 0


@pytest.fixture
def autoremove_rolldice(process_factory):
    """Fixture to care about"""
    deinstall = process_factory(["sudo", "apt-get", "remove", "-y", "-q", "rolldice"])
    deinstall.run()
    print("Rolldice removed before test")

    yield

    deinstall = process_factory(["sudo", "apt-get", "remove", "-y", "-q", "rolldice"])
    deinstall.run()
    print("Rolldice removed after test")


def test_use_rolldice_with_autoremove(autoremove_rolldice, process_factory):
    """This test installs a package via the package management, uses
    it and removes it again.
    Same as above, but we do not cleanup here
    """

    # make sure it is not installed
    call = process_factory(["whereis", "rolldice"])
    call.run()
    assert call.get_stdout() == "rolldice:"
    assert call.returncode == 0

    # Install package
    install = process_factory(["sudo", "apt-get", "install", "-y", "-q", "rolldice"])
    install.run()
    assert install.returncode == 0

    # Call and check output against a regex
    call = process_factory(["rolldice", "6"])
    call.run()

    # match a single digit
    assert re.match(r"^\d$", call.get_stdout()) is not None
    assert call.returncode == 0
