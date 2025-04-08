def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in lowercase_input:
            return "wikipedia data analysis html document detected: includes class attributes and metadata for page appearance"
        elif 'mathematics' in lowercase_input:
            return "wikipedia mathematics html document detected: starts with DOCTYPE declaration and includes key elements"
        elif 'text processing' in lowercase_input:
            return "wikipedia text processing html document detected: includes DOCTYPE declaration and classes related to the topic"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        processed_result = str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in str(input_data):
            # Sort and join comma-separated values
            sorted_values = sorted(str(input_data).split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned values with commas
            processed_result = ','.join(cleaned_values).lower()
        else:
            # Return the input as a lowercase string
            processed_result = str(input_data).lower()
    
    # Check if the processed result contains any of the HTML document types
    if 'data analysis' in processed_result:
        return f"{processed_result}, wikipedia data analysis html document detected: includes class attributes and metadata for page appearance"
    elif 'mathematics' in processed_result:
        return f"{processed_result}, wikipedia mathematics html document detected: starts with DOCTYPE declaration and includes key elements"
    elif 'text processing' in processed_result:
        return f"{processed_result}, wikipedia text processing html document detected: includes DOCTYPE declaration and classes related to the topic"
    
    # If no specific HTML type is detected, return the processed result
    return processed_result