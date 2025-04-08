def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Categorize known HTML document types
        if 'data analysis' in lowercase_input:
            return analyze_html_document(lowercase_input, "data analysis", ["analysis", "data", "of"], "high")
        elif 'mathematics' in lowercase_input:
            return analyze_html_document(lowercase_input, "mathematics", ["mathematics"], "medium")
        elif 'text processing' in lowercase_input:
            return analyze_html_document(lowercase_input, "text processing", ["processing", "text"], "low")
        else:
            # Analyze unknown HTML documents
            return analyze_html_document(lowercase_input, "unknown", [], "unknown")
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        return analyze_result(str(result), True)
    except:
        # If evaluation fails, process the input as text
        return analyze_result(str(input_data), False)

def analyze_html_document(input_data, doc_type, expected_words, complexity_level):
    # Extract content between first '>' and '<'
    content = input_data.split('>', 1)[1].split('<', 1)[0]
    words = content.split()
    
    # Calculate metrics
    word_count = len(words)
    unique_words = len(set(words))
    sorted_content = ','.join(sorted(words))
    complexity = unique_words / word_count if word_count > 0 else 0
    
    # Check for expected words
    found_words = [word for word in expected_words if word in words]
    
    return f"{doc_type} html document detected, word count: {word_count}, unique words: {unique_words}, complexity: {complexity:.2f}, expected words found: {len(found_words)}/{len(expected_words)}, sorted content: '{sorted_content}', complexity level: {complexity_level}".lower()

def analyze_result(input_data, evaluated):
    # Convert to lowercase, split, sort, and join
    lowercase_input = input_data.lower()
    words = lowercase_input.split()
    sorted_input = ','.join(sorted(words))
    
    # Calculate metrics
    word_count = len(words)
    unique_words = len(set(words))
    complexity = unique_words / word_count if word_count > 0 else 0
    
    return f"{sorted_input}, length: {len(sorted_input)}, word count: {word_count}, unique words: {unique_words}, complexity: {complexity:.2f}, evaluated: {evaluated}".lower()