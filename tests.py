import inspect
import unittest
import importlib

import re


class StudentTests(unittest.TestCase):

    BASIC_FUNCTIONS = ["hello_world_function",
                       "hello_world_function2",
                       "suma",
                       "sum",
                       "foo"]

    MODULES_LIST = ["db_interaction", "OOP_metody_magiczne", "podstawy",
                    "OOP_podstawy", "dekoratory", "zmienne", "funkcje"]

    def assertHasFunction(self, function_name):
        print(function_name, " searched")
        # raw_string = r"^def {}".format(function_name)
        # print(raw_string)
        matched = re.findall(r"def ([\w]+)\(", self.module_code)
        print(matched)
        assert function_name in matched

        # if matched is None: assert 1 == 0
        # else: assert 0 == 0

    def load_modules(self, module_names):
        try:
            log = open('log.txt', "x")
        except FileExistsError:
            log = open('log.txt', "w")
        for name in module_names:
            log.write(f"loading {name}... \n")
            try:
                self.module_list[name] = importlib.import_module(name)
            except Exception as e:
                print(e, file=log)
                print(f"module named {name} not present in directory \n", file=log)
        log.write("finished loading modules...\n")
        log.close()

    def setUp(self):
        self.module_list = {}
        self.load_modules(self.MODULES_LIST)
        # print(self.module_list)
        for key in self.module_list:
            print(key)
            print(self.module_list[key].__name__)

    def test_basic_functions_present(self):
        self.module_code = inspect.getsource(self.module_list['funkcje'])
        print(self.module_code)
        for function_name in self.BASIC_FUNCTIONS:
            self.assertHasFunction(function_name)

    def test_setUp(self):
        samplefunc = self.module_list["funkcje"].function
        self.assertIsNotNone(samplefunc)

    def test_has_kwargs_function(self):
        kw_func = self.module_list["funkcje"].function_kwargs
        self.assertIsNotNone(kw_func)

    def test_kwargs_working(self):
        kw_func = self.module_list["funkcje"].function_kwargs
        self.assertIsNotNone(kw_func(20, 30, file='test.txt', something='aosioa', acnobaw=[123, 'aofh']))
        self.assertIsNotNone(kw_func(10, 5))
        with self.assertRaises(TypeError) as e:
            result = kw_func()

    def test_basics(self):
        representation = inspect.getsource(self.module_list['podstawy'])
        self.assertIsNotNone(representation)


if __name__ == '__main__':
    unittest.main()
