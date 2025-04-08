import math

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
            # Count the number of classes in the HTML document
            class_count = lowercase_input.count('class=')
            return f"generic html document detected, class count: {class_count}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add its square, cube, and square root
        result_str = str(result).lower()
        if isinstance(result, (int, float)):
            return f"{result_str}, square: {result**2}, cube: {result**3}, square root: {math.sqrt(abs(result)):.2f}"
        else:
            return result_str
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item, lowercase it, and join them with semicolons
            reversed_items = [item[::-1].lower() for item in sorted_items]
            # Calculate the total length of all items
            total_length = sum(len(item) for item in reversed_items)
            return f"reversed and sorted: {';'.join(reversed_items)}, total length: {total_length}"
        elif input_data.isdigit():
            # If it's a single number, return its square, cube, factorial, and prime factorization
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
            
            return f"square: {number ** 2}, cube: {number ** 3}, factorial: {factorial}, prime factorization: {' * '.join(map(str, factors)) if factors else '1'}"
        elif input_data.replace(' ', '').isalpha():
            # If it's a word (ignoring spaces), return its length, reverse, first three characters, and vowel count
            lowercase_input = input_data.lower()
            vowels = sum(1 for char in lowercase_input if char in 'aeiou')
            return f"length: {len(input_data)}, reverse: {input_data[::-1]}, first three: {input_data[:3]}, vowel count: {vowels}"
        else:
            # For other inputs, reverse the string, convert to lowercase, remove non-alphanumeric characters,
            # and count the number of vowels and consonants
            reversed_cleaned = ''.join(char.lower() for char in input_data[::-1] if char.isalnum())
            vowels = sum(1 for char in reversed_cleaned if char in 'aeiou')
            consonants = sum(1 for char in reversed_cleaned if char.isalpha() and char not in 'aeiou')
            return f"{reversed_cleaned}, vowel count: {vowels}, consonant count: {consonants}"