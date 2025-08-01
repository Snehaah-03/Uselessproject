import os

cascade_path = os.path.join(os.path.dirname(__file__), 'haarcascades', 'haarcascade_eye.xml')

print("Checking for file at:", cascade_path)
print("Exists:", os.path.exists(cascade_path))
