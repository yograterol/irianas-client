from irianas_client.services.ftp.vsftp import vsFTPService
obj_vsftpd = vsFTPService()
tmp_path_vsftpd_config = '/tmp/vsftpd.conf'


class TestBINDService(object):

    def test_get_params(self):
        assert obj_vsftpd.listen == 'YES'
        assert obj_vsftpd.get('listen') == 'YES'

    def test_set_params(self):
        obj_vsftpd.listen = 'NO'
        assert obj_vsftpd.listen == 'NO'
        obj_vsftpd.listen = 'YES'
        assert obj_vsftpd.listen == 'YES'

    def test_save_config_file(self):
        obj_vsftpd.save_attr(tmp_path_vsftpd_config)
        assert open(tmp_path_vsftpd_config)
