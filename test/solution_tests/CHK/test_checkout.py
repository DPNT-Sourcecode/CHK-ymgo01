from solutions.CHK import checkout_solution


class TestCheckout():
    def test_A(self):
        assert checkout_solution.checkout('A') == 3

    def test_3A(self):
        assert checkout_solution.checkout('AAA') == 3
