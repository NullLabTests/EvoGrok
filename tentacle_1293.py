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
            # Count the number of classes and ids in the HTML document
            class_count = len(re.findall(r'class\s*=', lowercase_input))
            id_count = len(re.findall(r'id\s*=', lowercase_input))
            return f"generic html document detected, class count: {class_count}, id count: {id_count}"
    
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
            # Reverse each item, lowercase it, and join them with semicolons
            reversed_items = [item[::-1].lower() for item in sorted_items]
            # Calculate the total length of all items and the average length
            total_length = sum(len(item) for item in reversed_items)
            average_length = total_length / len(reversed_items) if reversed_items else 0
            return f"reversed and sorted: {';'.join(reversed_items)}, total length: {total_length}, average length: {average_length:.2f}"
        elif input_data.isdigit():
            # If it's a single number, return its square, cube, factorial, prime factorization, and fibonacci number at that position
            number = int(input_data)
            factorial = math.factorial(number)
            factors = []
            n = number
            for i in range(2, int(math.sqrt(n)) + 1):
                while n % i == 0:
                    factors.append(i)
                    n //= i
            if n > 1:
                factors.append(n)
            
            # Calculate Fibonacci number
            a, b = 0, 1
            for _ in range(number):
                a, b = b, a + b
            fibonacci = a
            
            return f"square: {number ** 2}, cube: {number ** 3}, factorial: {factorial}, prime factorization: {' * '.join(map(str, factors)) if factors else '1'}, fibonacci: {fibonacci}"
        elif input_data.replace(' ', '').isalpha():
            # If it's a word (ignoring spaces), return its length, reverse, first three characters, vowel count, and most common letter
            lowercase_input = input_data.lower()
            vowels = sum(1 for char in lowercase_input if char in 'aeiou')
            letter_counts = {}
            for char in lowercase_input:
                if char.isalpha():
                    letter_counts[char] = letter_counts.get(char, 0) + 1
            most_common = max(letter_counts, key=letter_counts.get) if letter_counts else ''
            
            return f"length: {len(input_data)}, reverse: {input_data[::-1]}, first three: {input_data[:3]}, vowel count: {vowels}, most common letter: {most_common}"
        else:
            # For other inputs, reverse the string, convert to lowercase, remove non-alphanumeric characters,
            # and count the number of vowels, consonants, and digits
            reversed_cleaned = ''.join(char.lower() for char in input_data[::-1] if char.isalnum())
            vowels = sum(1 for char in reversed_cleaned if char in 'aeiou')
            consonants = sum(1 for char in reversed_cleaned if char.isalpha() and char not in 'aeiou')
            digits = sum(1 for char in reversed_cleaned if char.isdigit())
            
            return f"{reversed_cleaned}, vowel count: {vowels}, consonant count: {consonants}, digit count: {digits}"