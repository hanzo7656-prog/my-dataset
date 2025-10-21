
## 🔗 **آپدیت نهایی `api_client.py`:**

```python
def __init__(self, api_key: str = "oYGlUrdvcdApdgxLTNs9jUnvR/RUGAMhZjt1Z3YtbpA=", 
             base_url: str = "https://openapiv1.coinstats.app",
             # لینک مستقیم به ریپوی داده‌های تو
             data_repo_url: str = "https://raw.githubusercontent.com/hanzo7656-prog/crypto-ai-dataset/main/raw_data"):
    
    self.api_key = api_key
    self.base_url = base_url
    self.data_repo_url = data_repo_url
    self.headers = {"X-API-KEY": api_key}
    self.session = requests.Session()
    self.session.headers.update(self.headers)
    
    # تست اتصال به ریپوی داده‌ها
    self._remote_data_available = self._test_remote_connection()

def _test_remote_connection(self):
    """تست اتصال به ریپوی داده‌ها"""
    try:
        test_url = f"{self.data_repo_url}/coins_list.json"
        response = requests.get(test_url, timeout=10)
        if response.status_code == 200:
            self.logger.info("✅ اتصال به ریپوی داده‌ها برقرار شد")
            return True
        else:
            self.logger.warning("⚠️ ریپوی داده‌ها در دسترس نیست")
            return False
    except Exception as e:
        self.logger.error(f"❌ خطا در اتصال به ریپوی داده‌ها: {e}")
        return False
