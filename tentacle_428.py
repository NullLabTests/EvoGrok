def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on its content
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as text
        if ',' in input_data:
            # Sort and join comma-separated values (from Parent2)
            sorted_values = sorted(input_data.split(','))
            # Remove any empty strings that might result from leading/trailing commas
            cleaned_values = [v.strip() for v in sorted_values if v.strip()]
            # Join the cleaned and sorted values
            return ','.join(cleaned_values)
        else:
            # Check if the input is a string of digits
            if input_data.isdigit():
                # If it's a number, return it as a string (from Parent1)
                return input_data.lower()
            else:
                # Return the input as a lowercase string (from Parent1)
                return str(input_data).lower()