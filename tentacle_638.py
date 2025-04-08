def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return 'data analysis html document detected'
        elif 'mathematics' in input_data.lower():
            return 'mathematics html document detected'
        elif 'text processing' in input_data.lower():
            return 'text processing html document detected'
        else:
            return 'generic html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # If the result is a number, return it as a string with two decimal places
            return f"{result:.2f}".lower()
        else:
            # Convert the result to a string, split it into words, sort them, and join with commas
            sorted_words = ','.join(sorted(str(result).lower().split()))
            return sorted_words
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        sorted_words = ','.join(sorted(str(input_data).lower().split()))
        
        # Process the sorted words based on their count
        if len(sorted_words.split(',')) == 1:
            # If there's only one word, return it as is
            return sorted_words
        elif len(sorted_words.split(',')) <= 3:
            # If there are 2 or 3 words, join them with spaces instead of commas
            return ' '.join(sorted_words.split(','))
        else:
            # For more than 3 words, return the sorted words joined by commas
            return sorted_words