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

- The **consensus motif**
- The **score** (lower score = better consensus)
- The list of **best motifs** found

---

#### Greedy Motif Search

  bash
```python greedy_motif_search_with_pseudocounts.py```

#### Randomized Motif Search

  bash
```python randomized_motif_search.py```

#### Gibbs Sampler Motif Search 

  bash
```python randomized_motif_search_with_gibbs_sampler.py```

You can change the default parameters (k, t, and N) directly in each script's function call at the bottom.

---

## 🧠 Algorithm Overviews

### Greedy Motif Search

- Iteratively builds a motif set by choosing the most probable k-mer using a profile.
- Fast and deterministic, but may get stuck in local optima.

### Randomized Motif Search

- Starts with random k-mers, updates motifs using profiles until convergence.
- Repeated multiple times to improve chances of a better result.

### Gibbs Sampling

- Iteratively refines motifs by randomly sampling one at a time based on profiles.
- Often yields better motifs with enough iterations.

---

## 👤 Author

Heitor Gelain do Nascimento
Email: heitorgelain@outlook.com
GitHub: @heitor-sg5

---

## 🧪 Example Output

Consensus: GAAAAAAATTTTTTT

Score: 2

Best Motifs: 
'CAAAAAAATTTTTTT', 
'GAAAAAAATTTTTTT', 
'GAAAAAAATTTTTTT', 
'CAAAAAAATTTTTTT', 
'GAAAAAAATTTTTTT', 
'GAAAAAAATTTTTTT'
