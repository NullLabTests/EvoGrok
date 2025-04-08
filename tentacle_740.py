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
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned and sorted values
            result = ','.join(cleaned_values)
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                result = str(input_data).lower()
            except ValueError:
                # If not a number, return the input as a lowercase string
                result = str(input_data).lower()
        
        # Additional processing for non-HTML, non-mathematical inputs
        if ' ' in result:
            # Split the result into words and sort them alphabetically
            words = result.split()
            sorted_words = sorted(words)
            # Join the sorted words with spaces
            return ' '.join(sorted_words)
        else:
            return result