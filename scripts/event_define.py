import imp
import os
import sys

def define(context):
	def test_method(arg):
		command = type(arg).__name__
		oSheet = context.get_document().CurrentController.ActiveSheet
		oCell1 = oSheet.getCellRangeByName("A1")
		oCell1.String = command
		oCell1 = oSheet.getCellRangeByName("A2")
		oCell1.String = 'com.sun.star.awt.ActionEvent'

	context.add_app_handler('com.sun.star.awt.ActionEvent', test_method)
