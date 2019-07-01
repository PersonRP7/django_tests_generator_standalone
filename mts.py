import sys
import os

class Command:

    app_name = str(input("app name? "))
    test_name = str(input("test name? "))

    def see_if_tests_dir_reachable(self):
        try:
            tests = os.listdir(f'./{self.app_name}/tests')
            return True
        except FileNotFoundError:
            sys.stderr.write(
"""Either the app doesn't exist
or the tests dir is misconfigured.
The app has to include a 'tests'
folder with an '__init__.py' inside."""
            )
            return False

    def see_if_test_already_exists(self):
        test_dir = os.listdir(f"./{self.app_name}/tests")
        print(test_dir)
        if f"test_{self.test_name}.py" in test_dir:
            sys.stderr.write(
                f"{self.test_name} already exists."
            )
            return True
        else:
            return False

    def ask_user_if_he_wants_to_overwrite_test(self):
        user_input = str(input(
"""
Press y to overwrite,
press anything else to cancel:
 """
        ))
        if user_input == 'y' or user_input == 'Y':
            return True
        else:
            return False

    def create_test(self):
        pth = os.path.abspath(
            os.path.join(
                self.app_name,
                f"tests/test_{self.test_name}.py"
            )
        )
        with open(pth, "w") as outbound:
            outbound.write(
f"""from django.test import TestCase, RequestFactory
from django.urls import reverse

class Test{self.test_name}(TestCase):

    def test_(self):
        pass
"""
            )
        sys.stdout.write(
            f"{self.test_name} created."
        )

    def exiting(self):
        sys.stdout.write("Exiting.")
        return 0

    def program_runner(self):
        if self.see_if_tests_dir_reachable():
            if self.see_if_test_already_exists():
                if self.ask_user_if_he_wants_to_overwrite_test():
                    self.create_test()
                else:
                    self.exiting()
            else:
                self.create_test()

Command().program_runner()
