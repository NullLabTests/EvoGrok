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
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values (from Parent2)
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned values with commas and lowercase the result
            return ','.join(cleaned_values).lower()
        else:
            # Check if the input is a string
            if isinstance(input_data, str):
                # Split the string into words
                words = input_data.split()
                # Sort the words alphabetically
                sorted_words = sorted(words)
                # Join the sorted words with spaces and lowercase the result
                return ' '.join(sorted_words).lower()
            else:
                # For non-string inputs, convert to string and lowercase
                return str(input_data).lower()