import imp
import os
import sys

context_path = os.path.dirname(sys.modules[__name__].__file__) + '/context.py'
context = imp.load_source('module.name', context_path).Context

def launch(arg, doc):
	context.set_document(doc)
	event_define = os.path.dirname(sys.modules[__name__].__file__) + '/../scripts/event_define.py'
	imp.load_source('module.name', event_define).define(context)
	context.invoke(arg)

