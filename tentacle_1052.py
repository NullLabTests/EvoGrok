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
        # If the reversed result contains digits, return the sum of those digits
        if any(char.isdigit() for char in reversed_result):
            return str(sum(int(char) for char in reversed_result if char.isdigit()))
        else:
            return reversed_result
    except:
        # If evaluation fails, process the input as a string or other type
        if isinstance(input_data, str):
            if ',' in input_data:
                # Sort and join comma-separated values
                sorted_values = sorted(input_data.split(','))
                # Reverse each value, capitalize it, and join with semicolons
                return ';'.join([value[::-1].capitalize() for value in sorted_values])
            else:
                # Process the string further
                words = input_data.split()
                if len(words) > 1:
                    # If multiple words, reverse them, join with hyphens, and convert to title case
                    reversed_words = [word[::-1] for word in words]
                    return '-'.join(reversed_words).title()
                else:
                    # If single word, return it in uppercase, reversed, and with alternating case
                    reversed_word = input_data.upper()[::-1]
                    return ''.join(c.lower() if i % 2 else c for i, c in enumerate(reversed_word))
        else:
            # For non-string inputs, convert to string, lowercase, reverse, and count unique characters
            reversed_str = str(input_data).lower()[::-1]
            return f"{reversed_str} (unique chars: {len(set(reversed_str))})"