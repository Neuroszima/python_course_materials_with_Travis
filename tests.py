import ast
import inspect
import unittest
import importlib
import re
import dis


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

    MODULES_TO_LOAD = ["db_interaction", "OOP_dziedziczenie_i_wiecej", "podstawy",
                       "OOP_podstawy", "dekoratory", "zmienne", "funkcje",
                       "generatory_i_iteratory"]

    MODULE_CODE = None

    MODULE_LIST = {}

    class Module:
        """
        a ``Module`` class serves as a decorator, that wraps a specific test to set what code of which module
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
                print("\ncoducting test: ")
                print("module: ", StudentTests.MODULE_LIST[self.md_name].__name__)
                print("test: ", function.__name__)
                StudentTests.MODULE_CODE = inspect.getsource(StudentTests.MODULE_LIST[self.md_name])
                result = function(*args, **kwargs)
                return result

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
        matched = re.findall(r"def ([\w]+)\(", self.MODULE_CODE)
        # print(matched)
        assert function_name in matched
        print(function_name, " found")

    def assertHasString(self, regex, cases: list=None):
        string = re.search(regex, self.MODULE_CODE)
        # print(string)
        self.assertIsNotNone(string, msg="no match for current regex:\n"
                                         "{}".format(regex))
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

    def assertHasClass(self, cls_name: str, inheritances: list=None):
        match = re.finditer(r'class (?P<classname>[\w]+)(?P<inherited>\((?:[\w]+, )*[\w]+\))?:\n', self.MODULE_CODE)
        # print(string)
        match_list = {k: v for k, v in
                      [(x.group('classname'), x.group('inherited')) for x in match]}
        #             ^ <- the list starting above the "^" character works similarly to what zip(list1, list2) does
        # https://stackoverflow.com/questions/209840/convert-two-lists-into-a-dictionary-in-python
        if inheritances is not None:
            for classname in inheritances:
                self.assertIsNotNone(re.search(classname, match_list[cls_name]),
                                     msg=f"{classname} not implemented in python materials")

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
        # language=regexp
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
        # language=regexp
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
        # language=regexp
        variable_types_regex = r"[\n \(]((int)|(float)|(str))\([\w\(\)\'\" :]+\)"
        self.assertHasString(variable_types_regex, ['int', 'float', 'str'])

    @Module('zmienne')
    def test_withAs_file_statement(self):
        # language=regexp
        withAs_statement_regex = r'with open\([\'\"][\w\.]+[\'\"], [\'\"]([axrw])[\'\"]\) ' \
                                 r'as [\w]+:([\w \(\"\'\)\.\n\+=<>#\!\?]+)\n'
        self.assertHasString(withAs_statement_regex, ['x', 'r', 'a', 'w'])

    @Module('zmienne')
    def test_tryExcept_statement(self):
        # language=regexp
        tryExcept_statement_regex = r"try:\n[\w\(\)\'\"\s+><=.,:\?\!]+(?<=except )[\w]+Error:" \
                                    r"\n[\w\(\)\'\"\s+><=.,:\?\!]+(?<=\n\n)"
        self.assertHasString(tryExcept_statement_regex)

    @Module('zmienne')
    def test_lists(self):
        # language=regexp
        lists_regex = [
            r'[\w]+ = \[\]',
            r'[\w]+ = list\(\)',
            r'\[(?<=\[)(?P<insides>(?:[\w\s\n\(\)\'\"\+., ]+, )+[\n\(\)\w\s\'\"\+. ]+)\]',
        ]
        for regex in lists_regex:
            self.assertHasString(regex)
        # language=regexp
        multiargument_list_regex = r'\[(?<=\[)(?P<insides>(?:[\w\s\n\(\)\'\"\+., ]+, )+[\n\(\)\w\s\'\"\+. ]+)\]'
        insides = [x.group('insides') for x in re.finditer(multiargument_list_regex, self.MODULE_CODE)]
        results = [re.findall(r'([\w.\'\"\s]+), ', string) for string in insides]
        # # print(results)
        # testing = results[0]
        # # print(testing)
        # for value in testing:
        #     print(type(ast.literal_eval(value)))
        for var_type in [bool, int, str, float]:
            match = False
            for single_list_contents in results:
                if match: break
                for element in single_list_contents:
                    if isinstance(ast.literal_eval(element), var_type): match = True
                    if match: break
            assert match, f"{var_type} not show as usable in lists!"


    @Module('zmienne')
    def test_dicts(self):
        # language=regexp
        dicts_regex = [r'\{\}',
                       r'(?P<pair>([\'\"][\w ]+[\'\"] : [\{\}\w\s\n\'\"\:. żźćśęąółń]+(?P<suffix>,\n|\}\n)))',
                       r'[\w]+\[[\'\"][\w\s]+[\'\"]\] = [\w\s\'\".,ąśćźżęółń\[\]*\-+><=]+\n',
                       r'[\w]+ = \{[\w\s\'\"{} :,.]+\}\n']
        for regex in dicts_regex:
            print(regex)
            self.assertHasString(regex)
        # language=regexp
        sample_dict = re.findall(
            r'[\w]+ = dict\((?P<insides>(?:[\w\n ]+=[\w\'\"\s().,]+,\n)+(?:[\w\n ]+=[\w\'\"\s().,]+))\)',
            self.MODULE_CODE)
        print('sample dict: ', sample_dict)
        arguments = re.findall(
            r'(([\w]+=[\w\'\[\]\n(),]+|[\[][\w\n\'\"()ąśćźżęóńł ,]+[\]],)(, |,\n|\n))',
            sample_dict[0])
        print(arguments)
        self.assertIsNotNone(arguments)

    @Module('zmienne')
    def test_listcomp(self):
        # language=regexp
        listComp_regex = [r'\[([\w\' śćżźęąłó()]+) for [\w]+ in [\w\s)(]+\]',
                          r'\[([\w*\-\/\\+=><)(. ]+) for [\w\s,.()]+ in zip\([\w, ]+\)\]']
        for regex in listComp_regex:
            self.assertHasString(regex)

    @Module('zmienne')
    def test_tuple(self):
        # language=regexp
        tuple_regex = [r'= tuple\(([^\n)]*)\)\n',
                       r'= (([\w]+), )*[\w]+\n',
                       r'[\w]+ = [\w]+,[\s]?\n']
        for regex in tuple_regex:
            self.assertHasString(regex)

    @Module('funkcje')
    def test_basic_functions_present(self):
        # print(self.MODULE_CODE)
        basic_functions = ["hello_world_function",
                           "hello_world_function2",
                           "suma",
                           "sum",
                           "foo"]
        for function_name in basic_functions:
            self.assertHasFunction(function_name)

    @Module('funkcje')
    def test_void_function(self):
        hw, hw2 = (self.MODULE_LIST["funkcje"].hello_world_function,
                   self.MODULE_LIST["funkcje"].hello_world_function2)
        hw_as_text = inspect.getsource(hw)
        hw2_as_text = inspect.getsource(hw2)
        print(hw_as_text, '\n', hw2_as_text)
        self.assertIsNotNone(re.findall(r'return [\"\']hello world from function[\"\']', hw_as_text)[0])
        self.assertEqual(re.findall(r'return ', hw2_as_text), [])
        self.assertIsNotNone(re.findall(r'print\([\"\']hello world from function[\"\']\)', hw2_as_text)[0])
        void = self.MODULE_LIST["funkcje"].hello_world_function2()
        non_void = self.MODULE_LIST["funkcje"].hello_world_function()
        self.assertIsNone(void)
        self.assertIsNotNone(non_void)

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

    @Module('funkcje')
    def test_selfreference(self):
        pass

    @Module('OOP_podstawy')
    def test_oop_classes(self):
        methods = ['__init__', '__str__', '__repr__', ]
        bike, polynomial, hw_cls, not_hw_cls, vege = (
            self.MODULE_LIST['OOP_podstawy'].Bicycle,
            self.MODULE_LIST['OOP_podstawy'].Polynomial,
            self.MODULE_LIST['OOP_podstawy'].HelloWorld,
            self.MODULE_LIST['OOP_podstawy'].HelloWorldWithNothing,
            self.MODULE_LIST['OOP_podstawy'].Vegetable
        )
        ast_msg = '{} not implemented in {} class!'
        assert hasattr(hw_cls, "__init__"), ast_msg.format("__init__", hw_cls.__name__)
        for method in methods:
            assert hasattr(polynomial, method), ast_msg.format(method, polynomial.__name__)
            assert hasattr(bike, method), ast_msg.format(method, bike.__name__)
            assert hasattr(vege, method), ast_msg.format(method, vege.__name__)
        assert hasattr(polynomial, '__len__'), ast_msg.format("__init__", polynomial.__name__)
        assert hasattr(polynomial, '__add__'), ast_msg.format("__init__", polynomial.__name__)

    @Module('OOP_podstawy')
    def test_bicycle(self):
        bike = self.MODULE_LIST['OOP_podstawy'].Bicycle('blue', 'mountain', gears=5, wheel_width=2,
                                                        company="BMI hardcore burners")
        self.assertEqual(bike.color, 'blue')

    @Module('OOP_podstawy')
    def test_polynomial(self):
        polynomial = self.MODULE_LIST['OOP_podstawy'].Polynomial(1, 2, 3)
        self.assertEqual("1 + 2x^1 + 3x^2", str(polynomial))

    @Module('OOP_podstawy')
    def test_property(self):
        vegetable = self.MODULE_LIST['OOP_podstawy'].Vegetable(40, 'blue')
        self.assertEqual(vegetable.color, 'blue')
        self.assertEqual(vegetable.mass, 40)
        property_color = self.MODULE_LIST['OOP_podstawy'].Vegetable.color
        property_mass = self.MODULE_LIST['OOP_podstawy'].Vegetable.mass
        self.assertEqual(type(property_mass), property)
        self.assertEqual(type(property_color), property)
        assert 'coefficients' not in [
            x[0] for x in inspect.classify_class_attrs(self.MODULE_LIST['OOP_podstawy'].Polynomial)
        ]

    @Module('OOP_podstawy')
    def test_property_mention(self):
        # language=regexp
        property_regex = [r'@property\n[\s]+def (?P<name>[\w]+)\(self\):',
                          r'@(?P<name2>[\w]+)\.setter\n[\s]+def (?P<name3>[\w]+)\(self, [\w\s:\[\],.]+\):']
        matches = []
        for regex in property_regex:
            matches.append(re.findall(regex, self.MODULE_CODE))
        print(matches)
        self.assertIsNotNone(matches[0])
        self.assertIsNotNone(matches[1])
        for i in range(0, len(matches[0])-1):
            varname = matches[0][i]
            for property_name in matches[1][i]:
                self.assertEquals(varname, property_name)

    @Module('OOP_dziedziczenie_i_wiecej')
    def test_inheritace_classes(self):
        self.assertHasClass('Plant')
        self.assertHasClass('Vegetable2', ['Plant'])
        self.assertHasClass('Apple', ['Plant'])
        self.assertHasClass('T34', ['Tank'])
        self.assertHasClass('Tank', ['BattleUnit', 'Vehicle'])

    @Module('OOP_dziedziczenie_i_wiecej')
    def test_abstract_class(self):
        # language=regexp
        self.assertHasClass('MovingObject', ['ABC'])
        # language=regexp
        self.assertHasString('@abstractmethod\n[ ]+def ([\w]+)\(self\):', ['move'])
        self.assertRaises(TypeError, self.MODULE_LIST['OOP_dziedziczenie_i_wiecej'].MovingObject)
        # ^ here callable means INSTANCE OF A FUNCTION, NOT FUNCTION CALL ITSELF

    @Module('OOP_dziedziczenie_i_wiecej')
    def test_diamond_conflict(self):
        classlist = [
            self.MODULE_LIST['OOP_dziedziczenie_i_wiecej'].T34,
            self.MODULE_LIST['OOP_dziedziczenie_i_wiecej'].Vehicle,
            self.MODULE_LIST['OOP_dziedziczenie_i_wiecej'].Tank,
            self.MODULE_LIST['OOP_dziedziczenie_i_wiecej'].BattleUnit,
            self.MODULE_LIST['OOP_dziedziczenie_i_wiecej'].MovingObject
        ]
        sampletank = self.MODULE_LIST['OOP_dziedziczenie_i_wiecej'].T34()
        # print(sampletank.move)
        for cls in classlist:
            if type(sampletank) != cls:
                # piece of code to check if method is overriden from superclass or is left as-is
                assert sampletank.move.__code__ != cls.move.__code__, \
                    f'{sampletank.__class__} has not overriden move() method from a superclass!' \
                    f' It is the same as in {cls}'
            assert isinstance(sampletank, cls)

    @Module('OOP_dziedziczenie_i_wiecej')
    def test_bases_implemented(self):
        vege1 = self.MODULE_LIST['OOP_dziedziczenie_i_wiecej'].Vegetable2('blue', 59)
        plant = self.MODULE_LIST['OOP_dziedziczenie_i_wiecej'].Plant
        bases = vege1.__bases__()
        assert plant in bases

    @Module('OOP_dziedziczenie_i_wiecej')
    def test_compareable_polynomial(self):
        poly_basic = self.MODULE_LIST['OOP_podstawy'].Polynomial(1, 3, 5, 8)
        poly_comp = self.MODULE_LIST['OOP_dziedziczenie_i_wiecej'].ComparablePolynomial(2, 4, 7)
        bases = poly_comp.__class__.__bases__
        assert poly_basic.__class__ in bases
        methodlist = ['__str__', '__len__', '__lt__', '__gt__', '__eq__', '__repr__', '__add__']
        for method in methodlist:
            # method check
            assert hasattr(poly_comp, method)
            # next is method overriding check, similar logic as in test_diamond_conflict
            # what is different, is that we check if the method is implemented in base class first
            # if the method is not defined in base class at all, it means it is a new addition
            # we can check it by invoking type(getattr(class, magic_method_name))
            # normally we wouldn't make this check, but for every magic method - the implementation exists
            # in the form of a so called "method-wrapper" class
            # if we don't check against it, the usual __code__ check will fail, as there is no __code__ object
            # under the hood when method is invoked, but the method itself exist
            #
            # some light can be cast when we take a look at the following link:
            # https://stackoverflow.com/questions/10401935/python-method-wrapper-type
            if str(type(getattr(poly_basic, method))) != '<class \'method-wrapper\'>':
                assert getattr(poly_comp, method).__code__ != getattr(poly_basic, method).__code__, \
                    f'{poly_comp.__class__} has not overriden {method} method from a superclass!\n' \
                    f' It is the same as in {poly_basic.__class__}'

    @Module('generatory_i_iteratory')
    def test_basic_generators(self):
        generators = ['generator1',
                      'multiple_yield_generator',
                      'infinite_yield_generator',]
        for func_name in generators:
            self.assertHasFunction(function_name=func_name)


if __name__ == '__main__':
    unittest.main()
