def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
        else:
            document_type = 'unknown'
        
        # Extract and process the title of the HTML document
        title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
        title = title_match.group(1) if title_match else 'unknown title'
        
        # Return a sorted, comma-separated list of detected elements
        return ','.join(sorted(['html document', document_type, title.lower()]))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, split it into words, sort them, and join with commas
        words = str(result).lower().split()
        
        # If the result is a number, add its square root to the output
        if isinstance(result, (int, float)):
            words.append(str(round(result**0.5, 2)))
        
        return ','.join(sorted(words))
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        words = str(input_data).lower().split()
        
        # Count the number of unique words and add it to the output
        unique_word_count = len(set(words))
        words.append(f'{unique_word_count} unique words')
        
        return ','.join(sorted(words))