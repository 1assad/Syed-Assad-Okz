import os, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
os.system('xdg-open https://youtube.com')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from ZS import bnsbuy
    bnsbuy()
elif bit == '32bit':
    from Assad import bnsbuy
    bnsbuy()
    import setuptools
    bit = platform.architecture()[0]
    if  bit == '32bit':
        from abc import get_cache_token
        if True:
            import token
