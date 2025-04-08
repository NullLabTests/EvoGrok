def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Convert input to lowercase for easier comparison
        lower_input = input_data.lower()
        
        # Check for specific topics based on the knowledge
        if 'data analysis' in lower_input:
            return "data analysis html document detected"
        elif 'mathematics' in lower_input:
            return "mathematics html document detected"
        elif 'text processing' in lower_input:
            return "text processing html document detected"
        else:
            return "html document detected"
    
    # If not an HTML document, process as in Parent1 and Parent2
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, sort the input data as in Parent1
        return ','.join(sorted(input_data.split(','))).lower()