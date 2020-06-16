from helper import readAndCleanDoc
import numpy as np
import math


def findDistinctiveWords():
    # Change these 3 variables as you like
    doc_list = ['lecs/vidText_1.txt', 'lecs/vidText_2.txt', 'lecs/vidText_4.txt']  # List of files
    language_analyzing = 'english'                                  # Language to analyze
    nam_distinctive_words = 5                                       # Num of words
    distinctiveWords = {}
    doc_word, word_list = buildDocWordMatrix(doc_list, language_analyzing)
    tf = buildTFMatrix(doc_word)
    idf = buildIDFMatrix(doc_word)
    tf_idf = buildTFIDFMatrix(tf, idf)
    rows = len(doc_word[:])
    for r in range(0, rows):
        listDict = []
        index = np.argsort(-tf_idf[r])[0:nam_distinctive_words]
        for i in index:
            listDict.append(word_list[i])
        distinctiveWords[doc_list[r]] = listDict
    return distinctiveWords


def buildDocWordMatrix(doclist, language_analyzing):
    # Word lists for each cleaned doc
    word_list = []
    for document in doclist:
        tokensClean = readAndCleanDoc(document, language_analyzing)
        for words_indv_doc in tokensClean:
            if words_indv_doc not in word_list:
                word_list.append(words_indv_doc)
    word_list = sorted(list(word_list))
    # Word lists to build the doc word matrix
    doc_word_matrix = np.zeros([len(doclist), len(word_list)])
    count = 0
    for document in doclist:
        tokensClean = readAndCleanDoc(document, language_analyzing)
        for word in tokensClean:
            index = word_list.index(word)
            doc_word_matrix[count, index] += 1
        count += 1
    return doc_word_matrix, word_list


def buildTFMatrix(doc_word):
    rows = len(doc_word[:])
    col = len(doc_word[0][:])
    tfFunc = np.zeros([rows, col])
    for r in range(0, rows):
        for c in range(0, col):
            tfFunc[r, c] = doc_word[r, c] / np.sum(doc_word[r], axis=0)
    return tfFunc


def buildIDFMatrix(doc_word):
    rows = len(doc_word[:])
    col = len(doc_word[0][:])
    counting_Matrix = np.zeros([1, col])
    idf_Matrix = np.zeros([1, col])
    for r in range(0, rows):
        for c in range(0, col):
            if doc_word[r, c] != 0:
                counting_Matrix[0, c] += 1
    index = 0
    for value in counting_Matrix[0]:
        idf_Matrix[0, index] = math.log10(rows / value)
        index += 1
    return idf_Matrix


def buildTFIDFMatrix(tf, idf):
    tf_idf = np.array(tf * idf)
    return tf_idf


if __name__ == '__main__':
    distinctive_words_dict = findDistinctiveWords()
    for key in distinctive_words_dict:
        print("For the file " + key + " the distinctive words are:")
        print(distinctive_words_dict[key])
        print()

