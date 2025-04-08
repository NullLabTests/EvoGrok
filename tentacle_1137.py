def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        document_type = 'unknown'
        detected_elements = ['html document']
        
        # Determine the type of HTML document and add relevant elements
        if 'data analysis' in input_data.lower():
            document_type = 'data analysis'
            detected_elements.extend(['wikipedia page', 'html5', 'statistics', 'data visualization', 'data science'])
        elif 'mathematics' in input_data.lower():
            document_type = 'mathematics'
            detected_elements.extend(['wikipedia page', 'html5', 'algebra', 'geometry', 'calculus'])
        elif 'text processing' in input_data.lower():
            document_type = 'text processing'
            detected_elements.extend(['wikipedia page', 'html5', 'nlp', 'regex', 'string manipulation'])
        
        # Add the document type to detected elements
        detected_elements.append(document_type)
        
        # Check for additional keywords and add them to detected elements
        if 'wikipedia' in input_data.lower():
            detected_elements.append('wikipedia')
        if 'html5' in input_data.lower():
            detected_elements.append('html5')
        
        # Process the text content of the HTML document
        content = input_data.lower().replace('\n', ' ').replace('\r', ' ')
        words = sorted(set(content.split()))
        
        # Identify categories based on content
        categories = []
        if 'data' in words or 'analysis' in words:
            categories.append('data analysis')
        if 'math' in words or 'equation' in words or 'number' in words:
            categories.append('mathematics')
        if 'text' in words or 'string' in words or 'word' in words:
            categories.append('text processing')
        
        # Add more specific categories based on the content
        if 'statistic' in words or 'visualization' in words:
            categories.append('data science')
        if 'algebra' in words or 'geometry' in words or 'calculus' in words:
            categories.append('advanced mathematics')
        if 'nlp' in words or 'regex' in words:
            categories.append('advanced text processing')
        
        # Return a structured output for HTML documents
        return {
            'type': 'html_document',
            'detected_elements': sorted(set(detected_elements)),
            'categories': sorted(set(categories)),
            'content_words': words
        }
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string
        result_str = str(result).lower()
        
        # Check if the result is a single number
        if result_str.replace('.', '').replace('-', '').isdigit():
            return {
                'type': 'numeric_result',
                'value': result_str
            }
        
        # If not a single number, process as text
        words = sorted(set(result_str.split()))
        
        # Identify categories based on content
        categories = []
        if 'data' in words or 'analysis' in words:
            categories.append('data analysis')
        if 'math' in words or 'equation' in words or 'number' in words:
            categories.append('mathematics')
        if 'text' in words or 'string' in words or 'word' in words:
            categories.append('text processing')
        
        # Add more specific categories based on the content
        if 'statistic' in words or 'visualization' in words:
            categories.append('data science')
        if 'algebra' in words or 'geometry' in words or 'calculus' in words:
            categories.append('advanced mathematics')
        if 'nlp' in words or 'regex' in words:
            categories.append('advanced text processing')
        
        # Return a structured output for evaluated expressions
        return {
            'type': 'evaluated_expression',
            'result': result_str,
            'categories': sorted(set(categories)),
            'content_words': words
        }
    except:
        # If evaluation fails, process the input as text
        words = sorted(set(str(input_data).lower().split()))
        
        # Identify categories based on content
        categories = []
        if 'data' in words or 'analysis' in words:
            categories.append('data analysis')
        if 'math' in words or 'equation' in words or 'number' in words:
            categories.append('mathematics')
        if 'text' in words or 'string' in words or 'word' in words:
            categories.append('text processing')
        
        # Add more specific categories based on the content
        if 'statistic' in words or 'visualization' in words:
            categories.append('data science')
        if 'algebra' in words or 'geometry' in words or 'calculus' in words:
            categories.append('advanced mathematics')
        if 'nlp' in words or 'regex' in words:
            categories.append('advanced text processing')
        
        # Return a structured output for text inputs
        return {
            'type': 'text_input',
            'categories': sorted(set(categories)),
            'content_words': words
        }