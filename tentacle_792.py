import re

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
                elif 'text' in title or 'processing' in title:
                    return f"text processing-related html document detected: {title}"
                else:
                    return f"html document detected: {title}"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add a prefix
        return f"math result: {str(result).lower()}"
    except Exception as e:
        # If evaluation fails, process the input based on its content
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join the items if it's a comma-separated list
                sorted_items = sorted(input_data.split(','))
                # Remove any empty items and strip whitespace
                cleaned_items = [item.strip() for item in sorted_items if item.strip()]
                return ','.join(cleaned_items)
            elif input_data.isdigit():
                # If it's a single number, return its square, cube, and factorial
                number = int(input_data)
                factorial = 1
                for i in range(1, number + 1):
                    factorial *= i
                return f"square: {number ** 2}, cube: {number ** 3}, factorial: {factorial}"
            else:
                # For other string inputs, perform multiple transformations
                lowercase = input_data.lower()
                reversed_string = lowercase[::-1]
                words = lowercase.split()
                capitalized_words = [word.capitalize() for word in words]
                capitalized_string = ' '.join(capitalized_words)
                # Add a new transformation: remove vowels
                vowels = 'aeiou'
                no_vowels = ''.join(char for char in lowercase if char not in vowels)
                return f"original: {lowercase}, reversed: {reversed_string}, capitalized: {capitalized_string}, no vowels: {no_vowels}"
        elif isinstance(input_data, (int, float)):
            # For numeric inputs, return basic statistics
            return f"value: {input_data}, square: {input_data ** 2}, cube: {input_data ** 3}, absolute: {abs(input_data)}"
        else:
            # For other types of input, return a string representation with type information
            return f"unknown type ({type(input_data).__name__}): {str(input_data)}"