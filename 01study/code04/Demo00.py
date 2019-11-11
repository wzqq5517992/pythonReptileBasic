# https://yuese62.com/get_file/1/e9f900fd55fc721da9f389e7409e8a074a373789e0/23000/23674/23674.mp4/?br=710&rnd=1573266269852
# https://xuexi.boxuegu.com/playback.html?id=1762&courseId=1485

import os
import requests


def getMP4():
    videoPath = "https://yuese62.com/get_file/1/e9f900fd55fc721da9f389e7409e8a074a373789e0/23000/23674/23674.mp4/?br=710&rnd=1573266269852";
    title = "wzqassd"
    Savepath = f'G:\\wzq\\{title}.mp4'
    if os.path.isfile(Savepath):
        print('文件已存在，无需下载')
        return
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36",
        "zh-CN, zh;q=0.9": "identity;q=1, *;q=0",
        # "referer": "https://yuese63.com/",
        # "upgrade-insecure-requests": 1,
        # "cookie": "__cfduid=da281ac0401d984e10dc4b356ce34ac081573268922; PHPSESSID=jmr00kcnvtsa9he42qlnjue3o3; kt_ips=27.189.229.224; UM_distinctid=16e4e2299e9217-0ae839ada04be3-22722347-59c25-16e4e2299ea449; CNZZDATA1275431286=537568110-1573268415-%7C1573268415; kt_tcookie=1; _ga=GA1.2.1259212009.1573268922; _gid=GA1.2.1867990856.1573268922; _gat_gtag_UA_84734824_7=1; kt_is_visited=1",
        # "cache-control": "max-age=0",
        # "accept-language": "zh-CN, zh;q=0.9",
        # "accept-encoding": "gzip, deflate, br",
        #  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # ":scheme": "https",
        # ":path": "/",
        # ":method": "GET",
        # ":authority": "yuese63.com"
    }
    response = requests.get(videoPath, headers=headers)
    print(response.status_code);
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


if __name__ == '__main__':
    getMP4()
