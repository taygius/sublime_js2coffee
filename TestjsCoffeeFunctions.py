import unittest, jsCoffeeFunctions

########################################################################
class TestjsCoffeeFunctions(unittest.TestCase):
    """"""

    # #----------------------------------------------------------------------
    def test_coffe2js(self):
        """ ()-> """
        stdout, stderr = jsCoffeeFunctions.coffee2js('()->')
        stdout = jsCoffeeFunctions.prepareJs(stdout)
        self.assertEqual(stdout, '(function() {});')

    def test_coffe2js_2(self):
        """ a=->1 """
        stdout, stderr = jsCoffeeFunctions.coffee2js('a=->1')
        stdout = jsCoffeeFunctions.prepareJs(stdout)
        self.assertEqual(stdout, "var a;\n\na = function() {\n  return 1;\n};")

    #----------------------------------------------------------------------
    def test_prepareCoffee(self):
        """ prepareCoffee """
        test1 = jsCoffeeFunctions.prepareCoffee('// ololo \n ()->').strip(" \t\n\r")
        self.assertEqual(test1, '()->')

    #----------------------------------------------------------------------
    def test_prepareJs(self):
        """ prepareJs """
        test1 = jsCoffeeFunctions.prepareJs('// Generated by CoffeeScript 1.4.0\n\n(function() {});')
        self.assertEqual(test1, '(function() {});')

    #----------------------------------------------------------------------
    def test_js2coffee(self):
        """ js2coffee """
        stdout, stderr = jsCoffeeFunctions.js2coffee('(function() {});')
        self.assertEqual(jsCoffeeFunctions.prepareCoffee(stdout), '->')
