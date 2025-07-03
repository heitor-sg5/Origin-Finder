import tkinter as tk
from tkinter import filedialog
from collections import defaultdict

def reverse_complement(text):
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join(complement[base] for base in reversed(text))

def hamming_distance(s1, s2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 0:
        return {''}
    
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in "ACGT":
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)
    return neighborhood

def find_min_skew(text):
    skew = 0
    min_skew = (float('inf'), -1)
    for i, base in enumerate(text):
        if base == 'G':
            skew += 1
        elif base == 'C':
            skew -= 1
        if skew < min_skew[0]:
            min_skew = (skew, i)
    return min_skew[1]

def count_kmers(text, k):
    counts = defaultdict(int)
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        counts[kmer] += 1
    return counts

def find_frequent_kmers_with_mismatches(text, k, d):
    counts = count_kmers(text, k)
    frequent_patterns = defaultdict(int)
    processed = set()

    for kmer in counts:
        if kmer in processed:
            continue
        neighborhood = neighbors(kmer, d)
        total_count = 0
        for approx_kmer in neighborhood:
            rev_comp = reverse_complement(approx_kmer)
            total_count += counts.get(approx_kmer, 0)
            if rev_comp != approx_kmer:
                total_count += counts.get(rev_comp, 0)
            processed.add(approx_kmer)
            processed.add(rev_comp)
        frequent_patterns[kmer] = total_count

    if not frequent_patterns:
        return []

    max_count = max(frequent_patterns.values())
    return [(pattern, count) for pattern, count in frequent_patterns.items() if count == max_count]

def process_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a FASTA file",
        filetypes=[("FASTA files", "*.fasta *.fa *.fna *.txt"), ("All files", "*.*")]
    )
    if not file_path:
        print("No file selected.")
        return

    with open(file_path, 'r') as file:
        text = ''.join(line.strip() for line in file if not line.startswith(">"))

    print("Genome selected.")

    k = 9
    d = 1
    L = 500

    min_skew_pos = find_min_skew(text)
    windows = [
        (max(0, min_skew_pos - L), min_skew_pos, f"-{L}"),
        (max(0, min_skew_pos - L//2), min_skew_pos + L//2, "0"),
        (min_skew_pos, min(min_skew_pos + L, len(text)), f"+{L}"),
    ]

    for start, end, window_name in windows:
        print(f"\nWindow {window_name}: positions [{start}:{end}]")
        window_seq = text[start:end]
        frequent_kmers = find_frequent_kmers_with_mismatches(window_seq, k, d)
        if not frequent_kmers:
            print("  No frequent patterns found.")
        else:
            for pattern, count in frequent_kmers:
                print(f"  Pattern: {pattern} | Count: {count}")

process_file()
