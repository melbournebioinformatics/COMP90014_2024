
import mmh3


def get_canon(kmer):
    # Return the canonical kmer  
    
    if kmer <= kmer.reverse_complement():
        return kmer
    else:
        return kmer.reverse_complement()


def kmer_locs(sequence, k=5):
    # Get kmers from seq object
    # Output kmers and their location as (kmer,location) tuples.

    for i in range(len(sequence)-k+1):
        kmer = sequence[i:i+k]
        if 'N' in kmer:
            continue
        else:
            yield (kmer,i)


def build_hash_table(kmer_list, hash_table_size = 10):
    # Builds and returns kmer index as hash table.
    # Collisions resolved using linear probing. 

    # Hash canonical kmer and calc memory address
    def hash_function(kmer):
        ckmer = get_canon(kmer)
        kloc = mmh3.hash64(str(ckmer), seed=42, signed=False)[0] % hash_table_size
        return kloc

    hash_table = dict()

    # Unpack kmers and their genomic locations from the kmer_list
    for key, value in kmer_list:
        
        # Get memory location for kmer 
        hash_index = hash_function(key)
        
        # Check if index is occupied by same or different kmer
        while hash_index in hash_table:
            
            if hash_table[hash_index][0] == key:
                # If the key already exists, append the value to the list of values and break.
                hash_table[hash_index][1].append(value)
                #print(f'Key exists, adding value to list: {str(key),value}')
                break
                
            else:
                # If the key doesn't match, move to the next slot using linear probing.
                #print(f'Collison at {hash_index}: Update {key} hash to {hash_index + 1}')
                hash_index = hash_index + 1
                
                # Raise error if run out of room in table.
                if hash_index > hash_table_size - 1:
                    raise ValueError("Hash table overflow: Unable to insert the key-value pair.")

        # If the loop completes without finding a match, insert the (key, [value]) pair at the vacant slot.
        if hash_index not in hash_table:
            #print(f'Insert new key at index {hash_index}: {str(key),value}')
            hash_table[hash_index] = (key, [value])
    return hash_table   
    

def kmerLookup(key, hash_table={}, hash_table_size = 10):
    # Returns genomic locations for a given kmer (hash table key) in a pre-build index.
    # Collisions resolved using linear probing. 
    # If kmer key is not in index, returns empty list. 

    # Function to calculate the initial hash_index based on the provided key.
    def hash_function(kmer):
        ckmer = get_canon(kmer)
        kloc = mmh3.hash64(str(ckmer), seed=42, signed=False)[0] % hash_table_size
        return kloc

    # Calc initial hash_index from key
    hash_index = hash_function(key)
    
    # Keep searching until we find the key or we exhaust the entire hash table.
    while hash_index in hash_table:
        if hash_table[hash_index][0] == key:
            # If the key is found, return the corresponding value.
            return hash_table[hash_index][1]
        else:
            # If the key doesn't match, perform linear probing by incrementing the hash_index with an offset.
            hash_index = hash_index + 1

            # If we have searched the entire hash table and haven't found the key, return None.
            if hash_index > hash_table_size:
                return []

    # If the loop completes without finding the key, return None.
    return []


def mapKmers(read, hash_table={}, k=3, hash_table_size = 100):
    # extracts kmers from a query sequence and looks up their genomic locations using kmerLookup() function. 

    read_kmers = kmer_locs(read, k=k) 
    
    for key, value in read_kmers:
        for i in kmerLookup(key, hash_table=hash_table, hash_table_size = hash_table_size):
            yield (value, i)
