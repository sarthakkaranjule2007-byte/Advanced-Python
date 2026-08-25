# Longest Common Subsequence using Dynamic Programming

def lcs(sequence1, sequence2):
    m= len(sequence1)
    n= len(sequence2)

    # Create DP table
    dp = [[0 for j in range(n+1)] for i in range(m+1)]

    # Fill the DP table
    for i in range(1, m +  1):
        for j in range(1, n + 1):

            if sequence1[i - 1] == sequence2[j - 1]:

                dp[i][j] = dp[i - 1][j - 1] + 1

            else:

                dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])

    # Length of LCS
    lcs_length = dp[m][n]

    # Construct the LCS 
    i = m
    j = n
    result = []

    while i > 0 and j > 0:

        if sequence1[i - 1] == sequence2[j - 1]:

            result.append(sequence1[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:

            i -= 1

        else:

            j -= 1

    # Reverse the result 
    result.reserve()

    return lcs_length, ''.join(result)


# Main Program 

sequence1 = input("Enter first sequence: ")
sequence2 = input("Enter second sequece: ")

length, subsequence = lcs(sequence1, sequence2)

print("\nlongest Common Subsequence:", subsequence)
print("Length of LCS:", length)


