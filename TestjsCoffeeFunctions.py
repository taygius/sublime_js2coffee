import sys, unittest, re, jsCoffeeFunctions

########################################################################
class TestjsCoffeeFunctions(unittest.TestCase):
    """test js2coffee and coffee2js:"""
    

    def test_coffee2js(self):
        """ self.assertCoffee2js(input_, shouldBe)"""

        self.assertCoffee2js("""
            ->
        """, """
            (function() {});
        """);

        self.assertCoffee2js("""
            a=->1
        """, """
            var a;
            a = function() {
                return 1;
            };
        """)

        self.assertCoffee2js("""
            a=->1
        """, """
            var a;
            a = function() {
                return 1;
            };
        """)

        self.assertCoffee2js("""
            // test comments
            ->
        """, """
            (function() {});
        """)


        self.assertCoffee2js("""
            console.log a for a in [1..9]
        """, """
            var a, _i;
            for (a = _i = 1; _i <= 9; a = ++_i) {
              console.log(a);
            }
        """)



    def test_js2coffee(self):
        """ self.assertJs2Coffee(input_, shouldBe)"""

        self.assertJs2Coffee("""
            (function() {});
        """, """
            ->
        """)

        self.assertJs2Coffee("""
            function fn(a,b,c) {
                return [c,b,a];
            };
        """, """
            fn = (a, b, c) ->
                [c, b, a]
        """)

    # assertion functions
    def assertCoffee2js(self, input_, shouldBe):
        result, err = jsCoffeeFunctions.coffee2js(input_)
        self.assertEqual(self.cl(result), self.cl(shouldBe))

    def assertJs2Coffee(self, input_, shouldBe):
        result, err = jsCoffeeFunctions.js2coffee(input_)
        self.assertEqual(self.cl(result), self.cl(shouldBe))

    # clear string
    def cl(self, s):
        return re.sub(r'[\n\t\ ]', '', s)