import math
import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # Count the number of classes and ids in the HTML
            class_count = len(re.findall(r'class="[^"]*"', lowercase_input))
            id_count = len(re.findall(r'id="[^"]*"', lowercase_input))
            return f"generic html document detected with {class_count} classes and {id_count} ids"

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add its square, cube, square root, and logarithm
        result_str = str(result).lower()
        if isinstance(result, (int, float)):
            return f"{result_str}, square: {result**2}, cube: {result**3}, square root: {math.sqrt(abs(result)):.2f}, logarithm: {math.log(abs(result)):.2f}"
        else:
            return result_str
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item, lowercase it, capitalize the first letter, and join them
            processed_items = [item[::-1].lower().capitalize() for item in sorted_items]
            # Calculate the average length of the processed items
            avg_length = sum(len(item) for item in processed_items) / len(processed_items)
            return f"{','.join(processed_items)}, average length: {avg_length:.2f}"
        elif input_data.isdigit():
            # If it's a single number, return its square, cube, factorial, fibonacci number, and prime factorization
            number = int(input_data)
            factorial = math.factorial(number)
            fibonacci = sum(int((5**0.5 * (1 + 5**0.5)/2)**n - int((5**0.5 * (1 + 5**0.5)/2)**n)) for n in range(number+1))
            
            def prime_factorization(n):
                factors = []
                d = 2
                while n > 1:
                    while n % d == 0:
                        factors.append(d)
                        n //= d
                    d += 1
                    if d * d > n:
                        if n > 1:
                            factors.append(n)
                        break
                return factors
            
            prime_factors = prime_factorization(number)
            return f"square: {number ** 2}, cube: {number ** 3}, factorial: {factorial}, fibonacci: {fibonacci}, prime factors: {prime_factors}"
        elif input_data.replace(' ', '').isalpha():
            # If it's a word (ignoring spaces), return its length, reverse, first three characters, vowel count, and most common letter
            vowels = sum(1 for char in input_data.lower() if char in 'aeiou')
            most_common = max(set(input_data.lower()), key=input_data.lower().count)
            return f"length: {len(input_data)}, reverse: {input_data[::-1]}, first three: {input_data[:3]}, vowel count: {vowels}, most common letter: {most_common}"
        else:
            # For other inputs, reverse the string, convert to lowercase, remove non-alphanumeric characters,
            # count the number of vowels, calculate the sum of ASCII values of remaining characters,
            # and find the longest sequence of consecutive identical characters
            reversed_cleaned = ''.join(char.lower() for char in input_data[::-1] if char.isalnum())
            vowels = sum(1 for char in reversed_cleaned if char in 'aeiou')
            ascii_sum = sum(ord(char) for char in reversed_cleaned)
            
            longest_sequence = max(re.findall(r'(.)\1*', reversed_cleaned), key=len)
            longest_sequence_length = len(longest_sequence)
            
            return f"{reversed_cleaned}, vowel count: {vowels}, ascii sum: {ascii_sum}, longest sequence: {longest_sequence[0]} x {longest_sequence_length}"