# Python 3.9 kullanarak bir temel imaj seçiyoruz
FROM python:3.9-slim

# Çalışma dizinini ayarlıyoruz
WORKDIR /app

# Gereksinimlerinizi kopyalıyoruz
COPY requirements.txt requirements.txt

# Gereksinimleri kuruyoruz
RUN pip install -r requirements.txt

# Uygulama kodunuzu kopyalıyoruz
COPY . .

# Uygulamanızı çalıştırıyoruz
CMD ["python", "app.py"]