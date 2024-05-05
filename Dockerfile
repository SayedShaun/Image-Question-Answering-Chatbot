FROM python:3.10
ENV PORT=8501
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]