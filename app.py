import subprocess
import random
import time
import data


def speak(text):
    """
    To make the system speak

    Parameters:
    text(string): What system has to speak

    Returns: None
    """
    subprocess.call(["say", text])


def introduction():
    """
    To introduce the player to the game

    Returns: None
    """
    text = (
        "Hi, My name is Machine Man, and i am your instructor for this game."
        " In this I will say a word and you will have to write the spelling "
        "of that word. You will get {positive_mark} points for each correct spelling and {negative_mark} "
        "if you spelled the word wrong. I will say {total_count} words in total. Let's see "
        "how much you can score. So let's get started."
    ).format(positive_mark=data.points_for_correct_answer, negative_mark=data.points_for_wrong_answer, total_count=data.no_of_words)
    speak(text)


if __name__ == "__main__":
    introduction()
    print("* You can type 'quit' to quit the game.")

    points = 0
    # Fetching the required number of words from the list of words
    word_list = random.sample(data.words, k=data.no_of_words)

    # Loop to get the user's input for each selected word
    for i in range(data.no_of_words):
        # Selecting a word at random from the list of fetched words
        word = random.choice(word_list)
        # Removing the selected word from the list so that it's not selected again
        word_list.remove(word)

        # Saying the word for the user
        text = f"Tell the Spell. The word is {word}"
        speak(text)
        # Taking user's input.
        answer = input("->")
        # Checking for the correctness of user's responce
        # And increasing or decreasing the points based on responce
        # And if the user enter's `quit`, will break out of loop immediately
        if answer.lower() == word.lower():
            text = "Well Done. That was correct."
            speak(text)
            points += 10
            time.sleep(0.3)
            text = f"Score increased by {data.points_for_correct_answer} points."
            speak(text)
            time.sleep(0.3)
        elif answer.lower() == "quit":
            break
        else:
            text = f"No. that's not the correct spelling for, {word}"
            speak(text)
            points -= 2
            time.sleep(0.3)
            text = f"Score decreased by {data.points_for_wrong_answer * -1} points."
            speak(text)
            time.sleep(0.3)

    # If the user has completed the game, giving some responce to the
    # user based on the score he got
    if answer.lower() != "quit":
        if points == data.total_points:
            text = "Well Done. You got all the answers right."
        elif points < 0:
            text = "Sorry buddy, but you need to work hard."
        else:
            text = f"Your final score is {points}"

        speak(text)
        time.sleep(0.3)

    # End Screen Message
    print("Final Score: ", points)
    text = "Thanks for playing. See you next time."
    speak(text)
