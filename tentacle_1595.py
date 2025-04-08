def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        input_lower = input_data.lower()
        if 'data analysis' in input_lower:
            return "Wikipedia Data Analysis HTML document detected - This document likely contains information about statistical methods and data processing techniques."
        elif 'mathematics' in input_lower:
            return "Wikipedia Mathematics HTML document detected - This document covers various mathematical concepts and theories."
        elif 'text processing' in input_lower:
            return "Wikipedia Text Processing HTML document detected - This document discusses methods for manipulating and analyzing text data."
        else:
            return "Generic HTML document detected - This document may contain various types of content."

    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return f"Mathematical expression evaluated: {str(result).lower()}"
    except:
        # If evaluation fails, process the input as a string
        if ',' in input_data:
            # Sort and join comma-separated values
            sorted_values = sorted(input_data.split(','))
            # Remove any leading/trailing whitespace from each value
            cleaned_values = [value.strip() for value in sorted_values]
            # Join the cleaned values with commas
            result = ','.join(cleaned_values).lower()
        else:
            # Return the input as a lowercase string
            result = str(input_data).lower()
        
        # Check if the result contains any of the HTML document types
        if 'data analysis' in result:
            return f"{result}, related to Wikipedia Data Analysis HTML document - statistical methods and data processing techniques may be discussed."
        elif 'mathematics' in result:
            return f"{result}, related to Wikipedia Mathematics HTML document - various mathematical concepts and theories may be covered."
        elif 'text processing' in result:
            return f"{result}, related to Wikipedia Text Processing HTML document - methods for manipulating and analyzing text data may be discussed."
        else:
            # Check if the input can be converted to a number
            try:
                float(result)
                return f"Numeric value detected: {result}"
            except ValueError:
                # If not a number, check for potential acronyms
                words = result.split()
                acronyms = [word for word in words if word.isupper() and len(word) > 1]
                if acronyms:
                    return f"Possible acronym(s) detected: {', '.join(acronyms)} in '{result}'"
                
                # New feature: Check for specific keywords related to the HTML document types
                keywords = ['statistics', 'data processing', 'mathematical concepts', 'theories', 'text manipulation', 'text analysis']
                found_keywords = [kw for kw in keywords if kw in result]
                
                if found_keywords:
                    return f"{result}, containing keywords related to: {', '.join(found_keywords)}"
                
                # New feature: Check for potential email addresses
                import re
                email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                emails = re.findall(email_pattern, result)
                if emails:
                    return f"Potential email address(es) detected: {', '.join(emails)} in '{result}'"
                
                # If no special cases are detected, return the processed input
                return result