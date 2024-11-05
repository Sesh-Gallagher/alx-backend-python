#!/usr/bin/env python3
"""
Module that tests for access_nested_map
"""
import requests
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestGetJson(unittest.TestCase):
    """
    Represents a TESTCASEto test the function for following inputs
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        method to test that utils.get_json returns the expected result
        """
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestAccessNestedMap(unittest.TestCase):
    """
    Represents a TESTCASE to test the function for following inputs
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """
        Represents a method to test that
        the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), answer)
        """
        Defines a test that a KeyError is raised for the following inputs
        """
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Represents a method to test that a KeyError is raised properly
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestMemoize(unittest.TestCase):
    """ Represents TESTCASE module"""
    def test_memoize(self):
        """
        Represents Test that when calling a property twice,
        the correct result is returned but a method is only
        called once using assert_called_once
        """
        class TestClass:
            """
            Defines a class
            """
            def a_method(self):
                """
                Defines method
                """
                return 42

            @memoize
            def a_property(self):
                """
                Defines property
                """
                return self.a_method()
        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert
