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
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add features
        result_str = str(result).lower()
        digit_count = sum(1 for char in result_str if char.isdigit())
        # Check if the result is an integer or a float
        number_type = "integer" if isinstance(result, int) else "float"
        return f"{result_str} (digits: {digit_count}, type: {number_type})"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned and sorted values and add features
            joined_values = ','.join(cleaned_values)
            word_count = len(joined_values.split())
            # Count the total number of characters
            char_count = len(joined_values)
            return f"{joined_values} (words: {word_count}, characters: {char_count})"
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                # If it's a number, return it as a lowercase string with features
                number_type = "integer" if float(input_data).is_integer() else "float"
                # Count the number of digits in the number
                digit_count = sum(1 for char in input_data if char.isdigit())
                return f"{str(input_data).lower()} (type: {number_type}, digits: {digit_count})"
            except ValueError:
                # If not a number, process the string
                processed_string = input_data.lower()
                # Reverse the string and capitalize the first letter
                reversed_string = processed_string[::-1].capitalize()
                # Add features: count the number of vowels and consonants in the processed string
                vowel_count = sum(1 for char in processed_string if char in 'aeiou')
                consonant_count = sum(1 for char in processed_string if char.isalpha() and char not in 'aeiou')
                # Count the number of unique characters
                unique_chars = len(set(processed_string))
                return f"processed: {reversed_string} (vowels: {vowel_count}, consonants: {consonant_count}, unique chars: {unique_chars})"