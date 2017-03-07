class User:
 def __init__(self, username, email, password):
  self.username, self.email, self.password = username, email, password

Jesse = User('Jesse', 'jesse@yh.com', 'googleit!')

print(Jesse.username)