import imp
import os
import sys

def define(context):
	def test_method(arg):
		oSheet = context.get_document().CurrentController.ActiveSheet
		oCell1 = oSheet.getCellRangeByName("A1")
		oCell1.String = type(arg).__name__
		oCell1 = oSheet.getCellRangeByName("A2")
		oCell1.String = 'com.sun.star.awt.ActionEvent'

	context.add_app_handler('com.sun.star.awt.ActionEvent', test_method)
