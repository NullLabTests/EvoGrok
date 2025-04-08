import json
import re

def tentacle(input_data):
    # Check if the input looks like the start of an HTML document
    if isinstance(input_data, str) and input_data.strip().lower().startswith('<!doctype'):
        # Determine the type of HTML document based on known patterns
        if 'data analysis' in input_data.lower():
            return "data analysis html document detected"
        elif 'mathematics' in input_data.lower():
            return "mathematics html document detected"
        elif 'text processing' in input_data.lower():
            return "text processing html document detected"
        else:
            # Attempt to extract the title from the HTML
            title_match = re.search(r'<title>(.*?)</title>', input_data, re.IGNORECASE)
            if title_match:
                return f"html document detected: {title_match.group(1).lower()}"
            else:
                return "generic html document detected"
    
    try:
        # Attempt to evaluate the input as a mathematical expression
        result = eval(input_data)
        # Convert the result to a string and lowercase it
        return str(result).lower()
    except:
        # If evaluation fails, process the input as a string or JSON-like structure
        if isinstance(input_data, str):
            if ',' in input_data or '{' in input_data or '[' in input_data:
                # Process comma-separated values or JSON-like structures
                try:
                    # Attempt to parse as JSON
                    json_obj = json.loads(input_data)
                    processed_values = process_json(json_obj)
                    return ','.join(sorted(processed_values))
                except:
                    # If JSON parsing fails, process as comma-separated values
                    values = [v.strip() for v in input_data.split(',') if v.strip()]
                    processed_values = []
                    for value in values:
                        try:
                            # Attempt to evaluate each value as a mathematical expression
                            eval_result = eval(value)
                            processed_values.append(str(eval_result).lower())
                        except:
                            # If evaluation fails, attempt to parse as JSON
                            try:
                                json_obj = json.loads(value)
                                processed_values.append(json.dumps(json_obj, sort_keys=True).lower())
                            except:
                                # If not JSON, keep the original value
                                processed_values.append(value.lower())
                    # Sort and join the processed values with commas
                    return ','.join(sorted(processed_values))
            else:
                # Convert the input to lowercase and remove leading/trailing whitespace
                return input_data.strip().lower()
        else:
            # For non-string inputs, attempt to convert to JSON
            try:
                return json.dumps(input_data, sort_keys=True).lower()
            except:
                # If JSON conversion fails, return the string representation
                return str(input_data).lower()

def process_json(json_obj):
    if isinstance(json_obj, dict):
        return [f"{k.lower()}:{v.lower()}" for k, v in json_obj.items()]
    elif isinstance(json_obj, list):
        return [str(item).lower() for item in json_obj]
    else:
        return [str(json_obj).lower()]