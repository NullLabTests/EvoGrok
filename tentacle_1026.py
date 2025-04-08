import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on the title or content
        if 'data analysis' in lowercase_input:
            return "specialized html document detected: data analysis"
        elif 'mathematics' in lowercase_input:
            return "specialized html document detected: mathematics"
        elif 'text processing' in lowercase_input:
            return "specialized html document detected: text processing"
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
                elif 'text' in title or 'string' in title:
                    return f"text processing html document detected: {title}"
                else:
                    return f"generic html document detected: {title}"
            else:
                # If no title is found, check for keywords in the content
                content_keywords = ['data', 'math', 'equation', 'text', 'string']
                for keyword in content_keywords:
                    if keyword in lowercase_input:
                        return f"{keyword}-related html document detected"
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
            elif input_data.replace('.', '').isdigit():
                # If it's a number (including decimals), return its square, cube, and square root
                number = float(input_data)
                return f"square: {number ** 2:.2f}, cube: {number ** 3:.2f}, square root: {number ** 0.5:.2f}"
            else:
                # For other string inputs, perform multiple transformations
                lowercase = input_data.lower()
                reversed_string = lowercase[::-1]
                words = lowercase.split()
                capitalized_words = [word.capitalize() for word in words]
                capitalized_string = ' '.join(capitalized_words)
                
                # Check for specific keywords and provide additional information
                if 'data' in lowercase:
                    return f"data-related string detected: original: {lowercase}, reversed: {reversed_string}, capitalized: {capitalized_string}"
                elif 'math' in lowercase or 'equation' in lowercase:
                    return f"math-related string detected: original: {lowercase}, reversed: {reversed_string}, capitalized: {capitalized_string}"
                elif 'text' in lowercase or 'string' in lowercase:
                    return f"text processing string detected: original: {lowercase}, reversed: {reversed_string}, capitalized: {capitalized_string}"
                else:
                    return f"original: {lowercase}, reversed: {reversed_string}, capitalized: {capitalized_string}"
        else:
            # For other types of input, return a string representation with type information
            return f"unknown type ({type(input_data).__name__}): {str(input_data)}"