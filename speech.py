import speech_recognition as sr
import pyttsx3
import re
import math


engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def solve_math(expression):
    
    if "sum" in expression or "add" in expression:
        try:
            numbers = [int(num) for num in re.findall(r"\d+", expression)]
            if len(numbers) >= 2:
                result = sum(numbers)
                return f"The sum is {result}"
            else:
                return "Please say at least two numbers to add."
        except Exception as e:
            return "I couldn't process the sum operation."

  
    elif "subtract" in expression or "minus" in expression:
        try:
            numbers = [int(num) for num in re.findall(r"\d+", expression)]
            if len(numbers) == 2:
                result = numbers[0] - numbers[1]  # Subtract the first number from the second
                return f"The result of subtraction is {result}"
            else:
                return "Please say two numbers to subtract."
        except Exception as e:
            return "I couldn't process the subtraction operation."

    elif "multiply" in expression or "times" in expression:
        try:
            numbers = [int(num) for num in re.findall(r"\d+", expression)]
            if len(numbers) == 2:
                result = numbers[0] * numbers[1]
                return f"The product is {result}"
            else:
                return "Please say two numbers to multiply."
        except Exception as e:
            return "I couldn't process the multiplication operation."

    
    elif "divide" in expression or "divided by" in expression:
        try:
            numbers = [int(num) for num in re.findall(r"\d+", expression)]
            if len(numbers) == 2:
                if numbers[1] != 0:
                    result = numbers[0] / numbers[1]
                    return f"The result of division is {result}"
                else:
                    return "Division by zero is undefined."
            else:
                return "Please say two numbers to divide."
        except Exception as e:
            return "I couldn't process the division operation."


    elif "square" in expression:
        try:
            number = int(re.search(r"square of (\d+)", expression).group(1))
            result = number ** 2
            return f"The square of {number} is {result}"
        except Exception as e:
            return "I couldn't process the square operation."
    elif "factorial" in expression:
        try:
            number = int(re.search(r"factorial of (\d+)", expression).group(1))
            result = math.factorial(number)
            return f"The factorial of {number} is {result}"
        except Exception:
            return "I couldn't process the factorial operation."


    elif "cube root of" in expression or "square root of" in expression:
        try:
            match = re.search(r"(\w+) root of (\d+)", expression)
            root_type = match.group(1)
            number = int(match.group(2))
            if "square" in root_type:
                result = math.sqrt(number)
            elif "cube" in root_type:
                result = number ** (1/3)
            else:
                return "Please specify square root or cube root."
            return f"The {root_type} root of {number} is {result}"
        except Exception:
            return "I couldn't process the root operation"

    try:
        allowed_chars = "0123456789+-*/.()"
        if all(char in allowed_chars for char in expression):
            result = eval(expression)
            return f"The result is {result}"
        else:
            return "Invalid input. Please use only numbers and basic math operations."
    except ZeroDivisionError:
        return "Division by zero is undefined."
    except Exception as e:
        return f"An error occurred: {e}"


def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("I am listening, please tell me a math problem.")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "There was an error in the voice recognition service."


def main():
    while True:
        question = get_voice_input()
        if "exit" in question.lower():
            speak("Goodbye!")
            break

        print(f"You said: {question}")
        result = solve_math(question)
        print(f"Answer: {result}")
        speak(result)

if __name__ == "__main__":
    main()
