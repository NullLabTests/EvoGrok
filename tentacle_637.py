def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return 'data analysis wikipedia page detected'
        elif 'mathematics' in lowercase_input:
            return 'mathematics wikipedia page detected'
        elif 'text processing' in lowercase_input:
            return 'text processing wikipedia page detected'
        else:
            return 'generic html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # If the result is a number, return it with two decimal places
            return f"{result:.2f}".lower()
        elif isinstance(result, str):
            # If the result is a string, split it into words, sort them, and join with commas
            sorted_words = ','.join(sorted(result.lower().split()))
            return sorted_words
        else:
            # For other types, return the string representation
            return str(result).lower()
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        sorted_words = ','.join(sorted(str(input_data).lower().split()))
        
        # Process the sorted words based on their count
        if len(sorted_words.split(',')) == 1:
            # If there's only one word, return it as is
            return sorted_words
        elif len(sorted_words.split(',')) <= 3:
            # If there are 2 or 3 words, join them with spaces
            return ' '.join(sorted_words.split(','))
        else:
            # For more than 3 words, return the sorted words joined with commas
            return sorted_words