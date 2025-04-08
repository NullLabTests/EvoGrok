def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect the type of HTML document based on the knowledge
        if 'data analysis' in input_data.lower():
            return 'data analysis html document detected'.lower()
        elif 'mathematics' in input_data.lower():
            return 'mathematics html document detected'.lower()
        elif 'text processing' in input_data.lower():
            return 'text processing html document detected'.lower()
        else:
            return 'html document detected'.lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, split it into words, sort them, and join with commas
        sorted_words = ','.join(sorted(str(result).lower().split()))
        
        # Check if the result contains any numbers
        if any(char.isdigit() for char in sorted_words):
            # If numbers are present, return the sorted words with a prefix
            return f"numerical result: {sorted_words}"
        else:
            # If no numbers are present, return the sorted words as is
            return sorted_words
    except:
        # If evaluation fails, convert the input to a string, split it into words, sort them, and join with commas
        sorted_words = ','.join(sorted(str(input_data).lower().split()))
        
        # Check if the result contains any numbers
        if any(char.isdigit() for char in sorted_words):
            # If numbers are present, return the sorted words with a prefix
            return f"non-numerical input with numbers: {sorted_words}"
        else:
            # If no numbers are present, return the sorted words as is
            return sorted_words