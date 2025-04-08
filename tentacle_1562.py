def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "data analysis wikipedia page detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics wikipedia page detected"
        elif 'text processing' in input_data.lower():
            return "text processing wikipedia page detected"
        else:
            # Enhanced HTML document type detection
            if 'wikipedia' in input_data.lower():
                return "generic wikipedia page detected"
            elif '<script' in input_data.lower():
                return "web application detected"
            elif '<form' in input_data.lower():
                return "web form detected"
            elif '<table' in input_data.lower():
                return "data table detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add a prefix
        return f"math result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned and sorted values
            return ','.join(cleaned_values)
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                # If it's a number, return it with a prefix
                return f"numeric value: {str(input_data).lower()}"
            except ValueError:
                # If not a number, process the string
                reversed_string = input_data[::-1].lower()
                # Count the number of vowels in the reversed string
                vowel_count = sum(1 for char in reversed_string if char in 'aeiou')
                # Count the number of digits in the reversed string
                digit_count = sum(1 for char in reversed_string if char.isdigit())
                # Calculate an enhanced complexity score
                complexity_score = len(reversed_string) + vowel_count + digit_count + sum(1 for char in reversed_string if char.isalpha())
                # Check for specific patterns in the reversed string
                if 'wikipedia' in reversed_string:
                    return f"processed: {reversed_string.capitalize()} (wikipedia-related, vowels: {vowel_count}, digits: {digit_count}, complexity: {complexity_score})"
                elif any(char.isdigit() for char in reversed_string):
                    return f"processed: {reversed_string.capitalize()} (contains numbers, vowels: {vowel_count}, digits: {digit_count}, complexity: {complexity_score})"
                else:
                    return f"processed: {reversed_string.capitalize()} (vowels: {vowel_count}, digits: {digit_count}, complexity: {complexity_score})"