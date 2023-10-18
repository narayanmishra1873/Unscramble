# Unscramble
#### Video Demo:
#### Description: https://youtu.be/VqzL67sAiFo

Typoglycemia: According to this principle, humans can comprehend text despite spelling errors and misplaced letters in the words as long as the first and the last letter are not misplaced.

I have made a game called "Unscramble" as my final project for CS50P using the above principle.
In this program, I have created two python files, one named project.py and the other named test_project.py

I have used a python library called "randfacts"

In python.py, I have implemented 1 "main" function and 3 other functions namely "scramble", "accuracy" and "get_length".
First, the "main" function is called.
It calls the "get_length" function.
In the "get_length" function, the user is asked to input the number corresponding to the length of the fact that he wants to generate.
This input is returned to the main function and stored in a variable called "fact_length".
Then, a random fact is generated according to the user preference.
Later, we get into "scramble" function and print the scrambled fact.
There are 5 cases while scrambling the words of the fact:
    1) If the word has only 1 letter then the word is printed as it is.
    2) If the word has 2 letters then the word is printed backwards.
    3) If the word has 3 or 4 letters then the 2nd and 3rd letter of the word are swapped.
    4) If the word has more than 4 letters then the first and the last letter are kept at their position while the others are scrambled
    5) If the word contains even one non charter which is not an alphabet then we make no changes to the word.

Now we ask the user to input their guess.
If guess matches the actual fact then we print "Correct!".
Else, we print "Incorrect." and we print the correct statement along with it.
Now, we go to the "accuracy" function and store its return value in a variable called "percentage_accuracy"
What the "accuracy" function does is that it calculates the number of correct words typed by the user and also the wrong words typed by the user. It calculates percentage accuracy using the formula (100*correct/(correct + wrong)) and then rounds it of upto 2 decimal places.
If the value of percentage_accuracy is greater than or equal to 90.00% then score, which was initially 0, is increased by 1 and the currect score is printed on the screen.
This continues in an infinite loop until the "percentage_accuracy" falls below 90.00%.
When that happens, the game ends and the final score of the user is printed on the screen.


In "test_project.py", I have used an additional library called mock and I have installed it using "pip install mock"
Here, I have tested the three functions in "project.py".