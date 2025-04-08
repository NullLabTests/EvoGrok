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
                return f"numbers found: {','.join(numbers)}"
            else:
                # Convert the input to lowercase and remove leading/trailing whitespace
                return input_data.strip().lower()
        elif isinstance(input_data, (int, float)):
            # For numeric inputs, return the value with a description
            return f"numeric input: {input_data}"
        elif isinstance(input_data, list):
            # For list inputs, sort and join the elements
            return ','.join(map(str, sorted(input_data)))
        else:
            # For other types, convert to string, lowercase, and strip whitespace
            return f"other type detected: {str(input_data).strip().lower()}"

    # New feature: Check for specific keywords related to the knowledge
    keywords = ['data analysis', 'mathematics', 'text processing']
    lowercase_input = str(input_data).lower()
    for keyword in keywords:
        if keyword in lowercase_input:
            return f"{keyword} related content detected"

    # New feature: Check for Wikipedia-specific patterns
    if isinstance(input_data, str):
        if re.search(r'wikipedia\.org', input_data, re.IGNORECASE):
            return "wikipedia content detected"

    # If no other conditions are met, return the input as a lowercase string
    return str(input_data).lower()