text = input("Enter a dialog sentence: ").lower()

if text.endswith("?") or text.startswith(("what", "why", "when", "where", "who", "how")):
    act = "Question"

elif text.startswith(("please", "can you", "could you")):
    act = "Request"

elif text.startswith(("hello", "hi", "hey")):
    act = "Greeting"

elif text.startswith(("bye", "goodbye", "see you")):
    act = "Goodbye"

elif text.startswith(("yes", "okay", "ok", "sure")):
    act = "Agreement"

elif text.startswith(("no", "not", "never")):
    act = "Disagreement"

else:
    act = "Statement"

print("Dialog Act:", act)
