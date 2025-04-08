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
                title = title_match.group(1)
                # Analyze the title for specific keywords
                if 'statistics' in title.lower():
                    return f"html document detected: {title} (related to statistics)"
                elif 'algorithm' in title.lower():
                    return f"html document detected: {title} (related to algorithms)"
                else:
                    return f"html document detected: {title}"
            else:
                # If no title is found, check for specific content
                if 'wikipedia' in lowercase_input:
                    return "generic wikipedia html document detected"
                else:
                    return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # If the result is a number, return various mathematical operations
        if isinstance(result, (int, float)):
            return (f"result: {result}, "
                    f"square: {result ** 2}, "
                    f"cube: {result ** 3}, "
                    f"sqrt: {math.sqrt(abs(result))}, "
                    f"sin: {math.sin(result)}, "
                    f"cos: {math.cos(result)}, "
                    f"log: {math.log(abs(result)) if result != 0 else 'undefined'}")
        else:
            # For other types of results, convert to string and lowercase
            return str(result).lower()
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item, capitalize it, and join them
            reversed_items = [item[::-1].capitalize() for item in sorted_items]
            # Add a new operation: count unique characters in each item
            unique_chars = [len(set(item.lower())) for item in sorted_items]
            return (f"processed list: {','.join(reversed_items)}, "
                    f"unique chars per item: {','.join(map(str, unique_chars))}")
        elif input_data.replace('.', '', 1).isdigit():
            # If it's a number (including decimals), return various mathematical operations
            number = float(input_data)
            return (f"number: {number}, "
                    f"square: {number ** 2}, "
                    f"cube: {number ** 3}, "
                    f"sqrt: {math.sqrt(abs(number))}, "
                    f"sin: {math.sin(number)}, "
                    f"cos: {math.cos(number)}, "
                    f"log: {math.log(abs(number)) if number != 0 else 'undefined'}")
        elif input_data.replace(' ', '').isalnum():
            # If it's a string of alphanumeric characters (with or without spaces)
            alphanumeric_chars = ''.join(char for char in input_data if char.isalnum())
            return (f"length: {len(alphanumeric_chars)}, "
                    f"reverse: {alphanumeric_chars[::-1].lower()}, "
                    f"unique chars: {len(set(alphanumeric_chars.lower()))}, "
                    f"is palindrome: {alphanumeric_chars.lower() == alphanumeric_chars.lower()[::-1]}")
        else:
            # For other inputs, reverse the string, convert to lowercase, 
            # remove non-alphanumeric characters, and count unique characters
            cleaned_input = ''.join(char.lower() for char in input_data if char.isalnum())
            return (f"cleaned and reversed: {cleaned_input[::-1]}, "
                    f"unique chars: {len(set(cleaned_input))}, "
                    f"vowel count: {sum(1 for char in cleaned_input if char in 'aeiou')}")