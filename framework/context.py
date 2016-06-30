class Context:
	def set_document(self, doc):
		self.document = doc

	def get_document(self):
		return self.document

	def __init__(self):
		self.document = None
		self.handlers = {}

	def add_app_handler(self, command, name, handler):
		self.handlers.setdefault(command, {})
		self.handlers[command].setdefault(name, [])
		self.handlers[command][name].append(handler)

	def invoke(self, arg):
		for handler in self.handlers.get(type(arg).__name__, {}) \
				.get(arg.Source.Model.Name, []):
			handler(arg)

	def import_file(self, model):
		tmp_path = os.path.dirname(os.path.dirname(sys.modules[__name__].__file__)) + '/scripts/' + model
		imp.load_source('module.name', tmp_path).define(context)
