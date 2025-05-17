#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_b.question_b import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_sample_case(self):
        result = get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT")
        self.assertEqual(result, (2, 4, 10))
