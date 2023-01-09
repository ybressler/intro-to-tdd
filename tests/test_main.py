"""Tests for main executable"""
from main import run_program
from user_input.tests.stubs import stubbed_input  # import to activate the fixture


def test_run_program(stubbed_input):
    """Asserts that run program actually works"""
    result = run_program(stubbed_input)
