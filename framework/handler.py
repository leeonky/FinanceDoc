import imp
import os
import sys

context_path = os.path.dirname(sys.modules[__name__].__file__) + '/context.py'
context = imp.load_source('module.name', context_path).Context()

def attach_stdout():
	sys.stdout = open(os.path.dirname(os.path.dirname(context_path)) + '/stdout.log', "a", 0)
	sys.stderr = sys.stdout

def launch(arg, doc):
	attach_stdout()
	context.set_document(doc)
	context.import_file('event_define.py')
	context.invoke(arg)

def initDoc(doc):
	attach_stdout()
	context.set_document(doc)
	context.import_file('init_doc.py')

def testDoc(doc):
	attach_stdout()
	context.set_document(doc)
	context.import_file('test_doc.py')

