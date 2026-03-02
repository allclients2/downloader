from pathlib import Path;
from configs import Configs;

result = Configs.fetch_configs("C:\\Users\\user\\Downloads\\decryptstuff\\cookies.txt")

print("result:", result["accessToken"])
