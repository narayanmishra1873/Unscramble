import randfacts
import random
import time


def main():
    score = 0
    fact_length = get_length()
    while(True):
        while(True):
            fact = randfacts.get_fact()
            words = fact.split(" ")
            no_of_words = len(words)
            if(fact_length == 1):
                if(no_of_words < 8):
                    break
            if(fact_length == 2):
                if(no_of_words >= 8 and no_of_words < 15):
                    break
            if(fact_length == 3):
                if(no_of_words > 15):
                    break
        print("The scrambled string: ")
        time.sleep(0.5)
        new_sentence = scramble(fact)
        guess = input("\nEnter the correct string: ")
        if(guess == fact):
            time.sleep(0.5)
            print("Correct!")
        else:
            time.sleep(0.5)
            print("Incorrect.")
            time.sleep(0.5)
            print("The correct statement was: " + fact)
        percentage_accuracy = accuracy(guess, fact)
        if(percentage_accuracy == None):
            percentage_accuracy = 0
        if(percentage_accuracy < 90):
            break
        else:
            score += 1
        time.sleep(0.5)
        print("Your score is: " + str(score) + "\n")

    time.sleep(0.5)
    print("\n-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
    time.sleep(0.5)
    print("Your accuracy has fallen below 90.0%")
    time.sleep(0.5)
    print("GAME ENDS")
    time.sleep(0.5)
    print("Your score is: " + str(score))
    time.sleep(0.5)
    print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-\n")







def scramble(fact):
    new_sentence = ""
    words = fact.split(" ")
    for word in words:
        if word.isalpha():
            letters = list(word)
            length = len(word)
            if length == 1:
                print(word, end = " ")
                new_sentence = new_sentence + " " + word
                continue
            if length == 2:
                temp = letters[0]
                letters[0] = letters[1]
                letters[1] = temp
                print("".join(letters), end = " ")
                new_sentence = new_sentence + " " + "".join(letters)
                continue
            if length == 3 or length == 4:
                temp = letters[1]
                letters[1] = letters[2]
                letters[2] = temp
                print("".join(letters), end = " ")
                new_sentence = new_sentence + " " + "".join(letters)
                continue
            a = letters[0]
            b = letters[length - 1]
            letters.pop(length - 1)
            letters.pop(0)
            random.shuffle(letters)
            letters.append(b)
            letters.insert(0, a)
            new_word = "".join(letters)
            print(new_word, end = " ")
            new_sentence = new_sentence + " " + new_word
        else:
            print(word, end = " ")
            new_sentence = new_sentence + " " + word
            continue
    return(new_sentence)


def accuracy(guess, fact):
    correct = 0
    wrong = 0
    wrong_words = []
    correct_words = []
    accuracy = 0
    guess_words = list(guess.split(" "))
    fact_words = list(fact.split(" "))
    length_guess = len(guess_words)
    length_fact = len(fact_words)
    if length_guess == length_fact:
        for i in range(length_guess):
            if(guess_words[i] == fact_words[i]):
                correct = correct + 1
            else:
                wrong = wrong + 1
                correct_words.append(fact_words[i])
                wrong_words.append(guess_words[i])
        accuracy = correct / (correct + wrong)
        time.sleep(0.5)
        print("Your accuracy is: " + str(round(accuracy * 100, 2)) + "%")
        for i in range(wrong):
            time.sleep(0.5)
            print(str(i + 1) + ". You have typed \"" + str(wrong_words[i]) + "\" instead of \"" + str(correct_words[i]) + "\"")
        return round(accuracy * 100, 2)
    else:
        time.sleep(0.5)
        print("You have not typed enough words")




def get_length():
    time.sleep(0.5)
    fact_length = int(input("Enter how long should the fact be:\nShort ---> Press 1\nMedium ---> Press 2\nLong ---> Press 3\n"))
    if(fact_length < 1 or fact_length > 3):
        fact_length = 2 # It will be treated as medium length
    return fact_length







if __name__ == "__main__":
    main()