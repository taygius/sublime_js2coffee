import sublime, sublime_plugin, jsCoffeeFunctions

class js2coffeeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.sel()[0]
        string = self.view.substr(region).encode('utf-8')

        javascript, stderr = jsCoffeeFunctions.coffee2js(string)

        if len(stderr) == 0:
            self.view.replace(edit, region, javascript) #replace selection with javascript
        else: # if not coffee
            coffee, stderr = jsCoffeeFunctions.js2coffee(string)
            if len(stderr) == 0:
                self.view.replace(edit, region, coffee)
            else: #if not js
                self.show_error_panel(stderr)

    # Error panel from external command
    # https://github.com/technocoreai/SublimeExternalCommand
    def show_error_panel(self, stderr):
        panel = self.view.window().get_output_panel("js2coffee_errors")
        panel.set_read_only(False)
        edit = panel.begin_edit()
        panel.erase(edit, sublime.Region(0, panel.size()))
        panel.insert(edit, panel.size(), stderr)
        panel.set_read_only(True)
        self.view.window().run_command("show_panel", {"panel": "output.js2coffee_errors"})
        panel.end_edit(edit)
