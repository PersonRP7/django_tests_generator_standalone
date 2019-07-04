from unittest import TestCase, main
import mts_functional as mts

class TestMakeTestStandalone(TestCase):

    def test_set_app_name(self):
        response = mts.set_app_name()
        self.assertEqual(
            response,
            "one"
        )

    def test_set_test_name(self):
        response = mts.set_test_name()
        self.assertEqual(
            response,
            "views"
        )

    def test_exiting(self):
        response = mts.exiting()
        self.assertEqual(
            response,
            0
        )

    def test_program_runner(self):
        response = mts.program_runner()
        self.assertEqual(
            response,
            None
        )

if __name__ == "__main__":
    main()
