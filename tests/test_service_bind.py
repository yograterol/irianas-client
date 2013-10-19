import pytest
from irianas_client.services.dns.bind import BINDService

condition_test = "'VIRTUAL_ENV' in os.environ or 'TRAVIS' in os.environ"

obj_bind = BINDService()
tmp_path_named_config = '/tmp/named.conf'


class TestBINDService(object):

    def test_get_params(self):
        assert obj_bind.port == 53
        assert obj_bind.get('port') == 53

    def test_set_params(self):
        obj_bind.port = 80
        assert obj_bind.port == 80
        obj_bind.port = 53
        assert obj_bind.port == 53

    def test_save_config_file(self):
        obj_bind.save_attr(tmp_path_named_config)
        assert open(tmp_path_named_config)

    @pytest.mark.skipif(condition_test,
                        reason="requires root permission")
    def test_install(self):
        assert obj_bind.install()

    @pytest.mark.skipif(condition_test,
                        reason="requires root permission")
    def test_uninstall(self):
        assert obj_bind.remove()

    @pytest.mark.skipif(condition_test,
                        reason="requires root permission")
    def test_reinstall(self):
        assert obj_bind.install()
