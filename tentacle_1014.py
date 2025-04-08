import math

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "wikipedia text processing html document detected"
        else:
            # If it's an HTML document but doesn't match specific types, check for other keywords
            if 'wikipedia' in lowercase_input:
                return "wikipedia html document detected"
            elif 'tutorial' in lowercase_input:
                return "tutorial html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add a prefix
        return f"math result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item, capitalize it, join them, and calculate total length
            processed_items = ','.join(item[::-1].capitalize() for item in sorted_items)
            total_length = sum(len(item) for item in sorted_items)
            return f"processed list: {processed_items}, total length: {total_length}"
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
            
            return f"square: {number ** 2}, cube: {number ** 3}, factorial: {factorial}, prime factors: {factors}"
        elif input_data.replace(' ', '').isalpha():
            # If it's a word (ignoring spaces), return its length, reverse, first three letters capitalized,
            # and count of vowels and consonants
            lowercase_input = input_data.lower()
            vowels = sum(1 for char in lowercase_input if char in 'aeiou')
            consonants = sum(1 for char in lowercase_input if char.isalpha() and char not in 'aeiou')
            
            return f"length: {len(input_data)}, reverse: {input_data[::-1]}, first three: {input_data[:3].upper()}, vowels: {vowels}, consonants: {consonants}"
        else:
            # For other inputs, reverse the string, convert to lowercase, remove non-alphanumeric characters,
            # add the count of vowels, consonants, and digits
            reversed_clean = ''.join(char.lower() for char in input_data[::-1] if char.isalnum())
            vowels = sum(1 for char in reversed_clean if char in 'aeiou')
            consonants = sum(1 for char in reversed_clean if char.isalpha() and char not in 'aeiou')
            digits = sum(1 for char in reversed_clean if char.isdigit())
            
            return f"processed: {reversed_clean}, vowel count: {vowels}, consonant count: {consonants}, digit count: {digits}"