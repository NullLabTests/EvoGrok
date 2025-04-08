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
            return f"{input_str}, square: {number**2}"
        elif input_str.startswith('lang='):
            # If input starts with 'lang=', process it as a language code
            lang_code = input_str.split('=')[1]
            if lang_code == 'en':
                return "english language detected"
            else:
                return f"language code detected: {lang_code}"
        elif ' ' in input_str:
            # If input contains spaces, reverse the order of words
            words = input_str.split()
            reversed_words = words[::-1]
            return ' '.join(reversed_words)
        elif input_str.startswith('http'):
            # If input looks like a URL, extract the domain
            domain = input_str.split('/')[2]
            return f"url detected, domain: {domain}"
        else:
            # For other inputs, reverse the string and capitalize the first letter
            reversed_str = input_str[::-1]
            return reversed_str.capitalize()