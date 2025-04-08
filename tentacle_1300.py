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
                return f"html document detected: {title_match.group(1).lower()}"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"evaluated result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item, convert to lowercase, and join them
            reversed_items = [item[::-1].lower() for item in sorted_items]
            return f"reversed and sorted: {', '.join(reversed_items)}"
        elif input_data.replace('.', '').isdigit():
            # If it's a number (including decimals), return various mathematical operations
            number = float(input_data)
            int_number = int(number)
            
            results = {
                "square": number ** 2,
                "cube": number ** 3,
                "factorial": factorial(int_number) if int_number == number else "N/A",
                "fibonacci": fibonacci(int_number) if int_number == number else "N/A",
                "square root": sqrt(number)
            }
            
            return ", ".join(f"{key}: {value}" for key, value in results.items())
        elif input_data.replace(' ', '').isalpha():
            # If it's a word (ignoring spaces), return various text analysis results
            vowels = 'aeiouAEIOU'
            vowel_count = sum(1 for char in input_data if char.lower() in vowels)
            consonant_count = sum(1 for char in input_data if char.isalpha() and char.lower() not in vowels)
            word_count = len(input_data.split())
            
            return f"length: {len(input_data)}, reverse: {input_data[::-1]}, words: {word_count}, vowels: {vowel_count}, consonants: {consonant_count}"
        else:
            # For other inputs, perform multiple operations
            processed = ''.join(char.lower() for char in input_data[::-1] if char.isalnum())
            unique_chars = len(set(processed))
            numeric_sum = sum(int(char) for char in processed if char.isdigit())
            palindrome = processed == processed[::-1]
            
            return f"processed: {processed}, unique characters: {unique_chars}, numeric sum: {numeric_sum}, palindrome: {palindrome}"

# Helper function to calculate Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b