from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_A(self):
        assert checkout_solution.checkout('A') == 50

    def test_3A(self):
        assert checkout_solution.checkout('AAA') == 130

    def test_invalid_inut(self):
        assert checkout_solution.checkout('sd"AFFFAARR') == -1

    def test_mix_inputs(self):
        assert checkout_solution.checkout('ABCD') == 115

    def test_invalid_input_space(self):
        assert checkout_solution.checkout('ABC D') == -1

    def test_3A2B(self):
        assert checkout_solution.checkout('ABABA') == 175

    def test_3C2D(self):
        assert checkout_solution.checkout('CCDCD') == 90

