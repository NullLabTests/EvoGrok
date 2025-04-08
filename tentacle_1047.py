def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        lowercase_input = input_data.lower()
        
        # Determine the type of HTML document based on the title
        if 'data analysis' in lowercase_input:
            content = ' '.join(lowercase_input.split()[2:])  # Remove DOCTYPE and first tag
            sorted_content = ','.join(sorted(content.split()))
            return f"Data analysis HTML document detected, length: {len(sorted_content)}, content: {sorted_content}"
        elif 'mathematics' in lowercase_input:
            content = ' '.join(lowercase_input.split()[2:])  # Remove DOCTYPE and first tag
            sorted_content = ','.join(sorted(content.split()))
            return f"Mathematics HTML document detected, length: {len(sorted_content)}, content: {sorted_content}"
        elif 'text processing' in lowercase_input:
            content = ' '.join(lowercase_input.split()[2:])  # Remove DOCTYPE and first tag
            sorted_content = ','.join(sorted(content.split()))
            return f"Text processing HTML document detected, length: {len(sorted_content)}, content: {sorted_content}"
        else:
            # If no specific type is detected, process the content
            content = ' '.join(lowercase_input.split()[2:])  # Remove DOCTYPE and first tag
            sorted_content = ','.join(sorted(content.split()))
            return f"Generic HTML document detected, length: {len(sorted_content)}, content: {sorted_content}"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Convert the result to a string, split it, sort it, and join it
        sorted_result = ','.join(sorted(str(result).split()))
        
        # Calculate the length of the original input and the processed result
        original_length = len(str(input_data))
        processed_length = len(sorted_result)
        
        # Return the sorted result, its length, the original result, and the original input length
        return f"Mathematical expression evaluated: {sorted_result}, processed length: {processed_length}, original result: {result}, original input length: {original_length}"
    except:
        # If evaluation fails, process the input as text
        # Convert to lowercase, split, sort, and join
        sorted_input = ','.join(sorted(str(input_data).lower().split()))
        
        # Calculate the length of the original input and the processed result
        original_length = len(str(input_data))
        processed_length = len(sorted_input)
        
        # Return the sorted input, its length, and the original input length
        return f"Text processed: {sorted_input}, processed length: {processed_length}, original input length: {original_length}"