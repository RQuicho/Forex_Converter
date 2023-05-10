from app import app

class ForexTestCases(TestCase):
	"""Tests all functions for converting currency"""

	def test_home_page(self):
		with app.test_client() as client:
			resp = client.get('/')
			html = resp.get_data(as_text=True)

			self.assertEqual(resp.status_code, 200)
			self.assertIn('<input type="text" name="from">', html)

	def test_convert_submit(self):
		with app.test_client() as client:
			resp = client.post('/convert', data={'from': 'USD', 'to': 'EUR', 'amount': 100})
			html = resp.get_data(as_text=True)

			self.assertEqual(resp.status_code, 200)
			self.assertIs(resp.data['result'], float(amount))
			# self.assertEqual(resp.data['result'], 91.009788)

		