def count_word_frequency(text):
    words = text.lower().split()
    word_counts = {}

    for word in words:
        word = word.strip(",.!?")
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def bubble_sort(word_list):
    n = len(word_list)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if word_list[j]["freq"] < word_list[j + 1]["freq"]:
                temp = word_list[j]
                word_list[j] = word_list[j + 1]
                word_list[j + 1] = temp

    return word_list


while True:
    text = input("Enter a sentence: ").strip()
    if text == "":
        print("Input cannot be empty. Please type a sentence.")
    else:
        break

word_counts = count_word_frequency(text)

word_list = []
for word, freq in word_counts.items():
    word_freq = {"word": word, "freq": freq}
    word_list.append(word_freq)

sorted_words = bubble_sort(word_list)

while True:
    top_n_input = input("How many top words would you like to see? ").strip()
    if not top_n_input.isdigit():
        print("Please enter a valid positive integer.")
        continue

    top_n = int(top_n_input)

    if top_n < 1:
        print("Please enter a number greater than 0.")

    break

print("Most common words:")
for i in range(min(top_n, len(sorted_words))):
    word_info = sorted_words[i]
    print(f'{i + 1}. "{word_info["word"]}" - {word_info["freq"]} times')