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
        # Convert the result to a string, lowercase it, and return its length
        result_str = str(result).lower()
        return f"evaluated result: {result_str}, length: {len(result_str)}"
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
            vowels = 'aeiouAEIOU'
            vowel_count = sum(1 for char in input_data if char in vowels)
            return f"length: {len(input_data)}, reverse: {input_data[::-1]}, vowels: {vowel_count}"
        else:
            # For other inputs, reverse the string, convert to lowercase, 
            # remove non-alphanumeric characters, and count unique characters
            processed = ''.join(char.lower() for char in input_data[::-1] if char.isalnum())
            unique_chars = len(set(processed))
            return f"processed: {processed}, unique characters: {unique_chars}"