import re

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
            # Attempt to extract the title from the HTML
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                return f"html document detected: {title_match.group(1).lower()}"
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
                return ','.join(cleaned_items)
            elif input_data.isdigit():
                # If it's a single number, return its square and cube
                number = int(input_data)
                return f"square: {number ** 2}, cube: {number ** 3}"
            else:
                # For other string inputs, perform multiple transformations
                lowercase = input_data.lower()
                reversed_string = lowercase[::-1]
                words = lowercase.split()
                capitalized_words = [word.capitalize() for word in words]
                capitalized_string = ' '.join(capitalized_words)
                return f"original: {lowercase}, reversed: {reversed_string}, capitalized: {capitalized_string}"
        else:
            # For non-string inputs, return a string representation
            return f"unknown type: {str(input_data)}"