from stockpile import utils


class TestUtils:

    def test_rel_return(self):
        a, b = (4, 2)

        assert utils.rel(a, b) == '200'

