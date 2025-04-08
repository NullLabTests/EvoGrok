import re
from math import factorial, sqrt

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on the title
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # Extract the title if possible
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                return f"html document detected: {title_match.group(1).strip()}"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # If the result is a number, perform additional calculations
        if isinstance(result, (int, float)):
            return f"result: {result}, square root: {sqrt(abs(result)):.2f}, factorial: {factorial(int(result)) if result >= 0 and result.is_integer() else 'N/A'}"
        else:
            # Convert the result to a string and lowercase it
            return str(result).lower()
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item, convert to lowercase, and join them
            return ','.join(item[::-1].lower() for item in sorted_items)
        elif input_data.replace(' ', '').isdigit():
            # If it's a single number, return its square, cube, factorial, and fibonacci number
            number = int(input_data)
            fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
            
            return f"square: {number ** 2}, cube: {number ** 3}, factorial: {factorial(number)}, fibonacci: {fibonacci(number)}"
        elif input_data.replace(' ', '').isalpha():
            # If it's a word (ignoring spaces), return its length, reverse, vowel count, consonant count, and palindrome check
            vowels = 'aeiouAEIOU'
            vowel_count = sum(1 for char in input_data if char.lower() in vowels)
            consonant_count = sum(1 for char in input_data if char.isalpha() and char.lower() not in vowels)
            is_palindrome = input_data.lower().replace(' ', '') == input_data.lower().replace(' ', '')[::-1]
            
            return f"length: {len(input_data)}, reverse: {input_data[::-1]}, vowels: {vowel_count}, consonants: {consonant_count}, palindrome: {is_palindrome}"
        else:
            # For other inputs, reverse the string, convert to lowercase, 
            # remove non-alphanumeric characters, count the unique characters,
            # calculate the sum of numeric characters, and check for common patterns
            processed = ''.join(char.lower() for char in input_data[::-1] if char.isalnum())
            unique_chars = len(set(processed))
            numeric_sum = sum(int(char) for char in processed if char.isdigit())
            
            # Check for common patterns
            is_email = bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', input_data))
            is_url = bool(re.match(r'^https?://[^\s/$.?#].[^\s]*$', input_data))
            
            return f"processed: {processed}, unique characters: {unique_chars}, numeric sum: {numeric_sum}, email: {is_email}, url: {is_url}"