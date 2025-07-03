
def computing_frequencies(text, k):
    frequency_array = [0] * (4 ** k)

    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1

    return frequency_array

def clump_finding(genome, k, t, L):
    frequent_patterns = []
    clump = [0] * (4 ** k)

    text = genome[0:L]
    frequency_array = computing_frequencies(text, k)
    for i in range(4 ** k):
        if frequency_array[i] >= t:
            clump[i] = 1
    
    for i in range(1, len(genome) - L):
        first_pattern = genome[i-1:i-1+k]
        index = pattern_to_number(first_pattern)
        frequency_array[index] = frequency_array[index] - 1
        last_pattern = genome[i+L-k:i+L]
        index = pattern_to_number(last_pattern)
        frequency_array[index] = frequency_array[index] - 1
        if frequency_array[index] >= t:
            clump[index] = 1
    
    for i in range(4 ** k):
        if clump[i] == 1:
            pattern = number_to_pattern(i, k)
            frequent_patterns.append(pattern)
    
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


text = "CATTCAGGATCACGTTACCCCGAAAAAAAGGTACCAGGAGCTCTTCTCCTCTGCAGTCAGGTCTATAGAAACTACACCATTAACCTTCCTGAGAACCGGGAGGTGGGAATCCGTCACATATGAGAAGGTATTTGCCCGATAATCAATACTCCAGGCTTCTAACTTTTTCCACTCGCTTGAGCCGGCTTGGCCTTTCTGCCTGAAGATTCGTTGGACTGGTGCCAACGCGCAGGCATAGTTCCAGGAGAATTATCCGGGGGCAGTGACAACCAACATCTCGGGTCTTGCCCAACCGGTCTACACGCTGATATAGCGAATCACCGAGAACCCGGCGCCACGCAATGGAACGTCCTTAACTCTGGCAGGCAATTAAAGGGAACGTATATATAACGCAAAAAAACTGGAAAATTGGCGAGAGAATCTTCTCTCTGTCTATCGAAGAATGGCCACGCGGAGGCATGCGTCATGCTAGCGTGCGGGGTACTCTTGCTATCCATTTGGGTCACAGGACACTCGCTGTTTTCGAATTTACCCTTTATGCGCCGGTATTGAACCACGCTTATGCCCAGCATCGTTACAACCAGACTGATACTAGATGTATAATGTCCGCCATGCAGACGAAACCAGTCGGAGATTACCGAGCATTCTATCACGTCGGCGACCACTAGTGAGCTACTGGAGCCGAGGGGTAACGATGATGCCCCTAAGAACCTCTCGGTCGACGCAAGCGATTACACTCCTGTCACATCATAATCGTTTGCTATTCAGGGGTTGACCAACACCGGATAGCTTTTCACTTGAAGTATTATGCACGACAGGGTGCGTGTACCAACTAAACCTGTTTTAACTTACCTCAGACTAGTTGGAAGTGTGGCTAGATCTTAGCTTTCGTCACTAGAGGGCCCACGCTTAGTTTTTATGATCCATTGATCTCCTAGACGCTGCAAGATTTGCAACCAGGCAGACTTAGCGGTAGGTCCTAGTGCAGCGGGACTTTTTT"
k = 5
t = 4
L = 500
print(clump_finding(text, k, t, L))


