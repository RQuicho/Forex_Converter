from unittest import TestCase
from app import app

class ForexTestCases(TestCase):
	"""Tests all functions for converting currency"""

	def test_home_page_displays_form(self):
		with app.test_client() as client:
			resp = client.get('/')
			html = resp.get_data(as_text=True)

			self.assertEqual(resp.status_code, 200)
			self.assertIn('<input type="text" name="from">', html)
			self.assertIn('<input type="text" name="to">', html)

	def test_returns_correct_conversion(self):
		with app.test_client() as client:
			resp = client.post('/convert', data={'from': 'USD', 'to': 'USD', 'amount': 1})

			result = resp.get_data(as_text=True)
			self.assertEqual(resp.status_code, 200)
			self.assertIn('<h1>The result is $ 1</h1>', result)

			# amount = float(result.strip('$ '))
			# self.assertIsInstance(amount, float)

			# values = resp.get_data(as_text=True).split()
			# first_curr, second_curr, amount = values[0], values[1], values[2]
			# print(first_curr)
			# self.assertEqual(len(first_curr), 3)
			# self.assertEqual(first_curr, first_curr.upper())
			# self.assertEqual(len(second_curr), 3)
			# self.assertEqual(second_curr, second_curr.upper())

		