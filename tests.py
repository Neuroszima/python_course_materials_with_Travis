import inspect
import unittest
import importlib

import re


class StudentTests(unittest.TestCase):
    """
    Test Case for python course modules

    used to check if most important features have been told about during classes, from different
    areas of python programming

    most tests revolves around checking if the modules have specific things implemented, in the form of
    regular expression matching the strings in modules responsible for desired features to show during classes

    that way running a test can show if some features have not been told about, or was omitted due to forgetful nature
    of the human

    """

    BASIC_FUNCTIONS = ["hello_world_function",
                       "hello_world_function2",
                       "suma",
                       "sum",
                       "foo"]

    MODULES_TO_LOAD = ["db_interaction", "OOP_metody_magiczne", "podstawy",
                       "OOP_podstawy", "dekoratory", "zmienne", "funkcje"]

    MODULE_CODE = None

    MODULE_LIST = {}

    class Module:
        """
        a `Module` class serves as a decorator, that wraps a specific test to set what code of which module
        should be checked during the test

        """
        def __init__(self, module_name):
            """
            initializes with the module_name as string, that has to be loaded for a given test

            :param module_name: module to check for
            """
            self.md_name = module_name

        def __call__(self, function):
            def function_wrapper(*args, **kwargs):
                StudentTests.MODULE_CODE = inspect.getsource(StudentTests.MODULE_LIST[self.md_name])
                result = function(*args, **kwargs)
                return result

            # print("in : __call__")
            return function_wrapper

    def load_modules(self, module_names):
        try:
            log = open('log.txt', "x")
        except FileExistsError:
            log = open('log.txt', "w")
        for name in module_names:
            log.write(f"loading {name}... \n")
            try:
                self.MODULE_LIST[name] = importlib.import_module(name)
            except Exception as e:
                print(e, file=log)
                print(f"module named {name} not present in directory \n", file=log)
        log.write("finished loading modules...\n")
        log.close()

    def assertHasFunction(self, function_name):
        # raw_string = r"^def {}".format(function_name)
        # print(raw_string)
        matched = re.findall(r"def ([\w]+)\(", self.MODULE_CODE)
        # print(matched)
        assert function_name in matched
        print(function_name, " found")

        # if matched is None: assert 1 == 0
        # else: assert 0 == 0

    def assertHasString(self, regex):
        string = re.search(regex, self.MODULE_CODE)
        print(string)
        self.assertIsNotNone(string)

    def setUp(self):
        print('setUp() ...')
        self.module_list = {}
        self.load_modules(self.MODULES_TO_LOAD)
        # print(self.module_list)
        for key in self.module_list:
            print(self.module_list[key].__name__)  # check if modules are there

    def test_setUp(self):
        samplefunc = self.MODULE_LIST["funkcje"].function
        self.assertIsNotNone(samplefunc)

    @Module('podstawy')
    def test_basics(self):
        self.assertIsNotNone(self.MODULE_CODE)

    @Module('podstawy')
    def test_basics_equations(self):
        equations = [
            r"([\w]+) = ([\w]+)",                    # assigning to variable
            r"([\w]+) = ([\w\. ]+) \+ ([\w\. ]+)",    # addition
            r"([\w]+) = ([\w\. ]+) \- ([\w\. ]+)",    # subtraction
            r"([\w]+) = ([\w\. ]+) \* ([\w\. ]+)",    # multiplication
            r"([\w]+) = ([\w\. ]+) \/ ([\w\. ]+)",   # division
            r"([\w]+) = ([\w\. ]+) \*\* ([\w\. ]+)"  # to the power of
            ]
        for equation in equations:
            print(equation)
            self.assertHasString(equation)

    @Module('podstawy')
    def test_IfElse_programflow(self):
        ifElse_statement = re.findall(r'if ([\w <>=]+):\n([\w \(\"\)\.\n\+=<>]+)else:\n([\w \(\"\)\.\n]+)\n',
                                      self.MODULE_CODE)
        self.assertIsNotNone(ifElse_statement)

    @Module('podstawy')
    def test_forEachIn_programflow(self):
        forEachIn_statement = re.findall(r'for ([\w ]+) in ([\w \[\]\(\"\)\.\n\+=<>:,]+):',
                                         self.MODULE_CODE)
        self.assertIsNotNone(forEachIn_statement)

    @Module('podstawy')
    def test_basic_functions(self):
        basic_functions = [
            # usages of "input" function
            r"",
            # usages of "open" function
            r"",
            # usages of "print" function,
            r"print(([\(\w\.\-\"\)\:\+=<> śćąźżę]+,[\(\w\.\-\"\)\:\+=<> śćąźżę]+)|([\(\w\.\-\"\)\:\+=<> śćąźżę]+))",
        ]

    @Module('funkcje')
    def test_basic_functions_present(self):
        # print(self.MODULE_CODE)
        for function_name in self.BASIC_FUNCTIONS:
            self.assertHasFunction(function_name)

    @Module('funkcje')
    def test_has_kwargs_function(self):
        kw_func = self.MODULE_LIST["funkcje"].function_kwargs
        self.assertIsNotNone(kw_func)

    @Module('funkcje')
    def test_kwargs_working(self):
        kw_func = self.MODULE_LIST["funkcje"].function_kwargs
        with self.assertRaises(TypeError) as e:
            result = kw_func()
        self.assertIsNotNone(kw_func(10, 5))
        self.assertIsNotNone(kw_func(20, 30, file='test.txt', something='aosioa', acnobaw=[123, 'aofh']))


if __name__ == '__main__':
    unittest.main()
