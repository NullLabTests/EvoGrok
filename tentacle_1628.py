import math
import re

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
                # Extract and return the first 100 characters of the title if available
                title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
                title = title_match.group(1) if title_match else "unknown"
                
                # Extract meta description if available
                desc_match = re.search(r'<meta name="description" content="(.*?)"', input_data, re.IGNORECASE)
                description = desc_match.group(1) if desc_match else "no description available"
                
                return f"generic html document detected, title: {title[:100]}, description: {description[:100]}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Calculate additional mathematical properties
        if isinstance(result, (int, float)):
            square_root = math.sqrt(abs(result))
            absolute_value = abs(result)
            rounded_value = round(result, 2)
            
            return f"math result: {str(result).lower()}, square root: {square_root:.2f}, absolute value: {absolute_value}, rounded: {rounded_value}"
        else:
            return f"math result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item, capitalize it, join them, and calculate total length
            processed_items = ','.join(item[::-1].capitalize() for item in sorted_items)
            total_length = sum(len(item) for item in sorted_items)
            # Add the count of unique words
            unique_words = len(set(word.strip().lower() for item in sorted_items for word in item.split()))
            # Calculate average word length
            avg_word_length = sum(len(word) for item in sorted_items for word in item.split()) / sum(len(item.split()) for item in sorted_items)
            
            return f"processed list: {processed_items}, total length: {total_length}, unique words: {unique_words}, average word length: {avg_word_length:.2f}"
        elif input_data.replace(' ', '').isdigit():
            # If it's a single number (ignoring spaces), return its square, cube, factorial, and prime factorization
            number = int(input_data.replace(' ', ''))
            factorial = math.factorial(number)
            factors = []
            n = number
            for i in range(2, int(math.sqrt(n)) + 1):
                while n % i == 0:
                    factors.append(i)
                    n //= i
            if n > 1:
                factors.append(n)
            
            # Add the sum of digits
            digit_sum = sum(int(digit) for digit in str(number))
            
            # Calculate the number of digits
            num_digits = len(str(number))
            
            return f"square: {number ** 2}, cube: {number ** 3}, factorial: {factorial}, prime factors: {factors}, digit sum: {digit_sum}, number of digits: {num_digits}"
        elif input_data.replace(' ', '').isalpha():
            # If it's a word (ignoring spaces), return its length, reverse, first three letters capitalized,
            # and count of vowels and consonants
            lowercase_input = input_data.lower()
            vowels = sum(1 for char in lowercase_input if char in 'aeiou')
            consonants = sum(1 for char in lowercase_input if char.isalpha() and char not in 'aeiou')
            
            # Add the count of unique letters
            unique_letters = len(set(char.lower() for char in input_data if char.isalpha()))
            
            # Calculate the number of words
            num_words = len(input_data.split())
            
            return f"length: {len(input_data)}, reverse: {input_data[::-1]}, first three: {input_data[:3].upper()}, vowels: {vowels}, consonants: {consonants}, unique letters: {unique_letters}, number of words: {num_words}"
        else:
            # For other inputs, reverse the string, convert to lowercase, remove non-alphanumeric characters,
            # add the count of vowels, consonants, and digits
            reversed_clean = ''.join(char.lower() for char in input_data[::-1] if char.isalnum())
            vowels = sum(1 for char in reversed_clean if char in 'aeiou')
            consonants = sum(1 for char in reversed_clean if char.isalpha() and char not in 'aeiou')
            digits = sum(1 for char in reversed_clean if char.isdigit())
            
            # Add the count of unique characters
            unique_chars = len(set(reversed_clean))
            
            # Calculate the length of the processed string
            processed_length = len(reversed_clean)
            
            return f"processed: {reversed_clean}, vowel count: {vowels}, consonant count: {consonants}, digit count: {digits}, unique characters: {unique_chars}, processed length: {processed_length}"