import math

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Detect the type of HTML document based on the knowledge
        if 'data analysis' in input_data.lower():
            return 'data analysis html document detected: wikipedia page on data analysis'.lower()
        elif 'mathematics' in input_data.lower():
            return 'mathematics html document detected: wikipedia page on mathematics'.lower()
        elif 'text processing' in input_data.lower():
            return 'text processing html document detected: wikipedia page on text processing'.lower()
        else:
            return 'html document detected: unknown type'.lower()
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        
        # Process the result based on its type
        if isinstance(result, (int, float)):
            # If the result is a number, return it with a descriptive message, its square, and cube
            squared_result = result ** 2
            cubed_result = result ** 3
            return f"mathematical result: {result}, squared: {squared_result}, cubed: {cubed_result}"
        elif isinstance(result, str):
            # If the result is a string, process it and count words
            processed_result = ','.join(sorted(result.lower().split()))
            word_count = len(result.split())
            return f"string result: {processed_result}, word count: {word_count}"
        else:
            # For other types, convert to string, process, and count words
            processed_result = ','.join(sorted(str(result).lower().split()))
            word_count = len(str(result).split())
            return f"processed result: {processed_result}, word count: {word_count}, type: {type(result).__name__}"
    except:
        # If evaluation fails, process the input
        if isinstance(input_data, (int, float)):
            # If input is a number, return it with a descriptive message, its square root, and cube root
            square_root = math.sqrt(abs(input_data))
            cube_root = abs(input_data) ** (1/3)
            return f"numeric input: {input_data}, square root: {square_root:.2f}, cube root: {cube_root:.2f}"
        elif isinstance(input_data, str):
            # If input is a string, process it and count words
            processed_input = ','.join(sorted(input_data.lower().split()))
            word_count = len(input_data.split())
            return f"string input: {processed_input}, word count: {word_count}"
        else:
            # For other types, convert to string, process, and count words
            processed_input = ','.join(sorted(str(input_data).lower().split()))
            word_count = len(str(input_data).split())
            return f"processed input: {processed_input}, word count: {word_count}, type: {type(input_data).__name__}"