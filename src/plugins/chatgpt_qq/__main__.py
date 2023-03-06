"""
Each plugin should have __main__.py, which Future Yasiro will start plugin from
"""
from plugins.chatgpt_qq.chatgpt_qq import main

if __name__ == '__main__':
    main()