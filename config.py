import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28987210")

API_HASH = os.environ.get("API_HASH", "04f69b63570297dac4e35948e4c6b4b7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7819649400:AAHrXcfn6Wb6gLAU12ASyqf0q6TktsSFH7M") 

FORCE_SUB = os.environ.get("FORCE_SUB", "moviesblaster_links") 

DB_NAME = os.environ.get("DB_NAME", "MBrenamebot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Pravin:944244@cluster0.qe3bn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5239080571').split()]

PORT = os.environ.get("PORT", "8080")
