import uvicorn
import sys
sys.path.append(r'module/ConfigModule')
from ReadConfig import web_host
from ReadConfig import web_port
from public.app_path import app

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=web_host,
        port=web_port
    )
