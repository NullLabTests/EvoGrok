def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        input_lower = input_data.lower()
        
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_lower:
            return "Wikipedia Data Analysis HTML document detected - This document likely contains information about statistical methods, data processing techniques, and data visualization."
        elif 'mathematics' in input_lower:
            return "Wikipedia Mathematics HTML document detected - This document covers various mathematical concepts, theories, and formulas, including algebra, geometry, and calculus."
        elif 'text processing' in input_lower:
            return "Wikipedia Text Processing HTML document detected - This document discusses methods for text manipulation, analysis, and natural language processing."
        else:
            return "Generic HTML document detected - This document may contain various types of content, including text, images, and multimedia elements."

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"Mathematical expression evaluated: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if ',' in str(input_data):
            # Sort and join comma-separated values
            sorted_values = sorted(str(input_data).split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned values with commas
            result = ','.join(cleaned_values).lower()
        else:
            # Return the input as a lowercase string
            result = str(input_data).lower()
        
        # Check if the result contains any of the HTML document types
        html_related = []
        if 'data analysis' in result:
            html_related.append("related to Wikipedia Data Analysis HTML document")
        if 'mathematics' in result:
            html_related.append("related to Wikipedia Mathematics HTML document")
        if 'text processing' in result:
            html_related.append("related to Wikipedia Text Processing HTML document")
        
        if html_related:
            return f"{result}, {' and '.join(html_related)}"
        else:
            return result