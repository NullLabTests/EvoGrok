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
            detected_elements.extend(['wikipedia page', 'equations', 'proofs'])
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
        
        # If the result is a number, return it as a string
        if isinstance(result, (int, float)):
            return str(result).lower()
        
        # If the result is a string, process it like text input
        elif isinstance(result, str):
            words = sorted(result.lower().split())
            return ','.join(words) if len(words) > 1 else words[0]
        
        # For other types of results, convert to string and process
        else:
            words = sorted(str(result).lower().split())
            return ','.join(words) if len(words) > 1 else words[0]
    
    except:
        # If evaluation fails, process the input as text
        if isinstance(input_data, str):
            words = sorted(input_data.lower().split())
            return ','.join(words) if len(words) > 1 else words[0]
        else:
            # For non-string inputs, convert to string and process
            words = sorted(str(input_data).lower().split())
            return ','.join(words) if len(words) > 1 else words[0]