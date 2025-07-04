
def computing_frequencies_with_mismatches(text, k, d):
    frequency_array = [0] * (4 ** k)

    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        neighbourhood = neighbours(pattern, d)
        for approximate_pattern in neighbourhood:
            j = pattern_to_number(approximate_pattern)
            frequency_array[j] += 1

    return frequency_array

def neighbours(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    
    neighbourhood = []
    suffix_neighbours = neighbours(pattern[1:], d)
    for text in suffix_neighbours:
        if hannings_distance(pattern[1:], text) < d:
            for x in ['A', 'C', 'G', 'T']:
                neighbourhood.append(x + text)
        else:
            neighbourhood.append(pattern[0] + text) 

    return neighbourhood
    
def hannings_distance(text, pattern):
    d = 0
    for i in range(len(text)):
        if text[i] != pattern[i]:
            d += 1
    return d

def faster_frequent_words(text, k, d):
    frequency_array = computing_frequencies_with_mismatches(text, k, d)
    max_count = max(frequency_array)
    
    frequent_patterns = []
    for i in range(4 ** k):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.append((pattern, max_count))
            
    return frequent_patterns

def pattern_to_number(pattern):
    if pattern == "":
        return 0
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)

def number_to_pattern(index, k):
    if k == 0:
        return ""
    prefix_index = index // 4
    r = index % 4
    symbol = number_to_symbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return prefix_pattern + symbol

def symbol_to_number(symbol):
    mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return mapping[symbol]

def number_to_symbol(number):
    mapping = ['A', 'C', 'G', 'T']
    return mapping[number]

text = "GTAGGATCGAATAAAATTTTTGACCTGGGCCTAGGACAAGGCCTCTTGTGGCTAAAATTTTTATCGGGTCTAGCTATTCAGGCGCCAAAATTTTTACTCGGATCGAGGGACTGCTAGCTCCGCATAAGATATAGCCAATGATTTGTGTGGTCACCTAGATGAAGCAGGGTTTCCGGTCCAGCCTTGTGCTAAAATTTTTCTTCACTGACGCCGAAAATTTTTGGCCAACGCTTTAAAATTTTTGGGCAAATAAAACAATGTTGGAAAATTTTTCATCTGTTTAGCAAAAATTTTTTGAGCTACTAAATGTATGCTTAATCCAGATGGTTCTAAGCTATGACGGGAAGTTGTGAAAATTTTTTCCTAGGATAGTCAAAATTTTTATTGCGGAGTTGAAAATTTTTGGGGGTATTGTGCGATCGGAAAAATTTTTTACACAGAAGAGGACAGGCGTGCTACATCAGAATTACCGACCTATTATGTCTACAGTTCAATGAAAATTTTTAGACGGGCGTTTCACCAACTACGCCCTAAAATTTTTGCAATATGTGGTAGCGGCCGATCAAAATTTTTCAGCTTCTAGTTGTCCCCTAATGGCAGGCCTCTCGAACGGCGTCATTTTGATGGCCCGCGCTGGCCTATTGGTCCATGTCATTCACTTGGTAACATGTTTTGGCAGGCACCTTTTGGATGTGTGTAAGCGTTCATAACATTATCATTCGTTCGCTGGAAAGTCTTCATAAGGCACTGATCGAGGGTCGGCCCCTCTATATTTCGTGTCCTCCAGTTAAAATTTTTATGACCGTTAAGGTCGAGAAAAATTTTTCCCCGTCTCTCTAACACAAAATTTTTTTCATTACATGTCTCTCCCACCCTATACCATGGCCGGCTATGTCATAACAGATACACGGCAATCAGTGGGTACACCCCGAATCCACGAACTCTACGAAGTGACAGCCGAGTCTGGAAACTGCCGGGTGGCGCGTGAGGGAAAAAAGAATTTCCCTGCGGTTTAGGCCACAAGGAAAATCGCGGCGTCGCCAGACTTCCAAAGCTTAAGACGCTCCCCCTTGCCGCTTACCTCTCCATAAAAATTTTTCCCAAGCTTGCTGCGCATACCTCCGTGCTCAAAATTTTTCGTAGTTTAAATATGGAAGTGAAGCGTGTTTGCTTCCGGA"

result = faster_frequent_words(text, k=9, d=1)
for pattern, count in result:
    print(f"Pattern: {pattern} | Count: {count}")
