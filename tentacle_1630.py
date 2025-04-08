import re
import math

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on the title or content
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # Attempt to extract the title from the HTML
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).lower()
                # Check for specific keywords in the title
                if 'data' in title:
                    return f"data-related html document detected: {title}"
                elif 'math' in title or 'equation' in title:
                    return f"math-related html document detected: {title}"
                elif 'text' in title or 'language' in title:
                    return f"text-related html document detected: {title}"
                else:
                    return f"html document detected: {title}"
            else:
                # If no title is found, check for keywords in the document
                if 'data' in lowercase_input:
                    return "data-related html document detected"
                elif 'math' in lowercase_input or 'equation' in lowercase_input:
                    return "math-related html document detected"
                elif 'text' in lowercase_input or 'language' in lowercase_input:
                    return "text-related html document detected"
                else:
                    return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add a prefix
        return f"math result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input based on its content
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join the items if it's a comma-separated list
                sorted_items = sorted(input_data.split(','))
                # Remove any empty items and strip whitespace
                cleaned_items = [item.strip() for item in sorted_items if item.strip()]
                # Capitalize the first letter of each item
                capitalized_items = [item.capitalize() for item in cleaned_items]
                return ','.join(capitalized_items)
            elif input_data.replace('.', '').replace('-', '').isdigit():
                # If it's a single number (including decimals and negatives), return its square, cube, square root, and logarithm
                number = float(input_data)
                return f"square: {number ** 2:.2f}, cube: {number ** 3:.2f}, square root: {number ** 0.5:.2f}, logarithm: {math.log(abs(number)):.2f}"
            else:
                # For other string inputs, perform multiple transformations
                lowercase = input_data.lower()
                reversed_string = lowercase[::-1]
                words = lowercase.split()
                capitalized_words = [word.capitalize() for word in words]
                capitalized_string = ' '.join(capitalized_words)
                # Count the number of vowels in the original string
                vowels = sum(1 for char in lowercase if char in 'aeiou')
                # Check if the input contains any numbers
                numbers = [float(part) for part in re.findall(r'-?\d+\.?\d*', input_data)]
                if numbers:
                    avg = sum(numbers) / len(numbers)
                    return f"original: {lowercase}, reversed: {reversed_string}, capitalized: {capitalized_string}, vowel count: {vowels}, average of numbers: {avg:.2f}"
                else:
                    return f"original: {lowercase}, reversed: {reversed_string}, capitalized: {capitalized_string}, vowel count: {vowels}"
        else:
            # For non-string inputs, return a string representation and its type
            return f"unknown type: {str(input_data)}, type: {type(input_data).__name__}"