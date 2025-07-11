# Origin Search Algorithms

This repository contains implementations of several bioinformatics algorithms to find frequent k-mers with mismatches, clumps of k-mers, and origin of replication (ori) regions in genomic sequences using GC skew and mismatch-tolerant k-mer counting.

---

## 🧬 What is the Ori?

The origin of replication (ori) is a specific region in the genome where DNA replication begins. In bacteria, this region often contains conserved motifs such as DnaA boxes — short, recurring DNA sequences (k-mers) that signal the start of replication. Identifying these motifs helps pinpoint the ori location.

Another useful feature for locating the ori is the GC skew — the imbalance between guanine (G) and cytosine (C) nucleotides along the DNA strand. This skew tends to shift near the origin, providing a genomic landmark.

By combining GC skew analysis with searching for frequent k-mers allowing mismatches, this algorithm improves the accuracy of ori prediction.

---

## 📁 Files in This Repository

- `frequent_kmers_with_mismatches.py`: Finds frequent k-mers allowing up to d mismatches.
- `clump_finding.py`: Detects clumps of frequent k-mers within genomic windows.
- `ori_finder_with_gc_skew.py`: Locates origin of replication regions using GC skew and approximate k-mer matching.

---

## ⚙️ How to Use

### 1. Prepare Input

Input DNA sequences should be provided as plain text strings or FASTA files (for the ori finder file).

### 2. Run the Algorithms

Each script reads from the input file and prints:

- The **frequent k-mers** (pattern)
- The **counts**
- The **windows** were the k-mers are found

---

#### Frequent k-mer with Mismatches

  bash
```python frequent_kmers_with_mismatches.py```

#### Clump Finding

  bash
```python clump_finding.py```

#### Ori Finder with GC Skew

  bash
```python ori_finder_with_gc_skew.py```

Parameters like k (k-mer length), d (allowed mismatches), t (threshold count), and L (window length) are defined within each script but can be adjusted for your needs.

---

## 🧠 Algorithm Overviews

### Frequent k-mers with Mismatches

- Computes the frequency of all k-mers allowing up to d mismatches.
- Uses a neighborhood generation approach and mapping between k-mers and numbers.
- Returns the k-mers with the highest approximate frequency.
- Time complexity: O(n * k * 3^d + 4^k)

### Clump Finding

- Scans a genome with a sliding window of length L.
- Finds k-mers appearing at least t times within any window (forming clumps).
- Efficiently updates frequency counts when sliding the window.
- Time complexity: O(n * k + 4^k)

### Ori Finder with GC Skews

- Computes GC skew to locate potential replication origin regions.
- Within L windows around minimum GC skew, finds frequent k-mers with mismatches.
- Uses a simple GUI to load FASTA files and display results.
- Time complexity: O(n * k + N * 3^d * k)

---

## 🧪 Example Output

Window -500: positions 4083876:4084376
  
  Pattern: CCGGGATCC | Count: 4
  
  Pattern: TGTGGATAA | Count: 4

Window 0: positions 4084126:4084626
  
  Pattern: GATCTTCCG | Count: 3
  
  Pattern: CTTCCGGAA | Count: 3
  
  Pattern: TCCGGAATC | Count: 3
  
  Pattern: CCGGAATCT | Count: 3
  
  Pattern: TTTTGCGCC | Count: 3
  
  Pattern: GCACCGTGC | Count: 3

Window +500: positions 4084376:4084876
  
  Pattern: GATCGGGTT | Count: 3
  
  Pattern: ATCGGGTTT | Count: 3
  
  Pattern: GCACCGTGC | Count: 3
  
  Pattern: GCTGATAAG | Count: 3
  
  Pattern: AGCCGATCA | Count: 3
  

---

## 👤 Author

Heitor Gelain do Nascimento
Email: heitorgelain@outlook.com
GitHub: @heitor-sg5

---

## 📚 References

Bioinformatics Algorithms: An Active Learning Approach (Chapter 1) by
Phillip Compeau & Pavel Pevzner
https://bioinformaticsalgorithms.com
