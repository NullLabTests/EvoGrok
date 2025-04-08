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
            # If it's an HTML document but doesn't match specific patterns, check for other keywords
            if 'science' in lowercase_input:
                return "wikipedia science html document detected"
            elif 'history' in lowercase_input:
                return "wikipedia history html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # If the result is a number, return it with additional information
        if isinstance(result, (int, float)):
            return f"mathematical result: {result:.2f}"
        else:
            # For non-numeric results, convert to string, lowercase, and remove whitespace
            return str(result).strip().lower()
    except:
        # If evaluation fails, process the input as a string
        if isinstance(input_data, str):
            # Check for comma-separated values
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Remove any empty strings and strip whitespace from each value
                cleaned_values = [value.strip() for value in sorted_values if value.strip()]
                # Join the cleaned values with commas and convert to lowercase
                result = ','.join(cleaned_values).lower()
                
                # Check if the result looks like a list of numbers
                if all(val.replace('.', '').replace('-', '').isdigit() for val in result.split(',')):
                    # If it's a list of numbers, calculate and return their average
                    numbers = [float(val) for val in result.split(',')]
                    average = sum(numbers) / len(numbers)
                    return f"average of {result}: {average:.2f}"
                else:
                    return result
            else:
                # Convert the input to lowercase and remove any leading/trailing whitespace
                return input_data.strip().lower()
        else:
            # For non-string inputs, convert to string and lowercase
            return str(input_data).lower()