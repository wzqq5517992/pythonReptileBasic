
import os
import requests
from concurrent.futures import ThreadPoolExecutor  # 线程池


def get_Video_lists():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "Origin": "http://stu.ityxb.com",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Host": "stu.ityxb.com",
            "Referer": "http://stu.ityxb.com/index.html",
        }
        data = {'publicCourseId': '270', 'record': ''}
        response = requests.post('http://stu.ityxb.com/bxg_anon/course/public/course/find', headers=headers, data=data,
                                 timeout=30)
        response.encoding = 'utf-8'
        Json_inf = response.json()
        videos_List = Json_inf['resultObject']['studentCourseGraduationVo']['videos']
        Video_lists = []
        for i, videos_url_item in enumerate(videos_List):
            # 将信息存入字典，再将字典加入到列表里
            Videodict = {}
            Videodict['videoPath'] = videos_url_item['videoPath']
            Videodict['title'] = videos_url_item['title']
            Video_lists.append(Videodict)
        del videos_List
        return Video_lists
    except Exception as err:
        print(err)


def getMP4(Videodict):
    videoPath = Videodict['videoPath']
    title = Videodict['title']
    Savepath = f'/Users/jolin/Downloads/wzq123/{title}.mp4'
    if os.path.isfile(Savepath):
        print('文件已存在，无需下载')
        return
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Accept-Language": "identity;q=1, *;q=0",
        "Referer": "http://stu.ityxb.com/index.html",
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


if __name__ == '__main__':
    Video_lists = get_Video_lists()
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(getMP4, Video_lists)
