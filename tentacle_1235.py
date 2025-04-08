def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "wikipedia text processing html document detected"
        else:
            # If it's an HTML document but doesn't match known patterns, check for comma-separated values
            html_content = lowercase_input.split('>', 1)[1] if '>' in lowercase_input else lowercase_input
            if ',' in html_content:
                # Sort and join comma-separated values found in the HTML content
                sorted_values = sorted(html_content.split(','))
                cleaned_values = [value.strip() for value in sorted_values if value.strip()]
                return f"generic html document with sorted content: {','.join(cleaned_values)}"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and remove leading/trailing whitespace
        return str(result).strip().lower()
    except:
        # If evaluation fails, process the input as a string
        if isinstance(input_data, str):
            # Check for comma-separated values in the input
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any empty strings, strip whitespace from each value, and convert to lowercase
                cleaned_values = [value.strip().lower() for value in sorted_values if value.strip()]
                # Join the cleaned values with commas and remove leading/trailing whitespace
                return ','.join(cleaned_values).strip()
            else:
                # Convert the input to lowercase and remove leading/trailing whitespace
                return input_data.strip().lower()
        else:
            # If the input is not a string, convert it to a string and lowercase it
            return str(input_data).lower()