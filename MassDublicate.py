import sublime
import sublime_plugin


class MassDublicateInsertCommand(sublime_plugin.TextCommand):
	def run_(self, edit_token, args):
		args = self.filter_args(args)
		if args:
			edit = self.view.begin_edit(edit_token, self.name())
			pos = self.view.sel()[0].end()
			if not self.view.sel()[0].empty():
				input_str = '\n' + self.view.substr(self.view.sel()[0])
				# self.view.insert(edit, pos, input_str*int(args))
				self.view.insert(edit, pos, input_str*int(args))
			else:
				sublime.status_message("Selection empty")
			self.view.end_edit(edit)





class MassDublicateCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Number of dublicate:", "", self.on_done, None, None)


	def on_done(self, num):

		if num.isdigit():
			self.window.run_command("mass_dublicate_insert", num)
		else:
			sublime.status_message("Error: " + num + " is not number")