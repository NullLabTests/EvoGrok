def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "wikipedia data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "wikipedia mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "wikipedia text processing html document detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and reverse it
        reversed_result = str(result).lower()[::-1]
        # Calculate the sum of digits in the result (if any)
        digit_sum = sum(int(digit) for digit in str(result) if digit.isdigit())
        return f"{reversed_result} (digit sum: {digit_sum})"
    except:
        # If evaluation fails, process the input as a string or other type
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Reverse each value, capitalize it, and join with commas
                return ','.join([value[::-1].capitalize() for value in sorted_values])
            else:
                # Process the string further
                words = input_data.split()
                if len(words) > 1:
                    # If multiple words, reverse them, join with underscores, and capitalize
                    reversed_words = [word[::-1] for word in words]
                    joined_words = '_'.join(reversed_words).capitalize()
                    # Count vowels in the result
                    vowel_count = sum(1 for char in joined_words if char.lower() in 'aeiou')
                    return f"{joined_words} (vowel count: {vowel_count})"
                else:
                    # If single word, return it in uppercase, reversed, and with its length
                    return f"{input_data.upper()[::-1]} (length: {len(input_data)})"
        else:
            # For non-string inputs, convert to string, lowercase, reverse, and add type information
            reversed_str = str(input_data).lower()[::-1]
            return f"{reversed_str} (type: {type(input_data).__name__})"