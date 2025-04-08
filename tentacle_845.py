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
            sorted_elements = sorted(input_str.split(','))
            # Reverse each element before joining
            reversed_elements = [elem[::-1] for elem in sorted_elements]
            return ','.join(reversed_elements)
        elif input_str.isdigit():
            # If input is a number, return it as a string and its square
            number = int(input_str)
            return f"{input_str}, {number**2}"
        elif input_str.isalpha():
            # If input is alphabetic, reverse the string and capitalize the first letter
            return input_str[::-1].capitalize()
        else:
            # For other inputs, return the first and last characters, and the length
            return f"{input_str[0]}{input_str[-1]} ({len(input_str)})" if len(input_str) > 1 else input_str