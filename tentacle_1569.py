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
            # New feature: Extract the title from the HTML if possible
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                return f"generic html document detected: {title_match.group(1)}"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
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
                return str(input_data).lower()
            except ValueError:
                # If not a number, reverse the string, capitalize the first letter, and add a prefix
                reversed_string = input_data[::-1].lower()
                # Count the number of vowels in the reversed string
                vowel_count = sum(1 for char in reversed_string if char in 'aeiou')
                # Check for specific keywords related to HTML document types
                keywords = ['data', 'analysis', 'mathematics', 'text', 'processing']
                found_keywords = [word for word in keywords if word in reversed_string]
                
                # New feature: Calculate the length of the reversed string
                string_length = len(reversed_string)
                
                if found_keywords:
                    return f"processed: {reversed_string.capitalize()} (length: {string_length}, vowels: {vowel_count}, keywords: {', '.join(found_keywords)})"
                else:
                    return f"processed: {reversed_string.capitalize()} (length: {string_length}, vowels: {vowel_count})"