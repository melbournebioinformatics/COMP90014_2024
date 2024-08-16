
#################
### Exercise 1 ##
#################

def extract_kmers(seq: str, k: int) -> set:
    '''
    Extract all kmers. Return Set of kmers.
    '''
    kmers = set()
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        kmers.add(kmer)
    return kmers

def jaccard(a: set, b: set) -> float:
    intersection = len(a.intersection(b))
    union = len(a.union(b))
    j = intersection / union
    return j

def true_jaccard_distance(seqA: str, seqB: str, k: int) -> float:
    kmersA = extract_kmers(seqA, k)
    kmersB = extract_kmers(seqB, k)
    j = jaccard(kmersA, kmersB)
    return j


#################
### Exercise 2 ##
#################

def minhash_sketch(seq: str, k: int, s: int) -> set:
    """
    Calulate minhash sketch from DNA sequence.
    """
    hashes = set()
    
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i + k]
        ckmer = get_canon(kmer)
        hash_value = dna_hash(ckmer)  
        hashes.add(hash_value)
    
    min_hashes = sorted(list(hashes))[:s]
    return set(min_hashes)


#################
### Exercise 3 ##
#################

def minhash_jaccard_distance(seqA: str, seqB: str, k: int, s: int) -> float:
    ### BEGIN SOLUTION
    sketchA = minhash_sketch(seqA, k, s)
    sketchB = minhash_sketch(seqB, k, s)
    j = jaccard(set(sketchA), set(sketchB))
    ### END SOLUTION
    return j 