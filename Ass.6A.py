# 0/1 Knapsack using Top-Down Dynamic Programming
# (Memoization)

def knapsack_top_down(weights, values, n, capacity, memo):

    # Base case
    if n == 0 or capacity == 0:
        return 0

    # Check if result is already calculated
    if memo[n][capacity] != -1:
        return memo[n][capacity]

    # If current item's weight is greater than capacity,
    # we cannot select it
    if weights[n - 1] > capacity:

        memo[n][capacity] = knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity,
            memo
        )

    else:
        # Option 1: Include the item
        include = values[n - 1] + knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity - weights[n - 1],
            memo
        )

        # Option 2: Exclude the item
        exclude = knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity,
            memo
        )

        # Choose the better option
        memo[n][capacity] = max(include, exclude)

    return memo[n][capacity]