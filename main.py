# Write a function to process user data
def process_user_data(user_data):
    processed_data = {}
    for user in user_data:
        user_id = user.get('id')
        name = user.get('name', 'Unknown')
        email = user.get('email', 'No Email Provided')
        
        processed_data[user_id] = {
            'name': name.title(),
            'email': email.lower()
        }
    
    return processed_data

# Suggest helper functions related to processing user data
