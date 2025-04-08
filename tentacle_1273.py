def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "wikipedia mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "wikipedia text processing html document detected"
        else:
            # Check for other common HTML document types
            if 'html' in input_data.lower():
                return "generic html5 document detected"
            elif 'xhtml' in input_data.lower():
                return "xhtml document detected"
            else:
                return "unknown html document type detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned values with commas
            processed_input = ','.join(cleaned_values)
        else:
            processed_input = input_data
        
        # Check if the processed input contains any uppercase letters
        if any(char.isupper() for char in processed_input):
            # If it does, return the input as is (preserving case)
            return f"mixed case string: {processed_input}"
        else:
            # If it doesn't, return the input as a lowercase string
            return f"lowercase string: {processed_input.lower()}"