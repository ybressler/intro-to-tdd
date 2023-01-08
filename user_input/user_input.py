"""Create interfaces for user input"""
from user_input.interface import BaseInput, PurePythonInput


def get_user_name(user_interface: BaseInput = PurePythonInput) -> str:
    """
    Ask a user what their name is
    """
    response = user_interface.input(prompt="What is your name?")

    return response

