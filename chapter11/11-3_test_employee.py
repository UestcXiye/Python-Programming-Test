import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """针对Employee类的测试。"""

    def setUp(self):
        """
        创建一个雇员，供使用的测试方法使用。
        """
        firstname = 'San'
        lastname = 'Zhang'
        annualSalary = 10000
        self.my_employee = Employee(firstname, lastname, annualSalary)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 15000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(added_annual_salary=10000)
        self.assertEqual(self.my_employee.annual_salary, 20000)


if "__name__" == '__main__':
    unittest.main()
