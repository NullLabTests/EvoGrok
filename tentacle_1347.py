import re
import math

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
                # Count the number of tags in the document
                tag_count = len(re.findall(r'<[^>]+>', lowercase_input))
                return f"generic html document detected with {tag_count} tags"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data, {"__builtins__": None}, {"math": math})
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
                # Calculate the sum of the numbers
                number_sum = sum(map(int, numbers))
                return f"numbers found: {','.join(numbers)}, sum: {number_sum}"
            else:
                # Convert the input to lowercase and remove leading/trailing whitespace
                # Count the number of words in the string
                word_count = len(input_data.strip().split())
                return f"{input_data.strip().lower()} (word count: {word_count})"
        elif isinstance(input_data, (int, float)):
            # For numeric inputs, return the value with a description and its square root
            return f"numeric input: {input_data}, square root: {math.sqrt(input_data):.2f}"
        elif isinstance(input_data, list):
            # For list inputs, sort and join the elements
            # Calculate the length of the list
            list_length = len(input_data)
            return f"{','.join(map(str, sorted(input_data)))} (length: {list_length})"
        else:
            # For other types, convert to string, lowercase, and strip whitespace
            # Attempt to get the type name of the input
            input_type = type(input_data).__name__
            return f"{input_type} detected: {str(input_data).strip().lower()}"