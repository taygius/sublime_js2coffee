# @todo: add https://github.com/technocoreai/SublimeExternalCommand as extended rep
# @todo: check js or coffee
# 4 spaces?
 
import sublime, sublime_plugin, re
import jsCoffeeFunctions

class js2coffeeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.edit      = edit
        selectedRegion = self.view.sel()[0]
        selectedString = self.view.substr(selectedRegion).encode('utf-8')

        jsString, stderr = jsCoffeeFunctions.coffee2js(selectedString)

        if len(stderr) == 0:
            # replace selection with javascript
            self.view.replace(self.edit, selectedRegion, self.fixup(jsString))
        else: # if not coffee
            coffeeString, stderr = jsCoffeeFunctions.js2coffee(selectedString)
            if len(stderr) == 0:
                self.view.replace(self.edit, selectedRegion, self.fixup(coffeeString))
            else: #if not js
                self.show_error_panel(self.fixup(stderr))

    # Error panel & fixup from external command
    # https://github.com/technocoreai/SublimeExternalCommand
    def show_error_panel(self, stderr):
        panel = self.view.window().get_output_panel("php_beautifier_errors")
        panel.set_read_only(False)
        edit = panel.begin_edit()
        panel.erase(edit, sublime.Region(0, panel.size()))
        panel.insert(edit, panel.size(), stderr)
        panel.set_read_only(True)
        self.view.window().run_command("show_panel", {"panel": "output.php_beautifier_errors"})
        panel.end_edit(edit)

    def fixup(self, string):
        return re.sub('(\r\n|\r)', '\n', string)
