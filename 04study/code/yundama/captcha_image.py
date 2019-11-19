# https://yuese62.com/get_file/1/e9f900fd55fc721da9f389e7409e8a074a373789e0/23000/23674/23674.mp4/?br=710&rnd=1573266269852
# https://xuexi.boxuegu.com/playback.html?id=1762&courseId=1485

import os
import time
import requests


def getImage():
    videoPath = "https://yuese64.com/captcha/logon/"
    # Savepath = f'../images/captcha.jpg'
    Savepath = "F:\\MyOwnCode\\pythonStudy\\pythonReptileBasic\\03study\\book\\book\\images\\captcha.jpg"
    t = str(int(time.time() * 1000))
    hou = "?rand={0}".format(t)
    # if os.path.isfile(Savepath):
    #     print('文件已存在，无需下载')
    #     return
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36",
        "zh-CN, zh;q=0.9": "identity;q=1, *;q=0",
    }
    response = requests.get(videoPath, headers=headers)
    print(response.status_code)
    if response.status_code == 403:
        print('403 服务器拒绝请求')
        return
    elif response.status_code == 404:
        print('404 not found')
        return
    with open(Savepath, "wb") as f:
        f.write(response.content)
    print(videoPath)
    response.close()
    return response.content


if __name__ == '__main__':
    getImage()
