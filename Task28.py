import re
def sentence(text: str) -> str:
    sentences = re.split(r"[.?!]\s*", text)
    first_words = [s.split()[0] for s in sentences if s]
    result_sentence = " ".join([first_words[0].capitalize()] + [w.lower() for w in first_words[1:]]) + "."
    return result_sentence

input_text = "Happy New Year! Wish you good luck. Please , write me how are you doing? Goodbye..."
print(sentence(input_text))


