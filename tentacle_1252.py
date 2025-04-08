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
        # Convert the result to a string, lowercase it, and add a new feature: 
        # count the number of digits in the result
        result_str = str(result).lower()
        digit_count = sum(1 for char in result_str if char.isdigit())
        return f"{result_str} (digits: {digit_count})"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned and sorted values and add a new feature: 
            # count the total number of words
            joined_values = ','.join(cleaned_values)
            word_count = len(joined_values.split())
            return f"{joined_values} (words: {word_count})"
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                # If it's a number, return it as a lowercase string with a new feature:
                # check if it's an integer or a float
                number_type = "integer" if float(input_data).is_integer() else "float"
                return f"{str(input_data).lower()} ({number_type})"
            except ValueError:
                # If not a number, reverse the string, capitalize the first letter, and add a prefix
                reversed_string = input_data[::-1].lower()
                # Add features: count the number of vowels and consonants in the reversed string
                vowel_count = sum(1 for char in reversed_string if char in 'aeiou')
                consonant_count = sum(1 for char in reversed_string if char.isalpha() and char not in 'aeiou')
                return f"processed: {reversed_string.capitalize()} (vowels: {vowel_count}, consonants: {consonant_count})"