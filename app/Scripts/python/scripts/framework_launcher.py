import imp
import os
import uno
def framework_handler(arg):
	doc = XSCRIPTCONTEXT.getDocument()
	scripts_path = os.path.dirname(uno.fileUrlToSystemPath(doc.URL)) + '/framework/handler.py'
	framework = imp.load_source('module.name', scripts_path)
	framework.launch(arg, doc);

