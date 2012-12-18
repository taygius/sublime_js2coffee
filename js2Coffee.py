import sublime, sublime_plugin, jsCoffeeFunctions

class js2coffeeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selectedRegion = self.view.sel()[0]
        selectedString = self.view.substr(selectedRegion).encode('utf-8')

        jsString, stderr = jsCoffeeFunctions.coffee2js(selectedString)

        if len(stderr) == 0:
            self.view.replace(edit, selectedRegion, jsString) # replace selection with javascript
        else: # if not coffee
            coffeeString, stderr = jsCoffeeFunctions.js2coffee(selectedString)
            if len(stderr) == 0:
                self.view.replace(edit, selectedRegion, coffeeString)
            else: #if not js
                self.show_error_panel(stderr)

    # Error panel & fixup from external command
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
