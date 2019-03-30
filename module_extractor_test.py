import inspect
import importlib
from unittest import TestCase, main
import re


class SimpleTest(TestCase):

    MODULES_TO_IMPORT = [
        'podstawy',
        'zmienne',
        'OOP_dziedziczenie_i_wiecej'
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

    def assertHasClass(self, cls_name, inheritances: list=None):
        match = re.finditer(r'class (?P<classname>[\w]+)(?P<inherited>\((?:[\w]+, )*[\w]+\))?:\n', self.MODULE_CODE)
        match_list = {k: v for k, v in [(x.group('classname'), x.group('inherited')) for x in match]}
        print(match_list)
        if inheritances is not None:
            for classname in inheritances:
                self.assertIsNotNone(re.search(classname, match_list[cls_name]),
                                     msg=f"{classname} not implemented in python materials")
        # Historical code - DON'T DO COPY PASTES BLINDLY
        # found = False
        # strings = re.findall(cls_name, self.MODULE_CODE)
        # # print(strings)
        # for class_name in inheritances:
        #     for catched_group in strings:
        #         if class_name in catched_group:
        #             found = True
        #             print("inherited ", class_name)
        #     assert found, f"{class_name} not implemented in python materials"
        #     found = False

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
        # language=regexp
        equations = r"([\w]+) = ([\w\. ]+) ([\+\-\*\/]{1,2}) ([\w\. ]+)"
        self.assertHasString(equations, ['+', '-', '*', '/', '**'])

    @codeExtractor('zmienne')
    def test_withAs_file_statement(self):
        # language=regexp
        withAs_statement_regex = r'with open\([\'\"][\w\.]+[\'\"], [\'\"]([axrw])[\'\"]\) as [\w]+:'
        self.assertHasString(withAs_statement_regex, ['x', 'r', 'a', 'w'])

    @codeExtractor('OOP_dziedziczenie_i_wiecej')
    def test_named_group_regex(self):
        # language=regexp
        cls_regex = r'class (?P<classname>[\w]+)(?P<inherited>\((?:[\w]+, )*[\w]+\))?:\n'
        something = re.finditer(cls_regex, self.MODULE_CODE)
        # calling results from named groups does not work with re.findall()
        # you have to use re.finditer() to be able to call them like that
        for match in something:
            print(match.group('classname'))
            print(match.group('inherited'))

    @codeExtractor('OOP_dziedziczenie_i_wiecej')
    def test_inheritace_classes(self):
        self.assertHasClass('Vegetable2', ['Plant'])
        # self.assertHasClass('Plant')
        # self.assertHasClass('T34', ['Tank'])
        # self.assertHasClass('Tank', ['Battleunit', 'Vehicle'])


if __name__ == '__main__':
    main()
