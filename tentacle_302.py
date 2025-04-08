def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document
        document_type = 'unknown'
        detected_elements = ['html document']
        
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
            detected_elements.append('wikipedia page')
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
            detected_elements.append('wikipedia page')
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
            detected_elements.append('wikipedia page')
        
        # Add the document type to detected elements
        detected_elements.append(document_type)
        
        # Return a sorted, comma-separated list of detected elements
        return ','.join(sorted(detected_elements))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it into words, sort them, and join with commas
        return ','.join(sorted(str(result).lower().split()))
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        return ','.join(sorted(str(input_data).lower().split()))