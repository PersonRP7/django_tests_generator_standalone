import sys
import os

app_name = ""
test_name = ""

def set_app_name():
    app_input = str(input("app name? "))
    global app_name
    app_name += app_input
    return app_input

def set_test_name():
    test_input = str(input("test name? "))
    global test_name
    test_name += test_input
    return test_input

def see_if_tests_dir_reachable():
    try:
        tests = os.listdir(f'./{app_name}/tests')
        return True
    except FileNotFoundError:
        sys.stderr.write(
"""Either the app doesn't exist
or the tests dir is misconfigured.
The app has to include a 'tests'
folder with an '__init__.py' inside."""
        )
        return False

def see_if_test_already_exists():
    test_dir = os.listdir(f"./{app_name}/tests")
    print(test_dir)
    if f"test_{test_name}.py" in test_dir:
        sys.stderr.write(
            f"{test_name} already exists."
        )
        return True
    else:
        return False

def ask_user_if_he_wants_to_overwrite_test():
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

def create_test():
    pth = os.path.abspath(
        os.path.join(
            app_name,
            f"tests/test_{test_name}.py"
        )
    )
    with open(pth, "w") as outbound:
        outbound.write(
f"""from django.test import TestCase, RequestFactory
from django.urls import reverse

class Test{test_name}(TestCase):

    def test_():
        pass
"""
        )
    sys.stdout.write(
        f"{test_name} created."
    )

def exiting():
    sys.stdout.write("Exiting.")
    print("printing")
    return 0

def program_runner():
    set_app_name()
    set_test_name()
    if see_if_tests_dir_reachable():
        if see_if_test_already_exists():
            if ask_user_if_he_wants_to_overwrite_test():
                create_test()
            else:
                exiting()
        else:
            create_test()

if __name__ == "__main__":
    program_runner()
