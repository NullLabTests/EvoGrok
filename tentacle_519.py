def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "text processing html document detected"
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
            # Reverse the order of the cleaned values (new functionality)
            reversed_values = cleaned_values[::-1]
            return ','.join(reversed_values)
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                # If it's a number, return it as a string with reversed digits (new functionality)
                return str(input_data)[::-1].lower()
            except ValueError:
                # If not a number, reverse the string and capitalize the first letter (new functionality)
                reversed_input = input_data[::-1]
                return reversed_input.capitalize()