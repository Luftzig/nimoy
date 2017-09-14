from tests.nimoy.integration.base_integration_test import BaseIntegrationTest


class TestWhereBlocks(BaseIntegrationTest):
    def test_single_variable(self):
        spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            (a % 2) == 0
        
        with where:
            value_of_a = [2, 4, 6, 8]
        """

        result = self._run_spec_contents(spec_contents)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(result.testsRun, 4)

    def test_single_variable_with_single_value(self):
        spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            (a % 2) == 0
        
        with where:
            value_of_a = [2]
        """

        result = self._run_spec_contents(spec_contents)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(result.testsRun, 1)

    def test_single_variable_and_fail(self):
        spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            (a % 2) == 0
        
        with where:
            value_of_a = [4, 3]
        """

        result = self._run_spec_contents(spec_contents)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(result.testsRun, 2)

    def test_single_variable_with_single_value_and_fail(self):
        spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            
        with expect:
            (a % 2) == 0
        
        with where:
            value_of_a = [3]
        """

        result = self._run_spec_contents(spec_contents)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(result.testsRun, 1)

    def test_list_form_multi_variables(self):
        spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a = [2, 4, 6]
            value_of_b = [1, 3, 5]
            expected_value = [2, 12, 30]
        """

        result = self._run_spec_contents(spec_contents)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(result.testsRun, 3)

    def test_list_form_multi_variables_with_a_single_value(self):
        spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a = [2]
            value_of_b = [1]
            expected_value = [2]
        """

        result = self._run_spec_contents(spec_contents)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(result.testsRun, 1)

    def test_list_form_multi_variables_and_fail(self):
        spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a = [1, 2]
            value_of_b = [1, 1]
            expected_value = [1, 5]
        """

        result = self._run_spec_contents(spec_contents)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(result.testsRun, 2)

    def test_list_form_multi_variables_with_a_single_value_and_fail(self):
        spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a = [1]
            value_of_b = [1]
            expected_value = [5]
        """

        result = self._run_spec_contents(spec_contents)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(result.testsRun, 1)

    def test_matrix_form_multi_variables(self):
        spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a | value_of_b | expected_value
            2          | 1          | 2
            4          | 3          | 12
            6          | 5          | 30
        """

        result = self._run_spec_contents(spec_contents)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(result.testsRun, 3)

    def test_matrix_form_multi_variables_with_a_single_value(self):
        spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a | value_of_b | expected_value
            2          | 1          | 2
        """

        result = self._run_spec_contents(spec_contents)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(result.testsRun, 1)

    def test_matrix_form_multi_variables_and_fail(self):
        spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a | value_of_b | expected_value
            1          | 1          | 1
            2          | 1          | 10
        """

        result = self._run_spec_contents(spec_contents)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(result.testsRun, 2)

    def test_matrix_form_multi_variables_with_a_single_value_and_fail(self):
        spec_contents = """from nimoy.specification import Specification
        
class JimbobSpec(Specification):
    
    def test(self):
        with given:
            a = value_of_a
            b = value_of_b
            
        with expect:
            (a * b) == expected_value
        
        with where:
            value_of_a | value_of_b | expected_value
            2          | 1          | 10
        """

        result = self._run_spec_contents(spec_contents)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(result.testsRun, 1)