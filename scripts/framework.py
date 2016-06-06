def launch(arg, doc):
	oSheet = doc.CurrentController.ActiveSheet
	oCell1 = oSheet.getCellRangeByName("A1")
	oCell1.String = 'Hello world'
