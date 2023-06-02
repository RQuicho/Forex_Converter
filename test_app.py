from unittest import TestCase
from app import app
import json

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
			resp = client.post('/convert', data={
				'from': 'USD',
				'to': 'USD',
				'amount': 1
			})

			result = resp.get_data(as_text=True)
			self.assertEqual(resp.status_code, 200)
			self.assertIn('<h1>The result is $ 1</h1>', result)

			self.assertEqual(resp.data['from'], 'USD')
			self.assertEqual(resp.data['to'], 'USD')
			self.assertIsInstance(resp.data['amount'], float)










			
	


		