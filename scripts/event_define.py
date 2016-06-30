# coding: UTF-8

import imp
import os
import sys

def define(context):

	def test_method(arg):
		oSheet = context.get_document().CurrentController.ActiveSheet
		oCell1 = oSheet.getCellRangeByName("A1")
		oCell1.String = arg.Source.Model.Name

	context.add_app_handler('com.sun.star.awt.ActionEvent', 'Button1', test_method)
