# Exported from Render on 2025-05-07T02:22:10Z
services:
- type: web
  name: Rockykingbite
  runtime: python
  repo: https://github.com/Rockykingbite/Rockykingbite
  plan: free
  region: oregon
  buildCommand: 'pip install requests '
  startCommand: python main.py
version: "1"
