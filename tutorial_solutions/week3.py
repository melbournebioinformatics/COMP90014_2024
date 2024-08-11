
import numpy as np

##################
### EXERCISE 1 ###
##################
def hamming(a, b):
    if len(a) != len(b):
        print('Input strings must be equal length')
        return
    
    hamming_distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            hamming_distance += 1
    
    return hamming_distance
    
    # # Another solution (compact)
    # assert len(a) == len(b), "Input sequences must be same length"
    # return sum(char_a != char_b for char_a, char_b in zip(a, b))


##################
### EXERCISE 2 ###
##################

# LIVE CODING #
def lev(a,b):
    """
    Recursively calculate Levenshtein distance between strings a and b.
    """
    
    global CALL_COUNT   # add this at the end
    CALL_COUNT += 1     # add this at the end

    if len(a)==0:
        return len(b)
    if len(b)==0:
        return len(a)
    
    if a[0]==b[0]:
        mismatch_cost = 0
    else:
        mismatch_cost = 1
    
    return min( 
        lev(a[1:],b[1:]) + mismatch_cost, # Case 1: Replace on first character
        lev(a[1:],b) + 1, # Case 2: Remove the first character
        lev(a,b[1:]) + 1 # Case 3: Insert first character
    )

# Add this to cell below to demonstrate how bad this scales
CALL_COUNT = 0 
lev("GATTACA","GACTATA")
print(CALL_COUNT)


##################
### EXERCISE 3 ###
##################
def levenshtein_distance(str1, str2):
    """
    Calculate the Levenshtein distance between two strings using dynamic programming.

    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    int: The Levenshtein distance between the two input strings.
    """
    len_str1 = len(str1)
    len_str2 = len(str2)
    
    # Initialize a matrix to store distances
    dist_matrix = np.zeros((len_str1 + 1, len_str2 + 1), dtype=int)
    
    # Initialize the first row and column of the matrix
    # Note: This bit only works because our penalty score is +1
    #       Think about how you would do this for idel penalties > 1
    for i in range(len_str1 + 1):
        dist_matrix[i, 0] = i
    for j in range(len_str2 + 1):
        dist_matrix[0, j] = j
    
    # Fill in the rest of the matrix
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            dist_matrix[i, j] = min(dist_matrix[i - 1, j] + 1,       # Deletion
                                    dist_matrix[i, j - 1] + 1,       # Insertion
                                    dist_matrix[i - 1, j - 1] + cost) # Substitution
    
    # The value at the bottom right corner of the matrix is the Levenshtein distance
    levenshtein_distance = dist_matrix[len_str1, len_str2]
    return levenshtein_distance


##################
### EXERCISE 4 ###
##################
def calculate_scoregrid(a, b,
                        indel_score=-1, match_score=2, mismatch_score=-1):
    """
    Given two strings a and b, calculate the maximum score grid, using
    specified scores for indels, matches and mismatches. Return the grid.
    Grid row and column 0 correspond to "before" the start of each string,
    so grid indexes are offset by 1 from string indexes. That is,
    grid position [1,1] represents the result of matching a[0] to b[0].
    """
    # The grid needs to be 1 bigger in each direction than the string lengths
    X = len(a)+1
    Y = len(b)+1
    scoregrid = np.zeros((X,Y), int)
    
    # You need to:
    # * initialise the top edge of grid, i.e. scoregrid[x,0] for all x, with indel scores
    # * initialise the left edge of grid, i.e. scoregrid[0,y] for all x, with indel scores
    # * loop over x and y, filling out each cell of the grid by looking for the
    #   maximum possible score from each of the three earlier cells
    
    # Fill out indel scores along the top and left edges
    # It's fine to do this with two for loops instead
    scoregrid[:,0] = list(range(0,indel_score*X,indel_score))
    scoregrid[0,:] = list(range(0,indel_score*Y,indel_score))
    for x in range(1,X):
        for y in range(1,Y):
            # Since we filled out the edges first and are working our way along each row,
            # we can assume that the three cells contibuting to (x,y) are already filled out
            if a[x-1]==b[y-1]: # Because our scoregrid is padded with zeros, coords are 1-indexed, whereas the sequences are 0-indexed
                diagonal_score = match_score
            else:
                diagonal_score = mismatch_score
            # Note maximum score, not minimum cost!
            score = max(scoregrid[x-1,y] + indel_score, # Left
                        scoregrid[x,y-1] + indel_score, # Up
                        scoregrid[x-1,y-1] + diagonal_score # Diagonal
                       )
            scoregrid[x,y] = score
    return scoregrid


##################
### EXERCISE 5 ###
##################

# A version with scores rather than costs, which can be specified
# Indels are scored per-base
def calculate_scoregrid_local(a, b, indel_score=-1, match_score=2, mismatch_score=-1):
    """
    Given two strings a and b, calculate the maximum score grid, using
    specified scores for indels, matches and mismatches. Return the grid.
    Grid row and column 0 correspond to "before" the start of each string,
    so grid indexes are offset by 1 from string indexes. That is,
    grid position [1,1] represents the result of matching a[0] to b[0].
    """
    # The grid needs to be 1 bigger in each direction than the string lengths
    X = len(a)+1
    Y = len(b)+1
    scoregrid = np.zeros((X,Y), int)

    # Fill out indel scores along the top and left edges; this will be zeros for local alignment
    # It's fine to do this with two for loops instead
    scoregrid[:,0] = [0] * X
    scoregrid[0,:] = [0] * Y
    for x in range(1,X):
        for y in range(1,Y):
            # Since we filled out the edges first and are working our way along each row,
            # we can assume that the three cells contibuting to (x,y) are already filled out
            if a[x-1]==b[y-1]:
                diagonal_score = match_score
            else:
                diagonal_score = mismatch_score
            # Note maximum score, not minimum cost!
            # The only addition with local alignment is that the score should be > 0
            score = max(scoregrid[x-1,y] + indel_score,
                        scoregrid[x,y-1] + indel_score,
                        scoregrid[x-1,y-1] + diagonal_score,
                        0)
            scoregrid[x,y] = score
    return scoregrid