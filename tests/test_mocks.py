from unittest import mock, main, TestCase
from unittest.mock import patch
import mts_functional
from contextlib import contextmanager
import sys

@contextmanager
def mock_input(mock):
    original_input = __builtins__.input
    __builtins__.input = lambda _:mock
    yield
    __builtins__.input = original_input

class TestSimpleMock(TestCase):

    def test_app_one(self):
        with mock_input("one"):
            self.assertEqual(
                mts_functional.set_app_name(),
                "one"
            )

    def test_test_one(self):
        with mock_input("views"):
            self.assertEqual(
                mts_functional.set_test_name(),
                "views"
            )

    def test_ask_user_if_overwrite_y(self):
        with mock_input("y"):
            self.assertEqual(
                mts_functional.ask_user_if_he_wants_to_overwrite_test(),
                True
            )

    def test_ask_user_if_overwrite_Y(self):
        with mock_input("Y"):
            self.assertEqual(
                mts_functional.ask_user_if_he_wants_to_overwrite_test(),
                True
            )

    def test_ask_user_if_overwrite_n(self):
        with mock_input("n"):
            self.assertEqual(
                mts_functional.ask_user_if_he_wants_to_overwrite_test(),
                False
            )

if __name__ == "__main__":
    main()
