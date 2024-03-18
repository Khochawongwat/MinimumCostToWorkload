def min_cost_knapsack(workloads, costs, num_machines, target_work):
    assert num_machines == len(workloads) == len(costs), f'The number of workloads and costs must be the same as the number of machines {num_machines} {len(workloads)} {len(costs)}'
    
    # max workload is added because the total workload can be negative and we want to avoid negative indices
    max_workload = max(workloads)
    # Get possible workloads from target_work + max_workload down to -max_workload
    dp = [float('inf')] * (target_work + 2 * max_workload +  1)

    #Base case for the dp array is when the total workload is 0, the cost is 0.
    dp[max_workload] = 0
    
    for machine_index in range(num_machines):
        # Iterate over all possible total workloads from target_work + max_workload down to -max_workload
        for total_workload in range(target_work + max_workload, -max_workload - 1, -1):
            # Calculate the cost of adding the current machine's work
            cost_with_current_machine = costs[machine_index] + dp[total_workload - workloads[machine_index]]

            # We pick if the current cost is lower than the cost with the current machine because we want to minimize the cost
            dp[total_workload] = min(dp[total_workload], cost_with_current_machine)

    # Return the minimum cost that exceeds or equals to the target work
    return dp[target_work + max_workload] if dp[target_work + max_workload] != float('inf') else -1

num_machines = 10
workloads = [x for x in range(1, num_machines + 1)]
costs = [60, 100, 120, 130, 150, 10, 20, 30, 40, 50] # Random costs
target_work = sum(workloads)//2 

# I want to get the minimum cost that exceeds or equals to the target work.
print(min_cost_knapsack(workloads, costs, num_machines, target_work))