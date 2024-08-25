from django.db import models

import dspy
import os

api_key = "AIzaSyBYEmC0DnXLqEUaH1gg0try7iWFX3S7QAk"


gemini = dspy.Google("models/gemini-1.5-flash", api_key=api_key)

dspy.settings.configure(lm=gemini, max_tokens=1024)

class BasicQA(dspy.Signature):
    """Answer questions with short factoid answers."""
    question = dspy.InputField()
    answer = dspy.OutputField(desc="code and comments about unit test")

#Pass signature to Predict module
generate_answer = dspy.Predict(BasicQA)