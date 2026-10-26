#!/usr/bin/env python
import os, sys, tempfile, requests

# Ensure the backend root is in sys.path so that 'rag' package can be imported if needed
backend_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(backend_root)

def main():
    url = 'http://127.0.0.1:8000/upload'
    # Create a temporary text file with sample content
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as f:
        f.write('Sample document for RAG upload test.')
        temp_path = f.name
    files = {'file': open(temp_path, 'rb')}
    try:
        resp = requests.post(url, files=files)
        print('Status code:', resp.status_code)
        try:
            print('Response JSON:', resp.json())
        except Exception:
            print('Response text:', resp.text)
    finally:
        files['file'].close()
        os.remove(temp_path)

if __name__ == '__main__':
    main()
