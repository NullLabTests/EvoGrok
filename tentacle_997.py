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
        # Convert the result to a string, reverse it, and lowercase it
        reversed_result = str(result)[::-1].lower()
        # If the result is a number, return it as is; otherwise, capitalize the first letter
        return reversed_result if reversed_result.replace('.', '').isdigit() else reversed_result.capitalize()
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Reverse the order of the cleaned values
            reversed_values = cleaned_values[::-1]
            # Capitalize the first letter of each value
            capitalized_values = [value.capitalize() for value in reversed_values]
            return ','.join(capitalized_values)
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                # If it's a number, return it as a string with reversed digits
                return str(input_data)[::-1].lower()
            except ValueError:
                # If not a number, reverse the string, capitalize the first letter, and lowercase the rest
                reversed_input = input_data[::-1]
                capitalized_input = reversed_input.capitalize()
                return capitalized_input[0] + capitalized_input[1:].lower()