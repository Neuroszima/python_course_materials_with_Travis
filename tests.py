import inspect
import unittest
import importlib
import dis
# import podstawy as pod


class StudentTests(unittest.TestCase):

    def load_modules(self, module_names):
        try:
            log = open('log.txt', "x")
        except FileExistsError:
            log = open('log.txt', "a")
        for each in module_names:
            log.write(f"loading {each}... \n")
            try:
                self.module_list[each] = importlib.import_module(each)
            except Exception as e:
                print(e, file=log)
                print(f"module named {each} not present in directory \n", file=log)
                log.close()
        log.write("finished loading modules...\n")
        log.close()

    def setUp(self):
        self.module_list = {}
        self.load_modules(["db_interaction", "OOP", "podstawy", "zmienne", "funkcje"])
        print(self.module_list)
        for key in self.module_list:
            print(key)
            print(self.module_list[key])

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
        print(representation)
        self.assertIsNotNone(representation)


if __name__ == '__main__':
    unittest.main()
