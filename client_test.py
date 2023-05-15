import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        test_quote = quotes[0]
        test_data_point = getDataPoint(test_quote)
        actual_price = test_data_point[3]

        bid_price = float(test_quote['top_bid']['price'])
        ask_price = float(test_quote['top_ask']['price'])
        expected_price = (bid_price + ask_price) / 2

        self.assertEqual(actual_price, expected_price)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        bid_greater_than_ask_quote = quotes[0]
        test_data_point = getDataPoint(bid_greater_than_ask_quote)
        test_ask_price = test_data_point[2]
        actual_price = test_data_point[3]

        self.assertTrue(actual_price > test_ask_price)

    """ ------------ Add more unit tests ------------ """

    def test_getDataPoint_calculatePriceBidSmallerThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        bid_greater_than_ask_quote = quotes[1]
        test_data_point = getDataPoint(bid_greater_than_ask_quote)
        test_ask_price = test_data_point[2]
        actual_price = test_data_point[3]

        self.assertTrue(actual_price < test_ask_price)

    def test_getRatio_calculateZeroPriceARatio(self):
        test_price_a = 0
        test_price_b = 100.55
        actual_ratio = getRatio(test_price_a, test_price_b)
        expected_ratio = 0

        self.assertEqual(actual_ratio, expected_ratio)

    def test_getRatio_calculateZeroPriceBRatio(self):
        test_price_a = 100.55
        test_price_b = 0
        actual_answer = getRatio(test_price_a, test_price_b)
        expected_answer = None

        self.assertEqual(actual_answer, expected_answer)

    def test_getRatio_calculateEqualRatio(self):
        test_price_a = test_price_b = 100.55
        actual_ratio = getRatio(test_price_a, test_price_b)
        expected_ratio = 1

        self.assertEqual(actual_ratio, expected_ratio)

    def test_getRatio_calculatePriceAGreaterThanBRatio(self):
        test_price_a = 10.23
        test_price_b = 5.99
        actual_ratio = getRatio(test_price_a, test_price_b)

        self.assertTrue(actual_ratio > 1)

    def test_getRatio_calculatePriceASmallerThanBRatio(self):
        test_price_a = 5.99
        test_price_b = 10.23
        actual_ratio = getRatio(test_price_a, test_price_b)

        self.assertTrue(actual_ratio < 1)


if __name__ == '__main__':
    unittest.main()
