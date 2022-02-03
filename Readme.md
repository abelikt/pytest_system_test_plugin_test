
# Tests for the Pytest Systemtest Plugin

This are some experimental tests for the Pytest Systemtest Plugin

See:
https://github.com/bitmuster/pytest_system_test_plugin


## Usage

With the locally checked out plugin:

    python3 -m venv env-plugin

    pip install ../pytest_system_test_plugin

    source env-plugin/bin/activate

    pytest -s

    # Will install and deinstall a package with apt needs passwordless sudo access
    pytest -s test_apt.py

    # Needs thin-edge.io, mosquitto on your computer
    pytest -s test_tedge.py


