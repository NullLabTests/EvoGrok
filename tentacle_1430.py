import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        return process_html(input_data)
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        return process_math_result(result, input_data)
    except Exception as e:
        # If evaluation fails, process as text
        return process_text(input_data, str(e))

def process_html(input_data):
    document_type = 'unknown'
    detected_elements = ['html document']
    
    # Determine the type of HTML document and add relevant elements
    if 'data analysis' in input_data.lower():
        document_type = 'data analysis'
        detected_elements.extend(['wikipedia page', 'html5', 'data analysis'])
    elif 'mathematics' in input_data.lower():
        document_type = 'mathematics'
        detected_elements.extend(['wikipedia page', 'html5', 'mathematics'])
    elif 'text processing' in input_data.lower():
        document_type = 'text processing'
        detected_elements.extend(['wikipedia page', 'html5', 'text processing'])
    
    # Add the document type to detected elements
    detected_elements.append(document_type)
    
    # Extract and process the text content of the HTML document
    content = extract_html_content(input_data)
    words = sorted(content.split())
    
    # Analyze word frequencies
    word_frequencies = {word: content.split().count(word) for word in set(words)}
    
    # Return a dictionary with HTML-specific information and text analysis
    return {
        'type': 'html',
        'document_type': document_type,
        'elements': sorted(detected_elements),
        'text_analysis': {
            'words': words,
            'word_count': len(words),
            'word_frequencies': word_frequencies
        },
        'original_input': input_data.strip()
    }

def process_math_result(result, input_data):
    if isinstance(result, (int, float)):
        # If the result is a number, return it with additional information
        return {
            'type': 'number',
            'value': result,
            'string_value': str(result).lower(),
            'text_analysis': {
                'words': sorted(str(result).lower().split()),
                'word_count': len(str(result).lower().split())
            },
            'original_input': input_data.strip()
        }
    else:
        # Convert the result to a string, split it into words, sort them
        words = sorted(str(result).lower().split())
        
        # Return the sorted words as a list with additional information
        return {
            'type': 'math_result',
            'words': words,
            'word_count': len(words),
            'original_result': str(result),
            'original_input': input_data.strip()
        }

def process_text(input_data, error):
    # Convert to lowercase, split into words, sort them
    words = sorted(str(input_data).lower().split())
    
    # Analyze word frequencies
    word_frequencies = {word: str(input_data).lower().split().count(word) for word in set(words)}
    
    # Return the sorted words as a list with additional information
    return {
        'type': 'text',
        'words': words,
        'word_count': len(words),
        'word_frequencies': word_frequencies,
        'original_input': input_data.strip(),
        'error': error if error else None
    }

def extract_html_content(html):
    # Remove HTML tags and extract content
    content = re.sub(r'<[^>]*>', ' ', html)
    return ' '.join(content.split()).lower()