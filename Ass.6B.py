# 0/1 Knapsack using Bottom-Up Dynamic Programming
# (Tabulation)

def knapsack_bottom_up(weights, values, capacity):

    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):

        for w in range(1, capacity + 1):

            # Current item's weight
            item_weight = weights[i - 1]

            # Current item's value
            item_value = values[i - 1]

            if item_weight <= w:

                # Include the item
                include = (
                    item_value +
                    dp[i - 1][w - item_weight]
                )

                # Exclude the item
                exclude = dp[i - 1][w]

                # Select maximum
                dp[i][w] = max(include, exclude)

            else:

                # Cannot include the item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
