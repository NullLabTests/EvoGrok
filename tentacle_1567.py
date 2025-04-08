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
            # Count the number of class and id attributes in the HTML
            class_count = input_data.lower().count('class=')
            id_count = input_data.lower().count('id=')
            # Calculate the total length of the HTML snippet
            html_length = len(input_data)
            return f"generic html document detected (class attributes: {class_count}, id attributes: {id_count}, length: {html_length})"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add new features
        result_str = str(result).lower()
        # Count the number of digits in the result
        digit_count = sum(1 for char in result_str if char.isdigit())
        # Count the number of vowels in the result
        vowel_count = sum(1 for char in result_str if char in 'aeiou')
        return f"{result_str} (digits: {digit_count}, vowels: {vowel_count})"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned and sorted values
            result = ','.join(cleaned_values)
            # Calculate the length of the processed string
            processed_length = len(result)
            return f"processed: {result} (length: {processed_length})"
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                return str(input_data).lower()
            except ValueError:
                # If not a number, reverse the string, capitalize the first letter, and add a prefix
                reversed_string = input_data[::-1].lower()
                # Count the number of vowels in the reversed string
                vowel_count = sum(1 for char in reversed_string if char in 'aeiou')
                # Calculate the length of the processed string
                processed_length = len(reversed_string)
                # Count the number of unique characters in the reversed string
                unique_chars = len(set(reversed_string))
                return f"processed: {reversed_string.capitalize()} (vowels: {vowel_count}, length: {processed_length}, unique characters: {unique_chars})"