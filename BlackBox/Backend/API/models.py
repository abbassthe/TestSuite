from django.db import models

import dspy
import os

api_key = "AIzaSyBYEmC0DnXLqEUaH1gg0try7iWFX3S7QAk"


gemini = dspy.Google("models/gemini-1.5-flash", api_key=api_key)

dspy.settings.configure(lm=gemini, max_tokens=1024)
class TestGenerator(dspy.Signature):
    """ A generator that uses Gemini to generate unittest."""
    code = dspy.InputField(desc = " Function with test case and output.")
    unittest = dspy.OutputField(desc = "Given the following Python function, test case and expected output, generate only a minimal unit test using the unittest framework. "
            "Do not include any extra explanation or code. Just return the unittest code. "
            "The function to test with test case and output is: {code} ### Expected unittest output: ")
class DocGenerator(dspy.Signature):
    """ A generator that uses Gemini to generate docstrings."""
    code = dspy.InputField(desc = " Function with test case and output.")
    docstring = dspy.OutputField(desc = "Given the following Python function, write a docstring in the specified format. "
            "Do not include any other code or explanations."
            "Insert the docstring between the function signature and the function body. "
            "Return only the function with the docstring inserted, without the given testcase, the output and any additional line of code in the code i'm giving you."
            "Do not return the function call(the test case)"
            "Do not return any additional line of code, like variable definitions not relevant to the definition of the function, even if present in {code}"
            "Use the following format for the docstring:\n"
            '"""\n'
            "Function brief description.\n\n"
            "Parameters:\n"
            "variable Name (type): Description of the first parameter.\n"
            "variable Name (type): Description of the second parameter.\n\n"
            "Returns:\n"
            "return type: Description of the return value.\n"
            '"""\n'
            "The function is: {code} ### Expected function with docstring output: ")
test = dspy.Predict(TestGenerator)
doc = dspy.Predict(DocGenerator)
