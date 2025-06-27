# Start project Xupisc URL
* Enable venv enviroment

```
source venv/bin/activate
pip install -r requirements.txt
```

# Create folder qrcode
* Create folder to save images qrcode
```
mkdir qrcode
```

# Start Redis with podman
* Redis to register
```
- podman run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

# Run application
* Run server
```
python server.py
```

* Run application to register urls
```
python main.py
```