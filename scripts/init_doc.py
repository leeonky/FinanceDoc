# coding: UTF-8

import imp
import os
import sys

def define(context):
	oSheet = context.get_document().CurrentController.ActiveSheet
	oCell1 = oSheet.getCellRangeByName("A2")
	oCell1.String = 'initDoc'
