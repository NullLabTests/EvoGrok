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
        # Convert the result to a string, lowercase it, and return with its square
        result_str = str(result).lower()
        return f"{result_str}, square: {result**2}"
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
        elif input_str.startswith('wiki='):
            # If input starts with 'wiki=', process it as a Wikipedia topic
            wiki_topic = input_str.split('=')[1]
            if wiki_topic in ['data analysis', 'mathematics', 'text processing']:
                return f"wikipedia page on {wiki_topic} detected"
            else:
                return f"wikipedia page on {wiki_topic} not recognized"
        else:
            # For other inputs, reverse the string, capitalize the first letter, and add its length
            reversed_str = input_str[::-1]
            return f"{reversed_str.capitalize()}, length: {len(input_str)}"