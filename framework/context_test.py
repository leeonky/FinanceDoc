import unittest

from Context import context

class ContextTest(unittest.TestCase):
	def test_set_and_get_document():
		context = Context();
		document = Object();

		context.set_document(document)
		
