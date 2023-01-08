"""Entry point for our program"""
from user_input.interface import BaseInput, PurePythonInput
from user_input.user_input import get_user_name


def run_program(input_class: BaseInput):
    """Runs our program once"""
    user_name = get_user_name(input_class)

if __name__ == '__main__':

    run_program(PurePythonInput)
