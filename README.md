# Intro to Test Driven Development
How to write code well using tests (first).


<!--- Hidden for redundency
[![Intro to Test Driven Development](https://img.youtube.com/vi/JA2N1Id_npg/0.jpg)](https://www.youtube.com/watch?v=JA2N1Id_npg "Intro to Test Driven Development")
-->

### Watch Youtube Tutorial
[![Intro to Test Driven Development](https://markdown-videos.vercel.app/youtube/JA2N1Id_npg)]([https://youtu.be/JA2N1Id_npg](https://www.youtube.com/watch?v=JA2N1Id_npg "Intro to Test Driven Development"))


# Getting started:
* Create a virtual environment
* Install dependencies
* Run tests

```bash
# Create and activate a virtual env
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Now run tests
python -m pytest
```


## Functionality
Let's start with a project that has some abstract purpose,
that way it is easier to write code which "does stuff."

We will create a command line interface which will
ask a user for their name and their favorite food.
Our program will then write that result locally to a JSON
file. The program will then give the option to submit
another response or to see a summary of all responses.
Summary should read in all the responses and display info about them.

### Let's define that in more discrete functionalities:
* User input's name and favorite food
  * will we need validation on input?
* Response is saved locally as a JSON
  * eventually, may be saved to a DB, or cloud location (S3?)
* Responses need to be loaded in from local storage (or wherever)
* Function keeps running until it is killed.

### Approach
Let's create some barebone functions, describe their input, then create tests
for them. Initially, all of our tests should fail since our code doesn't do anything.

### 1. Interface to ask a user their name:
Our initial program should ask a user their name.
```
def get_user_name() -> str:
    response = input("What is your name?")
```
Q: But how can you test this? `input` requires a human to execute a command on the CLI...

A: Create an abstract interface to represent input:
```python
from abc import ABC, abstractmethod
import builtins


class BaseInput(ABC):

    @classmethod
    @abstractmethod
    def input(self, prompt: str) -> str:
        pass


class PurePythonInput(BaseInput):
    """
    Implements a pure python user interface for getting user input,
    using builtin.input
    """

    @classmethod
    def input(self, prompt: str) -> str:
        return builtins.input(prompt)
```
Now update the original function to use the `PurePythonInput` we just created:
```python lines
def get_user_name(user_interface: BaseInput = PurePythonInput) -> str:
    return user_interface.input(prompt="What is your name?")
    
```
Your code should still work (should still ask a human to enter their name).

Here's the magic part, here's how you can test that:

1. Create a stubbed input class to create "fake" behavior for
input:
```python
from typing import Optional, Dict
import pytest

from user_input.interface BaseInput  # Or wherever it's defined


class StubbedInput(BaseInput):
    """
    Stubbed input class, stores mocked responses and
    serves them instead of asking the user for input.
    
    Instantiate with a dictionary of mocked_responses.
    """

    def __init__(self, mocked_responses: Dict[str, str] = {}):
        """
        
        """
        self.mocked_responses = mocked_responses

    def input(self, prompt: str) -> Optional[str]:
        """
        Returns a value from mocked responses, if the prompt is already stored.
        Otherwise, returns None
        """
        return self.mocked_responses.get(prompt)
```
2. Create a fixture to use in your tests:
```python
import pytest

@pytest.fixture()
def stubbed_input():  
    return StubbedInput(
        mocked_responses={
            "What is your name?": "Test User"
        }
    )
```
3. Now write a test using the fixture:
```python
def test_get_user_name_(stubbed_input):
    """Unittests for get_user_name()"""
    response = get_user_name(stubbed_input)
    assert response == "Test User"
```
🎉 Tada!

> Note: There are some extra tests in [`test_user_input.py`](user_input/tests/test_user_input.py),
> so you should def take a look there and poke around and have fun.

----

### 2. Next Thing to test

