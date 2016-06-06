import imp
import os
import uno
def test_test(arg):
	doc = XSCRIPTCONTEXT.getDocument()
	scripts_path = os.path.dirname(uno.fileUrlToSystemPath(doc.URL)) + '/scripts/framework.py'
	framework = imp.load_source('module.name', scripts_path)
	framework.launch(arg, doc);

