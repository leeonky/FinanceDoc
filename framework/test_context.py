from context import Context
from mock import MagicMock
import unittest

class ActionEvent(object):
	def __init__(self, name):
		class SourceArg(object):
			def __init__(self, name):
				class ModelArg(object):
					def __init__(self, name):
						self.Name = name
				self.Model= ModelArg(name)
		self.Source = SourceArg(name)

class OpenEvent(object):
	def __init__(self, name):
		class SourceArg(object):
			def __init__(self, name):
				class ModelArg(object):
					def __init__(self, name):
						self.Name = name
				self.Model= ModelArg(name)
		self.Source = SourceArg(name)


class TestContext(unittest.TestCase):

	def setUp(self):
		self.target_method1 = MagicMock()
		self.target_method2 = MagicMock()
		self.context = Context()


	def test_append_one_handler_to_one_control(self):
		control_name = 'test'
		self.context.add_app_handler('ActionEvent', control_name, self.target_method1)
		event_arg = ActionEvent(control_name)

		self.context.invoke(event_arg)

		self.target_method1.assert_called_with(event_arg)
		
	def test_append_two_handlers_to_one_control(self):
		control_name = 'test'
		self.context.add_app_handler('ActionEvent', control_name, self.target_method1)
		self.context.add_app_handler('ActionEvent', control_name, self.target_method2)
		event_arg = ActionEvent(control_name)

		self.context.invoke(event_arg)

		self.target_method1.assert_called_with(event_arg)
		self.target_method2.assert_called_with(event_arg)

	def test_append_handler_to_two_controls_and_invoke_one_crontrol(self):
		control_name1 = 'test1'
		control_name2 = 'test2'
		self.context.add_app_handler('ActionEvent', control_name1, self.target_method1)
		self.context.add_app_handler('ActionEvent', control_name2, self.target_method2)
		event_arg = ActionEvent(control_name1)

		self.context.invoke(event_arg)

		self.target_method1.assert_called_with(event_arg)
		self.target_method2.assert_not_called()

	def test_append_two_command_types(self):
		control_name = 'test'
		self.context.add_app_handler('ActionEvent', control_name, self.target_method1)
		self.context.add_app_handler('OpenEvent', control_name, self.target_method2)
		event_arg = ActionEvent(control_name)

		self.context.invoke(event_arg)

		self.target_method1.assert_called_with(event_arg)
		self.target_method2.assert_not_called()

if __name__ == '__main__':
	unittest.main()
