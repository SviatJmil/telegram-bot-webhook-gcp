☁️ Деплой у GCP Cloud Run
1. Аутентифікація
```bash

gcloud auth login
gcloud config set project YOUR_PROJECT_ID

2. Побудова образу і деплой
```bash

gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/webhook-server
gcloud run deploy webhook-server \
  --image gcr.io/YOUR_PROJECT_ID/webhook-server \
  --platform managed \
  --region europe-central2 \
  --allow-unauthenticated \
  --port 8080

➡️ Отримаєш HTTPS URL, наприклад:
https://webhook-server-xyz.a.run.app/webhook

✅ Перевірка
bash

curl -X POST https://webhook-server-xyz.a.run.app/webhook \
-H "Content-Type: application/json" \
-H "X-Webhook-Secret: supersecret" \
-d '{"event": "test", "data": {"example": 1}}'


✅ Що ще потрібно:
Dockerfile — він обов’язковий для збірки.
cloudbuild.yaml треба покласти в корінь проєкту.
GCP Cloud Build API має бути ввімкнений.
Cloud Run має бути налаштований (або буде автоматично створено при першому деплої).
За замовчуванням --allow-unauthenticated дозволяє відкритий доступ (що зручно для вебхуків).

🚀 Деплой
Щоб запустити деплой:

```bash

gcloud builds submit --config cloudbuild.yaml


-----------------------

Установка залежностей:
'''bash
pip install -r requirements.txt


Запуск серверу:
'''bash
uvicorn app.main:app --host 0.0.0.0 --port 8080


✅ Запустити у Docker локально
1️⃣ Зберіть образ (переконайтесь, що ви у директорії з Dockerfile):
'''bash
docker build -t webhook-fastapi .

Локально: 
docker build -f Dockerfile.dev -t webhook-fastapi .


2️⃣ Запустіть контейнер, пробросивши порт 8080:
'''bash
docker run -p 8080:8080 webhook-fastapi

----------------------