#!/usr/bin/python3
"""Write a method that determines if a
given data set represents a valid UTF-8 encoding."""

def validUTF8(data):
    """
    Number of bytes in the current UTF-8 character"""
    n_bytes = 0

    """For each integer in the data array"""
    for num in data:
        """Get the binary representation of the current byte"""
        bin_rep = format(num, '#010b')[-8:]

        """If this is the case then we have an incomplete character"""
        if n_bytes == 0:
            """Get number of 1s in the beginning of the binary representation
            to determine how many bytes the current UTF-8 character consists of"""
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            """1 byte characters must have the form 0xxxxxxx
            If this is not the case, then the input is invalid"""
            if n_bytes == 0:
                continue
            elif n_bytes > 4 or n_bytes == 1:
                return False

        else:
            """Else, the character is a continuation of the previous character
            # This means that its binary representation should have
            # the form 10xxxxxx"""
            if not (bin_rep.startswith('10')):
                return False

        """Decrement the number of bytes to process by 1
        # as we have processed the current byte"""
        if n_bytes:
            n_bytes -= 1

    """If we have an incomplete character left at the end, then the input is invalid"""
    return n_bytes == 0
 