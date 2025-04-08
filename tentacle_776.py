def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title
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
        # Convert the result to a string, lowercase it, and return its length and reverse
        result_str = str(result).lower()
        return f"length: {len(result_str)}, reverse: {result_str[::-1]}"
    except:
        # If evaluation fails, process the input based on its content
        if ',' in input_data:
            # Sort and join the items if it's a comma-separated list
            sorted_items = sorted(input_data.split(','))
            # Reverse each item, convert to lowercase, and join them
            return ','.join(item[::-1].lower() for item in sorted_items)
        elif input_data.isdigit():
            # If it's a single number, return its square, cube, and factorial
            number = int(input_data)
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            return f"square: {number ** 2}, cube: {number ** 3}, factorial: {factorial}"
        elif input_data.replace(' ', '').isalpha():
            # If it's a word (ignoring spaces), return its length, reverse, and vowel count
            vowels = sum(1 for char in input_data.lower() if char in 'aeiou')
            return f"length: {len(input_data)}, reverse: {input_data[::-1]}, vowels: {vowels}"
        else:
            # For other inputs, reverse the string, convert to lowercase, 
            # remove non-alphanumeric characters, and return its length
            processed_input = ''.join(char.lower() for char in input_data[::-1] if char.isalnum())
            return f"length: {len(processed_input)}, processed: {processed_input}"