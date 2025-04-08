def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        html_type = None
        if 'data analysis' in input_data.lower():
            html_type = "data analysis wikipedia page"
        elif 'mathematics' in input_data.lower():
            html_type = "mathematics wikipedia page"
        elif 'text processing' in input_data.lower():
            html_type = "text processing wikipedia page"
        
        if html_type:
            # Extract and process class attributes from the HTML
            class_attributes = []
            start_index = input_data.lower().find('class=')
            if start_index != -1:
                end_index = input_data.find('>', start_index)
                if end_index != -1:
                    class_attr = input_data[start_index+7:end_index].strip().strip('"')
                    class_attributes = [attr.strip() for attr in class_attr.split() if attr.strip()]
            
            # Process and return information about the HTML document
            if class_attributes:
                return f"{html_type} detected with classes: {', '.join(class_attributes)}"
            else:
                return f"{html_type} detected"
        else:
            return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"evaluated: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned and sorted values
            return f"sorted: {', '.join(cleaned_values)}"
        else:
            # Check if the input is a valid number
            try:
                float(input_data)
                return f"number: {str(input_data).lower()}"
            except ValueError:
                # If not a number, reverse the string, capitalize the first letter, and add a prefix
                reversed_string = input_data[::-1].lower()
                # Count the number of vowels in the reversed string
                vowel_count = sum(1 for char in reversed_string if char in 'aeiou')
                # Check for specific keywords related to HTML document types
                keywords = ['data', 'analysis', 'mathematics', 'text', 'processing']
                found_keywords = [word for word in keywords if word in reversed_string]
                
                if found_keywords:
                    return f"processed: {reversed_string.capitalize()} (vowels: {vowel_count}, keywords: {', '.join(found_keywords)})"
                else:
                    return f"processed: {reversed_string.capitalize()} (vowels: {vowel_count})"