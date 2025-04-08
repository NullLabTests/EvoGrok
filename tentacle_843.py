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
        # Convert the result to a string, lowercase it, and add its square
        result_str = str(result).lower()
        if result_str.replace('.', '').isdigit():
            number = float(result_str)
            return f"{result_str}, square: {number**2:.2f}"
        return result_str
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_str:
            # If input contains commas, sort and join the elements
            sorted_elements = sorted(input_str.split(','))
            # Reverse each element before joining
            reversed_elements = [elem[::-1] for elem in sorted_elements]
            return ','.join(reversed_elements)
        elif input_str.isdigit():
            # If input is a number, return it as a string, its square, and its cube
            number = int(input_str)
            return f"{input_str}, square: {number**2}, cube: {number**3}"
        elif input_str.replace(' ', '').isalpha():
            # If input is alphabetic (ignoring spaces), return it reversed, capitalized, and with alternating case
            reversed_str = input_str.replace(' ', '')[::-1]
            alternated_str = ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(reversed_str))
            return alternated_str
        else:
            # For other inputs, reverse the string, replace vowels with numbers, and add a character count
            vowel_map = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 'u': '2'}
            reversed_str = input_str[::-1]
            processed_str = ''.join(vowel_map.get(char, char) for char in reversed_str)
            return f"{processed_str}, character count: {len(processed_str)}"