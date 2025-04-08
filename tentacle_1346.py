import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # Attempt to extract the page title from the HTML
            title_match = re.search(r'<title>(.*?)</title>', lowercase_input)
            if title_match:
                title = title_match.group(1).strip()
                return f"html document detected: {title}"
            
            # Check for specific HTML classes or features
            if 'class="mw-parser-output"' in lowercase_input:
                return "wikipedia article html document detected"
            elif 'class="toc"' in lowercase_input:
                return "html document with table of contents detected"
            else:
                # Check for common HTML5 semantic elements
                semantic_elements = ['<header>', '<nav>', '<main>', '<footer>', '<article>', '<section>', '<aside>']
                detected_elements = [elem for elem in semantic_elements if elem in lowercase_input]
                if detected_elements:
                    return f"html5 document with elements: {', '.join(detected_elements)}"
                else:
                    return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string or other type
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any empty strings and strip whitespace
                cleaned_values = [value.strip() for value in sorted_values if value.strip()]
                return ','.join(cleaned_values)
            elif re.search(r'\d+', input_data):
                # If the string contains numbers, attempt to extract them
                numbers = re.findall(r'\d+', input_data)
                # Check if the string contains mathematical operators
                if re.search(r'[+\-*/]', input_data):
                    return f"potential math expression with numbers: {', '.join(numbers)}"
                else:
                    return f"numbers found: {', '.join(numbers)}"
            else:
                # Convert the input to lowercase and remove leading/trailing whitespace
                return input_data.strip().lower()
        elif isinstance(input_data, (int, float)):
            # For numeric inputs, return the value with a description
            return f"numeric input: {input_data}"
        elif isinstance(input_data, list):
            # For list inputs, sort and join the elements
            return ','.join(map(str, sorted(input_data)))
        elif isinstance(input_data, dict):
            # For dictionary inputs, sort and format key-value pairs
            sorted_items = sorted(input_data.items())
            return '; '.join(f"{k}: {v}" for k, v in sorted_items)
        else:
            # For other types, convert to string, lowercase, and strip whitespace
            return f"other type detected: {str(input_data).strip().lower()}"