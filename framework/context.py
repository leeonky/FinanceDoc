class Context:
	def __init__(self):
		self.document = None
		self.command_handlers = {}

	def set_document(self, doc):
		self.document = doc

	def get_document(self):
		return self.document

	def add_app_handler(self, command, handler):
		if command not in self.command_handlers:
			self.command_handlers[command] = []
		self.command_handlers[command].append(handler)

	def invoke(self, arg):
		command = type(arg).__name__
		if command in self.command_handlers:
			for handler in self.command_handlers[command]:
				handler(arg)
				
	def import_root(self, model):
		tmp_path = os.path.dirname(sys.modules[__name__].__file__) + '/../' + model
		imp.load_source('module.name', tmp_path).define(context)
