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
            # Calculate the ratio of classes to ids
            ratio = class_count / id_count if id_count > 0 else float('inf')
            return f"generic html document detected, class count: {class_count}, id count: {id_count}, class/id ratio: {ratio:.2f}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add various mathematical operations
        result_str = str(result).lower()
        if isinstance(result, (int, float)):
            operations = {
                "square": result**2,
                "cube": result**3,
                "square root": math.sqrt(abs(result)),
                "logarithm": math.log(abs(result)) if result > 0 else float('nan'),
                "factorial": math.factorial(int(result)) if result.is_integer() and result >= 0 else float('nan'),
                "fibonacci": calculate_fibonacci(int(abs(result)))
            }
            formatted_operations = ", ".join(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}" for key, value in operations.items())
            return f"{result_str}, {formatted_operations}"
        else:
            return result_str
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item, lowercase it, and join them with semicolons
            reversed_items = [item[::-1].lower() for item in sorted_items]
            # Calculate the total length of all items, the average length, and the most common character
            total_length = sum(len(item) for item in reversed_items)
            average_length = total_length / len(reversed_items) if reversed_items else 0
            all_chars = ''.join(reversed_items)
            char_counts = {}
            for char in all_chars:
                char_counts[char] = char_counts.get(char, 0) + 1
            most_common_char = max(char_counts, key=char_counts.get) if char_counts else ''
            
            return f"reversed and sorted: {';'.join(reversed_items)}, total length: {total_length}, average length: {average_length:.2f}, most common character: {most_common_char}"
        elif input_data.isdigit():
            # If it's a single number, return various mathematical operations
            number = int(input_data)
            factorial = math.factorial(number)
            factors = prime_factorization(number)
            fibonacci = calculate_fibonacci(number)
            
            return f"square: {number ** 2}, cube: {number ** 3}, factorial: {factorial}, prime factorization: {' * '.join(map(str, factors)) if factors else '1'}, fibonacci: {fibonacci}"
        elif input_data.replace(' ', '').isalpha():
            # If it's a word (ignoring spaces), return various text analysis results
            lowercase_input = input_data.lower()
            vowels = sum(1 for char in lowercase_input if char in 'aeiou')
            letter_counts = {}
            for char in lowercase_input:
                if char.isalpha():
                    letter_counts[char] = letter_counts.get(char, 0) + 1
            most_common = max(letter_counts, key=letter_counts.get) if letter_counts else ''
            unique_letters = len(set(char for char in lowercase_input if char.isalpha()))
            
            return f"length: {len(input_data)}, reverse: {input_data[::-1]}, first three: {input_data[:3]}, vowel count: {vowels}, most common letter: {most_common}, unique letters: {unique_letters}"
        else:
            # For other inputs, reverse the string, convert to lowercase, remove non-alphanumeric characters,
            # and count the number of vowels, consonants, digits, and unique characters
            reversed_cleaned = ''.join(char.lower() for char in input_data[::-1] if char.isalnum())
            vowels = sum(1 for char in reversed_cleaned if char in 'aeiou')
            consonants = sum(1 for char in reversed_cleaned if char.isalpha() and char not in 'aeiou')
            digits = sum(1 for char in reversed_cleaned if char.isdigit())
            unique_chars = len(set(reversed_cleaned))
            
            return f"{reversed_cleaned}, vowel count: {vowels}, consonant count: {consonants}, digit count: {digits}, unique characters: {unique_chars}"

# Helper function to calculate Fibonacci number
def calculate_fibonacci(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

# Helper function to calculate prime factorization
def prime_factorization(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors