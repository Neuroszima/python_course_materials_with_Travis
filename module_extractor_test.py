import inspect
import importlib
from unittest import TestCase, main
import re



class SimpleTest(TestCase):

    MODULES_TO_IMPORT = [
        'podstawy',
        'zmienne'
    ]

    MODULE_CODE = None

    MODULE_LIST = {}

    class codeExtractor():

        def __init__(self, module_name):
            self.md_name = module_name

        def __call__(self, function):

            def function_wrapper(*args, **kwargs):
                SimpleTest.MODULE_CODE = inspect.getsource(SimpleTest.MODULE_LIST[self.md_name])
                result = function(*args, **kwargs)
                return result

            print("in : __call__")
            return function_wrapper

    def setUp(self):
        for md_name in SimpleTest.MODULES_TO_IMPORT:
            SimpleTest.MODULE_LIST[md_name] = importlib.import_module(md_name)

    @codeExtractor('podstawy')
    def test_something(self):
        """
        test for a class decorator with parameter
        :return:
        """
        self.assertIsNotNone(SimpleTest.MODULE_CODE)

    def assertHasString(self, regex, cases=None):
        string = re.search(regex, self.MODULE_CODE)
        print(string)
        self.assertIsNotNone(string)
        # added part
        if cases is not None:
            found = False
            strings = re.findall(regex, self.MODULE_CODE)
            print(strings)
            for case in cases:
                for catched_group in strings:
                    if case in catched_group:
                        found = True
                        print("found ", case)
                assert found, f"{case} not mentioned in python materials"
                found = False

    @codeExtractor('podstawy')
    def test_case_regex(self):
        """
        test for custom assertion function and it's modification
        :return:
        """
        equations = r"([\w]+) = ([\w\. ]+) ([\+\-\*\/]{1,2}) ([\w\. ]+)"
        self.assertHasString(equations, ['+', '-', '*', '/', '**'])

    @codeExtractor('zmienne')
    def test_withAs_file_statement(self):
        withAs_statement_regex = r'with open\([\'\"][\w\.]+[\'\"], [\'\"]([axrw])[\'\"]\) as [\w]+:'
        self.assertHasString(withAs_statement_regex, ['x', 'r', 'a', 'w'])

if __name__ == '__main__':
    main()
