# Carlos Martinez
# fxv013
# CS-3343-001
# Project2
# This project solves the "Two-Sum Problem" using the various aspects of algorithmic thinking such as the Brute Force Approach,
# the Use of the HashMap Approach, and Python programming discussed in class.

# Brute Force Approach: Checks all possible pairs of numbers in the list to find the pair that sums to the target.
def brute_force(nums, target):
    # Iterate through the list
    for i in range(len(nums) - 1):
        # Iterate through the list using the second pointer, starting from i+1 to avoid duplicate pairs
        for j in range(i + 1, len(nums)):
            # Check if the sum of the two numbers equals the target
            if nums[i] + nums[j] == target:
                # If a pair is found, return their indices
                return [i, j]
    # If no pair is found, return None
    return None


# Hash Map Approach:
def hash_approach(nums, target):
    # Create a dictionary to store numbers and their corresponding indices
    num_map = {}
    # Iterate through the list using enumerate to get both index and value
    for index, num in enumerate(nums):
        # Calculate the complement (the number needed to reach the target when added to the current number)
        complement = target - num
        # Check if the complement is already in the dictionary
        if complement in num_map:
            # If found, return the indices of the complement and the current number
            return [num_map[complement], index]
        # If not found, add the current number and its index to the dictionary
        num_map[num] = index
        # Print the current state of the hash table for debugging or visualization
        print(f"Adding to hash table: key:{num}, value:{index}")
    # If no pair is found, return None
    return None



def main():
    try:
        # Prompt the user to enter a list of numbers separated by spaces
        nums_input = input("Enter the input data array items:")
        # Convert the input string into a list of integers
        nums = list(map(int, nums_input.split()))
        # Ensure the list has at least 2 elements
        if len(nums) < 2:
            print("Input data must have at least 2 elements")

        # Prompt the user to enter the target value
        target = int(input("Enter the target value:"))

        # Execute the Brute Force Approach
        print("\nBrute Force Approach:")
        result_brute = brute_force(nums, target)
        # Check if a valid result was found
        if result_brute:
            # Print the indices of the two numbers that sum to the target
            print(f"Output: {result_brute[0]} {result_brute[1]}")
        else:
            # If no result was found, print "INVALID INPUT"
            print("INVALID INPUT")

        # Separator for better readability in the console output
        print("\n===========================================\n")

        # Execute the Hash Map Approach
        print("\nHash Approach:")
        result_hash = hash_approach(nums, target)
        # Check if a valid result was found
        if result_hash:
            # Print the indices of the two numbers that sum to the target
            print(f"Output: {result_hash[1]} {result_hash[0]}")
        else:
            # If no result was found, print "INVALID INPUT"
            print("INVALID INPUT")

    # Handle invalid input (e.g., non-integer values)
    except ValueError:
        print("Please enter valid integers for the array and target.")
    # Handle user interruption (e.g., pressing Ctrl+C)
    except KeyboardInterrupt:
        print("\nProgram terminated.")


# Entry point of the program
if __name__ == "__main__":
    main()