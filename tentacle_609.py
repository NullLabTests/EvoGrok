def tentacle(input_data):
    # Convert input to string and strip whitespace
    input_str = str(input_data).strip().lower()
    
    # Check if the input looks like the start of an HTML document
    if input_str.startswith('<!doctype'):
        # Check for specific Wikipedia page titles
        if 'data analysis' in input_str:
            return "wikipedia page on data analysis detected"
        elif 'mathematics' in input_str:
            return "wikipedia page on mathematics detected"
        elif 'text processing' in input_str:
            return "wikipedia page on text processing detected"
        else:
            return "html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_str)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_str:
            # If input contains commas, sort and join the elements
            return ','.join(sorted(input_str.split(',')))
        elif input_str.isdigit():
            # If input is a number, return it as a string
            return input_str
        elif input_str.isalpha():
            # If input is alphabetic, reverse the string
            return input_str[::-1]
        else:
            # For other inputs, return the first and last characters
            return input_str[0] + input_str[-1] if len(input_str) > 1 else input_str