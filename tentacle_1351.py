def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Check for specific HTML document types based on knowledge
        if 'data analysis' in lowercase_input and 'wikipedia' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input and 'wikipedia' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input and 'wikipedia' in lowercase_input:
            return "wikipedia text processing html document detected"
        
        # Check for other specific HTML document types
        elif 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        
        # If not a specific type, try to extract the title
        title_start = lowercase_input.find('<title>')
        title_end = lowercase_input.find('</title>')
        if title_start != -1 and title_end != -1:
            title = lowercase_input[title_start+7:title_end].strip()
            return f"html document detected: {title}"
        
        # If no title found, check for other content
        if 'wikipedia' in lowercase_input:
            return "wikipedia html document detected"
        
        # If no specific patterns match, return a generic message
        return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string or other type
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any empty strings and strip whitespace
                cleaned_values = [value.strip() for value in sorted_values if value.strip()]
                return ','.join(cleaned_values)
            else:
                # Convert the input to lowercase and remove leading/trailing whitespace
                return input_data.strip().lower()
        else:
            # For non-string inputs, convert to string, lowercase, and strip whitespace
            return str(input_data).strip().lower()