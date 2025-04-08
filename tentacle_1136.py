def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        document_type = 'unknown'
        detected_elements = ['html document']
        
        # Determine the type of HTML document and add relevant elements
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
            detected_elements.extend(['wikipedia page', 'html5', 'statistics', 'data visualization', 'analysis'])
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
            detected_elements.extend(['wikipedia page', 'html5', 'algebra', 'geometry', 'equation'])
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
            detected_elements.extend(['wikipedia page', 'html5', 'nlp', 'regex', 'string'])
        
        # Add the document type to detected elements
        detected_elements.append(document_type)
        
        # Check for additional keywords and add them to detected elements
        if 'wikipedia' in input_data.lower():
            detected_elements.append('wikipedia')
        if 'html5' in input_data.lower():
            detected_elements.append('html5')
        
        # Attempt to evaluate the content as a mathematical expression
        try:
            content = input_data.split('>', 1)[1].split('<', 1)[0].strip()
            result = eval(content)
            detected_elements.append(f"evaluated result: {str(result).lower()}")
        except:
            pass
        
        # Return a sorted, comma-separated list of unique detected elements
        return ','.join(sorted(set(detected_elements)))
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string and lowercase it
        result_str = str(result).lower()
        
        # Check if the result is a single number
        if result_str.replace('.', '').replace('-', '').isdigit():
            return f"numeric result: {result_str}"
        
        # If not a single number, split into words, sort, and join with commas
        words = sorted(result_str.split())
        
        # Check for specific keywords and add them to the beginning of the result
        keywords = []
        if 'data' in words or 'analysis' in words:
            keywords.append('data analysis')
        if 'math' in words or 'equation' in words or 'algebra' in words or 'geometry' in words:
            keywords.append('mathematics')
        if 'text' in words or 'string' in words or 'nlp' in words or 'regex' in words:
            keywords.append('text processing')
        
        return f"evaluated expression: {','.join(keywords + words)}"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split into words, sort them, and join with commas
        words = sorted(str(input_data).lower().split())
        
        # Check for specific keywords and add them to the beginning of the result
        keywords = []
        if 'data' in words or 'analysis' in words:
            keywords.append('data analysis')
        if 'math' in words or 'equation' in words or 'algebra' in words or 'geometry' in words:
            keywords.append('mathematics')
        if 'text' in words or 'string' in words or 'nlp' in words or 'regex' in words:
            keywords.append('text processing')
        
        return f"processed text: {','.join(keywords + words)}"