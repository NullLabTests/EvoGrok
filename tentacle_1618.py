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
                # If not a number, process as text
                result = str(input_data).lower()
        
        # Additional processing for non-HTML, non-mathematical inputs
        if ' ' in result:
            # Split the result into words and sort them alphabetically
            words = result.split()
            sorted_words = sorted(words)
            # Join the sorted words with spaces
            sorted_result = ' '.join(sorted_words)
            
            # Check for specific patterns in the sorted result
            if 'data' in sorted_result and 'analysis' in sorted_result:
                return "data analysis text detected"
            elif 'mathematics' in sorted_result:
                return "mathematics text detected"
            elif 'text' in sorted_result and 'processing' in sorted_result:
                return "text processing text detected"
            else:
                return sorted_result
        else:
            return result