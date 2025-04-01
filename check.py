username = input("Enter username: ")
query = "SELECT * FROM users WHERE username = '" + username + "';"
execute_query(query)  # No sanitization
