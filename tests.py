import inspect
import os
import unittest
import importlib
import re
from platform import system


class StudentTests(unittest.TestCase):
    """
    Test Case for python course modules

    used to check if most important features have been told about during classes, from different
    areas of python programming

    most tests revolves around checking if the modules have specific things implemented, in the form of
    regular expression matching the strings in modules responsible for desired features to show during classes

    others check if the functions/classes work as intended by importing a module and using them with arguments
    and checking outputs

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
                print("coducting test: ")
                print("module: ", StudentTests.MODULE_LIST[self.md_name].__name__)
                print("test: ", function.__name__)
                StudentTests.MODULE_CODE = inspect.getsource(StudentTests.MODULE_LIST[self.md_name])
                result = function(*args, **kwargs)
                # if self.md_name == "zmienne":
                #     if system() == 'Windows':
                #         os.system('rem new_file.txt new_file2.txt')
                #     else:
                #         os.system('rm new_file.txt new_file2.txt')
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

    def assertHasString(self, regex, cases=None):
        string = re.search(regex, self.MODULE_CODE)
        # print(string)
        self.assertIsNotNone(string, msg="no match for current regex")
        if cases is not None:
            found = False
            strings = re.findall(regex, self.MODULE_CODE)
            # print(strings)
            for case in cases:
                for catched_group in strings:
                    if case in catched_group:
                        found = True
                        print("found ", case)
                assert found, f"{case} not mentioned in python materials"
                found = False

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
        equations = r"([\w]+) = ([\w\. ]+) ([\+\-\*\/]{1,2}) ([\w\. ]+)"
        self.assertHasString(equations, ['+', '-', '*', '/', '**'])

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

    @Module('zmienne')
    def test_basic_functions(self):
        basic_functions = [
            # usages of "input" function
            r"input([\w\(\'\"\:\+ ,ążźćęśłóń]{3,}\))",
            # usages of "open" function
            r"open\([\'\"][\w\.]+[\'\"], ([\'\"][axrw][\'\"])\)",
            r"[\w]+ = open\([\'\"][\w\.]+[\'\"], ([\'\"][axrw][\'\"])\)",
            r"[\w]+\.close\(\)",
            # usages of "isinstance" function
            r"isinstance\([\w]+, ((int)|(bool)|(float)|(str))\)",
            r"if isinstance\([\w]+, ((int)|(bool)|(float)|(str))\)\:",
            # usages of "type" function
            r"type\([\w]+\)",
            r"if type\([\w]+\) == [\w]+\:",
        ]
        for function_regex in basic_functions:
            print(function_regex)
            self.assertHasString(function_regex)

    @Module('zmienne')
    def test_variable_types(self):
        variable_types_regex = r"[\n \(]((int)|(float)|(str))\([\w\(\)\'\" :]+\)"
        self.assertHasString(variable_types_regex)

    @Module('zmienne')
    def test_withAs_file_statement(self):
        withAs_statement_regex = r'with open\([\'\"][\w\.]+[\'\"], [\'\"]([axrw])[\'\"]\) ' \
                                 r'as [\w]+:([\w \(\"\'\)\.\n\+=<>#\!\?]+)\n'
        self.assertHasString(withAs_statement_regex, ['x', 'r', 'a', 'w'])

    @Module('zmienne')
    def test_tryExcept_statement(self):
        tryExcept_statement_regex = r"try:\n[\w\(\)\'\"\s+><=.,:\?\!]+(?<=except )[\w]+Error:" \
                                    r"\n[\w\(\)\'\"\s+><=.,:\?\!]+(?<=\n\n)"
        self.assertHasString(tryExcept_statement_regex)

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
