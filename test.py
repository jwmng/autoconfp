import unittest
from acp import AutoConfigParser


class TestAutoConfigParser(unittest.TestCase):
    def setUp(self):
        self.acp = AutoConfigParser()
        self.sec = 'test'
        self.opt = 'value'
        self.conf_str_pre = '[%s]\n%s=' % (self.sec, self.opt)

    def _assert_val_types(self, string_values, type_):
        for v in string_values:
            conf_str = self.conf_str_pre + v
            self.acp.read_string(conf_str)
            self.assertIsInstance(self.acp.get(self.sec, self.opt), type_)

    def test_int_values(self):
        int_values = ['1', '23', '49282', '0', '-8']
        self._assert_val_types(int_values, int)

    def test_float_values(self):
        float_values = ['1.0', '5e-3', '2e2', '-2e3', '3.88885', '-5.02e1']
        self._assert_val_types(float_values, float)

    def test_bool_values(self):
        bool_values = ['true', 'yes', 'on', 'false', 'no', 'off']
        self._assert_val_types(bool_values, bool)

    def test_unconverted(self):
        str_values = ['asdfasd', 'hello', 'nope', 'valse', 'nothing', 'zero']
        self._assert_val_types(str_values, str)


if __name__ == '__main__':
    unittest.main()
