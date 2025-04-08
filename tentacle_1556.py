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
            # For generic HTML documents, extract the title if possible
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                return f"generic html document detected: {title_match.group(1)}"
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
            return f"sorted and cleaned: {','.join(cleaned_values)}"
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                return f"number detected: {str(input_data).lower()}"
            except ValueError:
                # If not a number, process the string in multiple ways
                reversed_string = input_data[::-1].lower()
                capitalized_reversed = reversed_string.capitalize()
                
                # Count characters
                vowel_count = sum(1 for char in reversed_string if char in 'aeiou')
                consonant_count = sum(1 for char in reversed_string if char.isalpha() and char not in 'aeiou')
                
                # Calculate the ratio of vowels to consonants
                if consonant_count == 0:
                    ratio = "undefined (no consonants)"
                else:
                    ratio = f"{vowel_count / consonant_count:.2f}"
                
                # Count unique characters
                unique_chars = len(set(reversed_string))
                
                # Calculate the percentage of alphabetic characters
                alpha_percent = (sum(1 for char in reversed_string if char.isalpha()) / len(reversed_string)) * 100
                
                # Return the processed string with additional information
                return f"processed: {capitalized_reversed} (vowels: {vowel_count}, consonants: {consonant_count}, vowel/consonant ratio: {ratio}, unique characters: {unique_chars}, alphabetic character percentage: {alpha_percent:.2f}%)"