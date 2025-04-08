def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return "data analysis html document detected"
        elif 'mathematics' in lowercase_input:
            return "mathematics html document detected"
        elif 'text processing' in lowercase_input:
            return "text processing html document detected"
        else:
            # Add a new feature to classify unknown HTML documents
            if 'wikipedia' in lowercase_input:
                return "wikipedia html document detected"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as text
        if ',' in input_data:
            # Sort and join comma-separated values (from Parent2)
            sorted_values = sorted(input_data.split(','))
            # Reverse the sorted values (from Parent2)
            reversed_values = sorted_values[::-1]
            # Add a new feature to count the number of items
            item_count = len(reversed_values)
            return f"{','.join(reversed_values)} (total items: {item_count})"
        else:
            # Check if the input is a palindrome (from Parent2)
            cleaned_input = ''.join(char.lower() for char in input_data if char.isalnum())
            if cleaned_input == cleaned_input[::-1]:
                return f"palindrome detected: {input_data.lower()}"
            else:
                # Add a new feature to check for common words
                common_words = ['the', 'and', 'to', 'of', 'a', 'in', 'is', 'it']
                word_count = sum(1 for word in input_data.lower().split() if word in common_words)
                if word_count > 0:
                    return f"common words detected: {word_count} out of {len(input_data.split())} words"
                else:
                    # Return the input as a lowercase string (from Parent1)
                    return str(input_data).lower()