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
            # Classify unknown HTML documents
            if 'wikipedia' in lowercase_input:
                return "wikipedia html document detected"
            else:
                # New feature: Detect if it's a generic HTML5 document
                if 'html5' in lowercase_input:
                    return "generic html5 document detected"
                else:
                    return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, lowercase it, and add a descriptive prefix
        return f"mathematical result: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as text
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Reverse the sorted values
            reversed_values = sorted_values[::-1]
            # Count the number of items
            item_count = len(reversed_values)
            # New feature: Calculate the sum of numeric values if present
            numeric_sum = sum(float(val) for val in reversed_values if val.replace('.', '').isdigit())
            if numeric_sum:
                return f"{','.join(reversed_values)} (total items: {item_count}, sum: {numeric_sum:.2f})"
            else:
                return f"{','.join(reversed_values)} (total items: {item_count})"
        else:
            # Check if the input is a palindrome
            cleaned_input = ''.join(char.lower() for char in input_data if char.isalnum())
            if cleaned_input == cleaned_input[::-1]:
                return f"palindrome detected: {input_data.lower()}"
            else:
                # Check for common words
                common_words = ['the', 'and', 'to', 'of', 'a', 'in', 'is', 'it']
                word_count = sum(1 for word in input_data.lower().split() if word in common_words)
                if word_count > 0:
                    # New feature: Calculate the percentage of common words
                    total_words = len(input_data.split())
                    percentage = (word_count / total_words) * 100
                    return f"common words detected: {word_count} out of {total_words} words ({percentage:.2f}%)"
                else:
                    # New feature: Check if the input contains any digits
                    if any(char.isdigit() for char in input_data):
                        return f"contains digits: {''.join(char for char in input_data if char.isdigit())}"
                    else:
                        # Return the input as a lowercase string
                        return str(input_data).lower()