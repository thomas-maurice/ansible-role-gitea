import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_gitea_binary(host):
    gitea_bin = host.file('/usr/local/bin/gitea')
    assert gitea_bin.exists
    assert gitea_bin.user == 'root'
    assert gitea_bin.group == 'root'

def test_gitea_config_file(host):
    gitea_config = host.file('/etc/gitea/gitea.ini')
    assert gitea_config.exists
    assert gitea_config.mode == 0o600

def test_gitea_service_running(host):
    gitea = host.service('gitea')
    assert gitea.is_running

def test_gitea_reachable(host):
    gitea_http = host.run('curl http://localhost:3000')
    assert gitea_http.rc == 0
