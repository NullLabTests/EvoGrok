def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on the title and content
        lowercase_input = input_data.lower()
        if 'data analysis' in lowercase_input:
            word_count = len(lowercase_input.split())
            class_count = lowercase_input.count('class=')
            return f"data analysis html document detected, word count: {word_count}, class count: {class_count}".lower()
        elif 'mathematics' in lowercase_input:
            word_count = len(lowercase_input.split())
            doctype_length = len(lowercase_input.split('<!doctype')[1].split('>')[0])
            return f"mathematics html document detected, word count: {word_count}, doctype length: {doctype_length}".lower()
        elif 'text processing' in lowercase_input:
            word_count = len(lowercase_input.split())
            html_tag_count = lowercase_input.count('<html')
            return f"text processing html document detected, word count: {word_count}, html tag count: {html_tag_count}".lower()
        else:
            word_count = len(lowercase_input.split())
            return f"html document detected, word count: {word_count}".lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string, split it, sort it, and join it
        sorted_result = ','.join(sorted(str(result).split()))
        # Calculate various statistics about the result
        result_length = len(sorted_result)
        word_count = len(str(result).split())
        unique_words = len(set(str(result).split()))
        numeric_value = float(result) if isinstance(result, (int, float)) else None
        return f"{sorted_result}, length: {result_length}, word count: {word_count}, unique words: {unique_words}, numeric value: {numeric_value}"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split, sort, and join
        lowercase_input = str(input_data).lower()
        sorted_input = ','.join(sorted(lowercase_input.split()))
        # Calculate various statistics about the input
        input_length = len(sorted_input)
        word_count = len(lowercase_input.split())
        unique_words = len(set(lowercase_input.split()))
        vowel_count = sum(1 for char in lowercase_input if char in 'aeiou')
        return f"{sorted_input}, length: {input_length}, word count: {word_count}, unique words: {unique_words}, vowel count: {vowel_count}"