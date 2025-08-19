# 1. Use official Python image
FROM python:3.11.3

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements file first (for caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your app code
COPY . .

# 6. Set the default command to run your app
CMD ["python", "main.py"]
