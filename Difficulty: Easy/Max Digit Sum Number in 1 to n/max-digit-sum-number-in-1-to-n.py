class Solution:
    def findMax(self, n):
        # code here
        # Helper function to compute the sum of digits
                def get_digit_sum(x: int) -> int:
                    return sum(int(d) for d in str(x))

                s = list(str(n))
                max_val = n
                max_sum = get_digit_sum(n)

                # Generate candidates by decrementing each digit position
                for i in range(len(s)):
                    if s[i] != '0':
                        # Create a modified copy of the digit array
                        curr = s.copy()
                        curr[i] = str(int(curr[i]) - 1)
                        for j in range(i + 1, len(s)):
                            curr[j] = '9'

                        # Convert the modified digits back to an integer
                        candidate = int("".join(curr))

                        # Filter out leading zeros causing candidate to be 0
                        if candidate > 0:
                            curr_sum = get_digit_sum(candidate)

                            # Update if a strictly larger digit sum is found
                            if curr_sum > max_sum:
                                max_sum = curr_sum
                                max_val = candidate
                            # In case of a tie, choose the larger number
                            elif curr_sum == max_sum:
                                max_val = max(max_val, candidate)

                return max_val