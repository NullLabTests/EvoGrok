def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect the type of HTML document based on the knowledge
        if 'data analysis' in input_data.lower():
            return 'data analysis html document detected: wikipedia page'.lower()
        elif 'mathematics' in input_data.lower():
            return 'mathematics html document detected: wikipedia page'.lower()
        elif 'text processing' in input_data.lower():
            return 'text processing html document detected: wikipedia page'.lower()
        else:
            return 'html document detected'.lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # If the result is a number, return it with a descriptive message and its square
            squared_result = result ** 2
            return f"mathematical result: {result}, squared: {squared_result}"
        else:
            # Convert the result to a string, split it into words, sort them, 
            # join with commas, and count the number of words
            processed_result = ','.join(sorted(str(result).lower().split()))
            word_count = len(str(result).split())
            return f"processed result: {processed_result}, word count: {word_count}"
    except:
        # If evaluation fails, process the input
        if isinstance(input_data, (int, float)):
            # If input is a number, return it with a descriptive message and its square root
            import math
            square_root = math.sqrt(abs(input_data))
            return f"numeric input: {input_data}, square root: {square_root:.2f}"
        else:
            # Convert the input to a string, split it into words, sort them, 
            # join with commas, and count the number of words
            processed_input = ','.join(sorted(str(input_data).lower().split()))
            word_count = len(str(input_data).split())
            return f"processed input: {processed_input}, word count: {word_count}"