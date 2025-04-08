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
            # If no specific type is detected, return the lowercase input
            return lowercase_input
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_items = sorted(input_data.split(','))
            # Remove any empty strings from the sorted list and strip whitespace
            cleaned_items = [item.strip() for item in sorted_items if item.strip()]
            # If there are any items left, join them
            if cleaned_items:
                return f"sorted and cleaned list: {','.join(cleaned_items)}"
            else:
                # If all items were empty, return an empty list
                return "empty list"
        else:
            # Return the input as a lowercase string
            return f"processed string: {str(input_data).lower()}"