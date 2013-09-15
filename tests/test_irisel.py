class TestIrisel(object):

    def test_suma(self):
        suma = 2 + 2
        assert suma == 4

    def test_no_numero(self):
        num = 2 + 2
        assert isinstance(num, int)
