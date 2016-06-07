import imp
import os
import uno

def launch(arg, doc):
	# context_path = os.path.dirname(uno.fileUrlToSystemPath(doc.URL)) + '/framework/context.py'
	context_path = '/Users/leeonky/Documents/source/FinanceDoc/framework/context.py'
	context = imp.load_source('module.name', context_path)

	# context.set_document(doc)
	# context.add_app_handler('com.sun.star.awt.ActionEven', 
	oSheet = doc.CurrentController.ActiveSheet
	# for property, value in vars(arg.Source.Model).iteritems():
		# print property, ": ", value
	oCell1 = oSheet.getCellRangeByName("A1")
	oCell1.String = arg.Source.Model.Label
	oCell1 = oSheet.getCellRangeByName("A2")
	oCell1.String = context_path
	# oCell1.String = uno.com.sun.star.awt.ActionEvent.__name__

