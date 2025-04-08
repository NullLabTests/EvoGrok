import re
import math

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Detect specific types of HTML documents based on title and content
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # Attempt to extract the title from the HTML
            title_match = re.search(r'<title>(.*?)</title>', lowercase_input, re.IGNORECASE)
            if title_match:
                return f"html document detected: {title_match.group(1)}"
            else:
                # If no title found, check for specific keywords
                keywords = ['science', 'technology', 'arts', 'history']
                for keyword in keywords:
                    if keyword in lowercase_input:
                        return f"{keyword} html document detected"
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # If the result is a number, return its square, cube, square root, and logarithm
        if isinstance(result, (int, float)):
            return f"result: {result}, square: {result ** 2}, cube: {result ** 3}, sqrt: {math.sqrt(result)}, log: {math.log(result) if result > 0 else 'undefined'}"
        else:
            # For other types of results, convert to string, lowercase, and reverse
            return str(result).lower()[::-1]
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item, capitalize it, and join them
            return ','.join(item[::-1].capitalize() for item in sorted_items)
        elif input_data.replace('.', '', 1).isdigit():
            # If it's a number (including decimals), return its square, cube, square root, and logarithm
            number = float(input_data)
            return f"square: {number ** 2}, cube: {number ** 3}, sqrt: {math.sqrt(number)}, log: {math.log(number) if number > 0 else 'undefined'}"
        elif input_data.replace(' ', '').isalnum():
            # If it's a string of alphanumeric characters (with or without spaces)
            alphanumeric_chars = ''.join(char for char in input_data if char.isalnum())
            return f"length: {len(alphanumeric_chars)}, reverse: {alphanumeric_chars[::-1].lower()}, unique chars: {len(set(alphanumeric_chars.lower()))}, is palindrome: {alphanumeric_chars.lower() == alphanumeric_chars.lower()[::-1]}"
        else:
            # For other inputs, reverse the string, convert to lowercase, 
            # remove non-alphanumeric characters, count unique characters, and check for palindrome
            cleaned_input = ''.join(char.lower() for char in input_data if char.isalnum())
            return f"cleaned and reversed: {cleaned_input[::-1]}, unique chars: {len(set(cleaned_input))}, is palindrome: {cleaned_input == cleaned_input[::-1]}"