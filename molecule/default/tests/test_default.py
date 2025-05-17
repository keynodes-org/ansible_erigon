import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")

@pytest.mark.parametrize(
    "directory",
    [
        "/opt/erigon/data",
        "/opt/erigon/config",
        "/opt/erigon/logs"
    ]
)
def test_directories(host, directory):
    d = host.file(directory)
    assert d.exists
    assert d.is_directory
    assert d.user == "erigon"
    assert d.group == "erigon"

@pytest.mark.parametrize(
    "file",
    [
        "/usr/local/bin/erigon",
        "/etc/systemd/system/erigon.service",
        "/opt/erigon/config/config.yml"
    ],
)
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.is_file


@pytest.mark.parametrize("service", ["erigon"])
def test_service(host, service):
    s = host.service(service)
    assert s.is_running
    assert s.is_enabled
