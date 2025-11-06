def add_binary_integers(A, B, n):
    """
    Add two n-bit binary integers stored in arrays A and B.
    
    Args:
        A: Array of n bits (LSB at index 0)
        B: Array of n bits (LSB at index 0)
        n: Number of bits
    
    Returns:
        C: Array of (n+1) bits representing sum (LSB at index 0)
    """
    C = [0] * (n + 1)  # Initialize result array with n+1 elements
    carry = 0
    
    for i in range(n):
        # Add corresponding bits and carry
        total = A[i] + B[i] + carry
        C[i] = total % 2      # Current bit is remainder
        carry = total // 2     # Carry is quotient
    
    C[n] = carry  # Store final carry
    
    return C


def add_binary_integers_verbose(A, B, n):
    """
    Add two n-bit binary integers with detailed output
    """
    print(f"Adding binary numbers:")
    print(f"A = {A} (LSB first)")
    print(f"B = {B} (LSB first)")
    print(f"\nBit-by-bit addition:\n")
    
    C = [0] * (n + 1)
    carry = 0
    
    for i in range(n):
        total = A[i] + B[i] + carry
        C[i] = total % 2
        new_carry = total // 2
        
        print(f"Position {i}:")
        print(f"  A[{i}] = {A[i]}, B[{i}] = {B[i]}, carry = {carry}")
        print(f"  Sum = {A[i]} + {B[i]} + {carry} = {total}")
        print(f"  C[{i}] = {C[i]}, new carry = {new_carry}")
        
        carry = new_carry
    
    C[n] = carry
    print(f"\nFinal carry: C[{n}] = {carry}")
    print(f"\nResult: C = {C}")
    
    return C


def binary_array_to_decimal(arr):
    """Convert binary array (LSB first) to decimal"""
    result = 0
    for i in range(len(arr)):
        result += arr[i] * (2 ** i)
    return result


def decimal_to_binary_array(num, length):
    """Convert decimal to binary array (LSB first)"""
    arr = []
    for i in range(length):
        arr.append(num % 2)
        num //= 2
    return arr


def binary_array_to_string(arr):
    """Convert binary array (LSB first) to binary string (MSB first)"""
    return ''.join(map(str, reversed(arr)))


# Test examples
print("="*70)
print("BINARY INTEGER ADDITION")
print("="*70)

# Example 1: 1011 (11) + 1101 (13) = 11000 (24)
print("\n### Example 1 ###")
A1 = [1, 1, 0, 1]  # 1011 in binary (11 in decimal)
B1 = [1, 0, 1, 1]  # 1101 in binary (13 in decimal)
n1 = 4

print(f"A represents: {binary_array_to_string(A1)} = {binary_array_to_decimal(A1)} (decimal)")
print(f"B represents: {binary_array_to_string(B1)} = {binary_array_to_decimal(B1)} (decimal)")

C1 = add_binary_integers_verbose(A1, B1, n1)

print(f"\nC represents: {binary_array_to_string(C1)} = {binary_array_to_decimal(C1)} (decimal)")
print(f"Verification: {binary_array_to_decimal(A1)} + {binary_array_to_decimal(B1)} = {binary_array_to_decimal(C1)} ✓")

print("\n" + "="*70)

# Example 2: 1111 (15) + 1111 (15) = 11110 (30)
print("\n### Example 2 ###")
A2 = [1, 1, 1, 1]  # 1111 in binary (15 in decimal)
B2 = [1, 1, 1, 1]  # 1111 in binary (15 in decimal)
n2 = 4

print(f"A represents: {binary_array_to_string(A2)} = {binary_array_to_decimal(A2)} (decimal)")
print(f"B represents: {binary_array_to_string(B2)} = {binary_array_to_decimal(B2)} (decimal)")

C2 = add_binary_integers_verbose(A2, B2, n2)

print(f"\nC represents: {binary_array_to_string(C2)} = {binary_array_to_decimal(C2)} (decimal)")
print(f"Verification: {binary_array_to_decimal(A2)} + {binary_array_to_decimal(B2)} = {binary_array_to_decimal(C2)} ✓")

print("\n" + "="*70)

# Example 3: 101 (5) + 011 (3) = 1000 (8)
print("\n### Example 3 ###")
A3 = [1, 0, 1]  # 101 in binary (5 in decimal)
B3 = [1, 1, 0]  # 011 in binary (3 in decimal)
n3 = 3

C3 = add_binary_integers(A3, B3, n3)

print(f"A = {A3} → {binary_array_to_string(A3)} = {binary_array_to_decimal(A3)}")
print(f"B = {B3} → {binary_array_to_string(B3)} = {binary_array_to_decimal(B3)}")
print(f"C = {C3} → {binary_array_to_string(C3)} = {binary_array_to_decimal(C3)}")
print(f"Verification: {binary_array_to_decimal(A3)} + {binary_array_to_decimal(B3)} = {binary_array_to_decimal(C3)} ✓")

## Pseudocode
# ADD-BINARY-INTEGERS(A, B, n)
#     // Initialize result array with n+1 elements
#     let C[0 : n] be a new array
#     carry = 0
    
#     // Add bits from right to left (but arrays store LSB first)
#     for i = 0 to n - 1
#         total = A[i] + B[i] + carry
#         C[i] = total mod 2        // Current bit
#         carry = ⌊total / 2⌋       // Carry for next position
    
#     C[n] = carry  // Store final carry bit
    
#     return C
