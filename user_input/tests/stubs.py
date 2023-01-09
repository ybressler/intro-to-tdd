"""Stubs for testing user input interface"""
from typing import Optional, Dict
import pytest

from user_input.interface import BaseInput


class StubbedInput(BaseInput):
    """
    Stubbed input class, stores mocked responses and
    serves them instead of asking the user for input
    """

    def __init__(self, mocked_responses: Dict[str, str] = {}):
        self.mocked_responses = mocked_responses

    def input(self, prompt: str) -> Optional[str]:
        """
        Returns a value from mocked responses, if the prompt is already stored.
        Otherwise, returns None
        """
        return self.mocked_responses.get(prompt)

@pytest.fixture()
def stubbed_input():
    """Returns stubbed input class"""
    return StubbedInput(
        # The following is a bit brittle, maybe we can bolster
        mocked_responses={
            "What is your name?": "Test User"
        }
    )