from context import Context
from mock import MagicMock

def test_append_two_command_handler():
	class TestArg1(object):
		def __init__(self):
			pass
	class TestArg2(object):
		def __init__(self):
			pass
	target_method1 = MagicMock()
	target_method2 = MagicMock()

	context = Context()
	context.add_app_handler('TestArg1', target_method1)
	context.add_app_handler('TestArg2', target_method2)

	arg1 = TestArg1()
	context.invoke(arg1)
	target_method1.assert_called_with(arg1)

	arg2 = TestArg2()
	context.invoke(arg2)
	target_method2.assert_called_with(arg2)

def test_append_two_handlers_for_one_command():
	class TestArg(object):
		def __init__(self):
			pass
	target_method1 = MagicMock()
	target_method2 = MagicMock()
	context = Context()
	context.add_app_handler('TestArg', target_method1)
	context.add_app_handler('TestArg', target_method2)

	arg = TestArg()
	context.invoke(arg)

	target_method1.assert_called_with(arg)
	target_method2.assert_called_with(arg)
