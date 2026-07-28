class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        # Edge case
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list for each row
        rows = [""] * numRows
        
        current_row = 0
        going_down = False
        
        # Traverse the string
        for char in s:
            rows[current_row] += char
            
            # Change direction at the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row
            if going_down:
                current_row += 1
            else:
                current_row -= 1
        
        # Join all rows
        return "".join(rows)