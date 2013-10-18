from irianas_client.services.dns.bind import BINDService

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
