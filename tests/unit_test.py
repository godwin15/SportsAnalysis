import unittest
from soccer import inputNumber, leaguefixtures, fixturedf, fixturechoice, teamIDs, headtohead, dataframeheadtohead, wins_draws, probability

data = symbols_json()
symb_dict = symbols_dic(data)
data_2 = convertion_json('USD', 'BTC')
    
class TestFileName(unittest.TestCase):
 
    #testing if it returns a dictionary
    def test_function1(self):
      
        self.assertEqual(type(data), dict)
        self.assertIsNotNone(data)
       
    #testing if it returns a dictionary
    def test_function2(self):
      
        self.assertEqual(type(symb_dict), dict)
        self.assertIsNotNone(symb_dict)
         
    def test_function3(self):
         
        for_int_val = test_input1(123)
        for_float_val = test_input1(12.34)
        for_str_val = test_input1('str')
        for_list_val = test_input1([1, '2', True])
         
        self.assertEqual(for_int_val, True)
        self.assertEqual(for_float_val, True)
        self.assertEqual(for_str_val, False)
        self.assertEqual(for_list_val, False)
         
    def test_function4(self):

        for_int_val = test_input2(123, symb_dict)
        for_float_val = test_input2(12.34, symb_dict)
        for_str_val = test_input2('str', symb_dict)
        for_list_val = test_input2([1, '2', True], symb_dict)
        for_correct_val = test_input2('USD', symb_dict)
        for_incor_val = test_input2('NTT', symb_dict)

        self.assertEqual(for_int_val, False)
        self.assertEqual(for_float_val, False)
        self.assertEqual(for_str_val, False)
        self.assertEqual(for_list_val, False)
        self.assertEqual(for_correct_val, True)
        self.assertEqual(for_incor_val, False)
      
      
    def test_function5(self):

        for_int_val = test_input3(123, 123, symb_dict)
        for_float_val = test_input3(12.34, 23.3, symb_dict)
        for_str_val = test_input3('str', 12, symb_dict)
        for_list_val = test_input3([1, '2', True], 121, symb_dict)
        for_correct_val = test_input3('BTC', 'USD', symb_dict)
        for_incor_val = test_input3('NTT', 'USE', symb_dict)

        self.assertEqual(for_int_val, False)
        self.assertEqual(for_float_val, False)
        self.assertEqual(for_str_val, False)
        self.assertEqual(for_list_val, False)
        self.assertEqual(for_correct_val, True)
        self.assertEqual(for_incor_val, False)
      
   
    # testing if it returns a dictionary
    def test_function4(self):
        data_2 = convertion_json('USD', 'BTC')
        self.assertEqual(type(data_2), dict)
        self.assertIsNotNone(data_2)
        
    def test_function5(self):
        final_amont = final_cal(data_2, 12.34, "BTC")
        self.assertIsNone(final_amont)