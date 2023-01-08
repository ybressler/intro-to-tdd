"""Test methods for user input"""
from typing import Optional, Dict
import pytest

from user_input.interface import BaseInput
from user_input.user_input import get_user_name


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


def test_get_user_name_1(stubbed_input):
    """
    Unittests for get_user_name()

    Tests a single given name
    """
    response = get_user_name(stubbed_input)
    assert response == "Test User"


def test_get_user_name_2(stubbed_input):
    """
    Unittests for get_user_name() using multiple names
    """
    for name in ("Joe Test", "Joelle Test"):
        stubbed_input.mocked_responses["What is your name?"] = name  # this is a bit brittle tbh
        response = get_user_name(stubbed_input)
        assert response == name


@pytest.mark.parametrize('name', ["Joe Test", "Joelle Test"])
def test_get_user_name_3(stubbed_input, name: str):
    """
    Unittests for get_user_name() using multiple names, with
    parameterization
    """
    stubbed_input.mocked_responses["What is your name?"] = name
    response = get_user_name(stubbed_input)
    assert response == name


@pytest.mark.skip()
def test_get_user_name_5(stubbed_input):
    """
    What happens if we alter the scope of the stubbed_input >> for the whole module?

        @pytest.fixture(scope='module')
            def stubbed_input():
                pass

    This last test should now fail, since we are not re-instantiating the stubbed class.
    Don't rely on ordering of tests. Instead, limit the scope of the fixture.
    """
    response = get_user_name(stubbed_input)
    assert response == "Test User"