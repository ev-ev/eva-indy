"""
evaindy Test
"""

# Django
from django.test import TestCase


class TestEvaindy(TestCase):
    """
    EvaindyExample
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Test setup
        :return:
        :rtype:
        """

        super().setUpClass()

    def test_evaindy(self):
        """
        Dummy test function
        :return:
        :rtype:
        """

        self.assertEqual(True, True)
