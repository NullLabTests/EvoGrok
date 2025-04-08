def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        return analyze_html_document(input_data)
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        return analyze_math_result(result, input_data)
    except Exception as e:
        # If evaluation fails, process the input as text
        return analyze_text(input_data, str(e))

def analyze_html_document(html_data):
    document_type = 'unknown'
    detected_elements = ['html document']
    
    # Determine the type of HTML document and add relevant elements
    if 'data analysis' in html_data.lower():
        document_type = 'data analysis'
        detected_elements.extend(['wikipedia page', 'html5', 'data analysis'])
    elif 'mathematics' in html_data.lower():
        document_type = 'mathematics'
        detected_elements.extend(['wikipedia page', 'html5', 'mathematics'])
    elif 'text processing' in html_data.lower():
        document_type = 'text processing'
        detected_elements.extend(['wikipedia page', 'html5', 'text processing'])
    
    # Add the document type to detected elements
    detected_elements.append(document_type)
    
    # Extract additional information from the HTML
    language = None
    if 'lang="' in html_data.lower():
        start = html_data.lower().index('lang="') + 6
        end = html_data.lower().index('"', start)
        language = html_data[start:end]
    
    # Extract class attributes
    classes = []
    for match in re.finditer(r'class="([^"]*)"', html_data, re.IGNORECASE):
        classes.extend(match.group(1).split())
    
    # Return a dictionary with HTML-specific information
    return {
        'type': 'html',
        'document_type': document_type,
        'elements': sorted(detected_elements),
        'language': language,
        'classes': sorted(set(classes)),
        'original_input': html_data.strip()
    }

def analyze_math_result(result, original_input):
    if isinstance(result, (int, float)):
        # If the result is a number, return it with additional information
        return {
            'type': 'number',
            'value': result,
            'string_value': str(result).lower(),
            'is_integer': isinstance(result, int),
            'is_positive': result > 0,
            'original_input': original_input.strip()
        }
    else:
        # Convert the result to a string, split it into words, sort them
        words = sorted(str(result).lower().split())
        
        # Return the sorted words as a list with additional information
        return {
            'type': 'math_result',
            'words': words,
            'word_count': len(words),
            'unique_words': len(set(words)),
            'original_result': str(result),
            'original_input': original_input.strip()
        }

def analyze_text(text_input, error):
    # Convert to lowercase, split into words, sort them
    words = sorted(str(text_input).lower().split())
    
    # Check if the input might be related to HTML document types
    related_to_html = any(term in text_input.lower() for term in ['data analysis', 'mathematics', 'text processing'])
    
    # Calculate word frequencies
    word_frequencies = {}
    for word in words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    
    # Return the sorted words as a list with additional information
    return {
        'type': 'text',
        'words': words,
        'word_count': len(words),
        'unique_words': len(set(words)),
        'related_to_html': related_to_html,
        'word_frequencies': word_frequencies,
        'original_input': text_input.strip(),
        'error': error if error else None
    }