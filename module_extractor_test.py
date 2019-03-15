import inspect
import importlib
from unittest import TestCase




class SimpleTest(TestCase):

    MODULES_TO_IMPORT = [
        'podstawy'
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
        print(SimpleTest.MODULE_CODE)


