from unittest import main, TestCase
from unittest.mock import patch
import os
import mts_functional
import shutil
import pathlib

class TestMts(TestCase):

    def setUp(self):
        import pathlib
        pathlib.Path('./one/tests/').mkdir(
            parents = True,
            exist_ok = True
        )
        pathlib.Path(
            './one/tests/__init__.py'
        ).touch()

    def test_if_dir_reachable(self):
        response = mts_functional.see_if_tests_dir_reachable("one")
        self.assertEqual(
            response,
            True
        )

    def test_create_test(self):
        response = mts_functional.create_test("one", "views")
        self.assertEqual(
            response,
            "views created."
        )

    def test_exiting(self):
        response = mts_functional.exiting()
        self.assertEqual(
            response,
            0
        )


    def tearDown(self):
        shutil.rmtree("one")

class TestMtsExists(TestCase):

    def setUp(self):
        pathlib.Path('./one/tests').mkdir(
            parents = True,
            exist_ok = True
        )
        files = ['__init__.py', 'test_views.py']
        for file in files:
            pathlib.Path(
                f'./one/tests/{file}'
            ).touch()

    def test_if_test_already_exists_true(self):
        response = mts_functional.see_if_test_already_exists("one", "views")
        self.assertEqual(
            response,
            True
        )

    def test_if_test_already_exists_false(self):
        response = mts_functional.see_if_test_already_exists("one", "models")
        self.assertEqual(
            response,
            False
        )

    def tearDown(self):
        shutil.rmtree("one")


if __name__ == "__main__":
    main()
