class Context:
	document = None
	@staticmethod
	def set_document(doc):
		Context.document = doc 
	@staticmethod
	def get_document():
		return Context.document

	command_handlers = {}
	@staticmethod
	def add_app_handler(command, handler):
		if command not in Context.command_handlers:
			Context.command_handlers[command] = []
		Context.command_handlers[command].append(handler)

	@staticmethod
	def invoke(arg):
		command = type(arg).__name__
		if command in Context.command_handlers:
			for handler in Context.command_handlers[command]:
				handler(arg)
