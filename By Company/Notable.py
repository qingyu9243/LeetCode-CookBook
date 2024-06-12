"""
Problem: Doctors often verbally dictate their clinical note after seeing a patient. These
dictations are transcribed word-for-word and then formatted to generate the final note. As part
of their dictation, doctor’s need a simple way to insert numbered lists. To accomplish this, we
have provided the doctor with some phrases that they can say in order to indicate the start of a
numbered list and every next item.
To start a numbered list, the doctor would say “Number n”, where n is a number from one to
nine, then say what they would want as the nth item in the numbered list. To indicate the start
of the next item in the numbered list, the doctor would say “Number next”, then say what they
would want as the next item in the numbered list. For example, the “Number next” item after
saying the “Number one” item would be the second item in the numbered list. The doctor
would then repeat the “Number next” steps until they reach the end of their numbered list.
The task is to write a function that takes in transcribed text as a string, applies the above
transformation to the text, and returns the transformed string.
For example, the input text from a doctor’s transcription:
Patient presents today with several issues. Number one BMI has increased by 10% since their
last visit. Number next patient reports experiencing dizziness several times in the last two
weeks. Number next patient has a persistent cough that hasn’t improved for last 4 weeks.
And the expected output would be:
Patient presents today with several issues.
1. BMI has increased by 10% since their last visit.
2. Patient reports experiencing dizziness several times in the last two weeks.
3. Patient has a persistent cough that hasn’t improved for last 4 weeks.
The function should be able to start from any number from one to nine. If the “Number n”
phrase is “Number three”, that item would be the third item and the following “Number
next” item would be the fourth item. The first letter in each item of the list should be
capitalized if it is not already capitalized, for example “Number one hello” should become “1.
Hello”.
You are free to use any languages, frameworks, libraries, etc that you’d like. With your
response, please include a zip file with your source code (preferably in a git repository), and
instructions for how to run the application locally.
"""