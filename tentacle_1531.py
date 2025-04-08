def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in lowercase_input:
            return "data analysis wikipedia page detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics wikipedia page detected"
        elif 'text processing' in lowercase_input:
            return "text processing wikipedia page detected"
        else:
            # Check for specific class attributes
            if 'class="client-nojs"' in lowercase_input:
                return "wikipedia page detected"
            elif 'class="mw-mobile"' in lowercase_input:
                return "mobile wikipedia page detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        input_str = str(input_data)
        
        # Check if the input contains comma-separated values
        if ',' in input_str:
            # Sort and join comma-separated values
            sorted_values = sorted(input_str.split(','))
            # Remove any empty strings and strip whitespace
            cleaned_values = [value.strip() for value in sorted_values if value.strip()]
            # Join the cleaned values
            result = ','.join(cleaned_values)
        else:
            # Convert the input to lowercase and remove leading/trailing whitespace
            result = input_str.strip().lower()
        
        # Check for specific keywords in the processed input
        if 'data analysis' in result:
            return f"data analysis related: {result}"
        elif 'mathematics' in result:
            return f"mathematics related: {result}"
        elif 'text processing' in result:
            return f"text processing related: {result}"
        
        # Additional processing for numeric inputs
        try:
            # Attempt to convert the result to a float
            numeric_value = float(result)
            return f"numeric input: {numeric_value}"
        except ValueError:
            # If conversion to float fails, perform additional text processing
            words = result.split()
            if len(words) > 1:
                # Return the first and last word if there are multiple words
                return f"processed text: {words[0]} ... {words[-1]}"
            else:
                # Return the entire string if it's a single word
                return result