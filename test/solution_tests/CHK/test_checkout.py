from solutions.CHK import checkout_solution


class TestCheckout():
    def test_A(self):
        assert checkout_solution.checkout('A') == 50

    def test_3A(self):
        assert checkout_solution.checkout('AAA') == 130

    def test_invalid_inut(self):
        assert checkout_solution.checkout('sd"AFFFAARR') == 130

    def test_mix_inputs(self):
        assert checkout_solution.checkout('ABCD') == 130


