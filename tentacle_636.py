def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            return 'data analysis html document detected'
        elif 'mathematics' in lowercase_input:
            return 'mathematics html document detected'
        elif 'text processing' in lowercase_input:
            return 'text processing html document detected'
        else:
            return 'generic html document detected'
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result
        if isinstance(result, (int, float)):
            # If the result is a number, return it as is
            return str(result).lower()
        else:
            # Convert to string, split into words, sort them, and join with commas
            sorted_words = ','.join(sorted(str(result).lower().split()))
            
            # Check for specific keywords in the sorted words
            if 'data' in sorted_words and 'analysis' in sorted_words:
                return f'{sorted_words} - related to data analysis'
            elif 'mathematics' in sorted_words:
                return f'{sorted_words} - related to mathematics'
            elif 'text' in sorted_words and 'processing' in sorted_words:
                return f'{sorted_words} - related to text processing'
            else:
                return sorted_words
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        sorted_words = ','.join(sorted(str(input_data).lower().split()))
        
        # Check for specific keywords in the sorted words
        if 'data' in sorted_words and 'analysis' in sorted_words:
            return f'{sorted_words} - related to data analysis'
        elif 'mathematics' in sorted_words:
            return f'{sorted_words} - related to mathematics'
        elif 'text' in sorted_words and 'processing' in sorted_words:
            return f'{sorted_words} - related to text processing'
        else:
            return sorted_words