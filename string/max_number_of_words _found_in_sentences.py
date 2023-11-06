def mostWordsFound(sentences):
    sentence_count = {}
    
    for sentence in sentences:
        words = sentence.split()
        words_count = len(words)
        sentence_count[sentence] = words_count
        words_max_number = max(sentence_count.values())
    # print(words_max_number)
    return words_max_number


sentences = ["alice and bob love leetcode best", "i think so too", "this is great thanks very much"]
mostWordsFound(sentences)
