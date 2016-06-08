import imp
import os
import sys

context_path = os.path.dirname(sys.modules[__name__].__file__) + '/context.py'
context = imp.load_source('module.name', context_path).Context()

def launch(arg, doc):
	context.set_document(doc)
	context.import_root('/scripts/event_define.py')
	context.invoke(arg)

