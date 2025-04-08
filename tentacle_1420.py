def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        document_type = 'unknown'
        detected_elements = ['html document', 'html5']
        
        # Determine the type of HTML document and add relevant elements
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
            detected_elements.extend(['wikipedia page', 'statistics', 'data visualization', 'charts', 'tables'])
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
            detected_elements.extend(['wikipedia page', 'equations', 'proofs', 'theorems', 'formulas'])
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
            detected_elements.extend(['wikipedia page', 'natural language processing', 'algorithms', 'tokenization', 'stemming'])
        
        # Add the document type to detected elements
        detected_elements.append(document_type)
        
        # Sort and return a comma-separated list of detected elements
        return ','.join(sorted(detected_elements)).lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # If the result is a number, return it as a string with two decimal places
        if isinstance(result, (int, float)):
            return f"{result:.2f}".lower()
        
        # Otherwise, convert the result to a string, split it into words, sort them, and join with commas
        words = sorted(str(result).lower().split())
        return ','.join(words)
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        words = sorted(str(input_data).lower().split())
        
        # If the result is a single word, return it as is
        if len(words) == 1:
            return words[0]
        
        # For multiple words, check if any word is a number
        numbers = [w for w in words if w.replace('.', '').isdigit()]
        
        if numbers:
            # If numbers are present, return the highest number formatted to two decimal places
            highest_number = max(float(n) for n in numbers)
            return f"{highest_number:.2f}".lower()
        
        # Otherwise, return the sorted, comma-separated list of words
        return ','.join(words)