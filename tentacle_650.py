def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        document_type = 'unknown'
        detected_elements = ['html document', 'html5']
        
        # Determine the type of HTML document and add relevant elements
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
            detected_elements.extend(['wikipedia page', 'statistics', 'data visualization'])
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
            detected_elements.extend(['wikipedia page', 'equations', 'theorems'])
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
            detected_elements.extend(['wikipedia page', 'natural language processing', 'algorithms'])
        
        # Add the document type to detected elements
        detected_elements.append(document_type)
        
        # Return a sorted, comma-separated list of detected elements
        return ','.join(sorted(detected_elements))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, split it into words, sort them, and join with commas
        words = sorted(str(result).lower().split())
        
        # If the result is a single number, return it as is
        if len(words) == 1 and words[0].replace('.', '').isdigit():
            return words[0]
        
        # Otherwise, return the sorted, comma-separated list of words
        return ','.join(words)
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        words = sorted(str(input_data).lower().split())
        
        # Add additional detected elements based on the input
        if 'data' in words:
            words.append('data analysis')
        if 'math' in words or 'equation' in words or 'number' in words:
            words.append('mathematics')
        if 'text' in words or 'word' in words or 'sentence' in words:
            words.append('text processing')
        
        # Return the sorted, comma-separated list of words
        return ','.join(sorted(words))