# 1️⃣ Use an official Python runtime as a base image
FROM python:3.9

# 2️⃣ Set the working directory inside the container
WORKDIR /app

# 3️⃣ Copy project files into the container
COPY . /app/

# 4️⃣ Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5️⃣ Expose the port your app will run on (important for Railway)
EXPOSE 8000

# 6️⃣ Run Gunicorn to start the Django app (same as your Procfile)
CMD ["gunicorn", "Abbey_Monastry.wsgi:application", "--bind", "0.0.0.0:8000", "--log-file", "-"]
