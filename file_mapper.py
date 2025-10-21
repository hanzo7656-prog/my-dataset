# file_mapper.py
import json
import os

class FileMapper:
    def __init__(self, base_path="raw_data"):
        self.base_path = base_path
        self.organization = self.load_organization()
    
    def load_organization(self):
        """بارگذاری ساختار سازماندهی"""
        try:
            with open('file_organization.json', 'r') as f:
                return json.load(f)
        except:
            return self.generate_organization()
    
    def generate_organization(self):
        """تولید خودکار ساختار سازماندهی"""
        organization = {
            "organization": {
                "type": "alphabetical",
                "folders": {},
                "total_files": 0
            },
            "index": {}
        }
        
        folders = ['A', 'B', 'C', 'D']
        
        for folder in folders:
            folder_path = os.path.join(self.base_path, folder)
            if os.path.exists(folder_path):
                files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
                coin_names = [f.replace('.json', '') for f in files]
                
                organization["organization"]["folders"][folder] = {
                    "description": f"Coins in {folder}",
                    "file_count": len(files),
                    "coins": coin_names
                }
                
                # ایجاد ایندکس
                for coin in coin_names:
                    organization["index"][coin] = f"{folder}/{coin}.json"
                
                organization["organization"]["total_files"] += len(files)
        
        # ذخیره فایل سازماندهی
        with open('file_organization.json', 'w') as f:
            json.dump(organization, f, indent=2)
        
        return organization
    
    def get_file_path(self, coin_id):
        """دریافت مسیر فایل برای یک کوین"""
        return self.organization["index"].get(coin_id)
    
    def get_all_coins(self):
        """دریافت لیست تمام کوین‌ها"""
        return list(self.organization["index"].keys())

# تست
if __name__ == "__main__":
    mapper = FileMapper()
    print("🔍 ساختار سازماندهی:")
    print(f"📁 تعداد کل فایل‌ها: {mapper.organization['organization']['total_files']}")
    
    # تست جستجو
    test_coins = ["bitcoin", "ethereum", "dogecoin"]
    for coin in test_coins:
        path = mapper.get_file_path(coin)
        print(f"📍 {coin} → {path}")
