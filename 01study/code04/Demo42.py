
import urllib.request
def Dwonprogress(block_num, block_size, total_size):
    '''回调函数
           @block_num: 已经下载的数据块
           @block_size: 数据块的大小
           @total_size: 远程文件的大小
        '''
    # 已下载的百分比，强制类型转为int
    now_jd = int((block_num * block_size / total_size) * 100)
    # #end=" "将print的换行符\n替换成空字符串，也就是打印不换行
    print("\r[%s%s]%d%s" % (">" * now_jd, " " * (100 - now_jd), now_jd, '%'), end="")
requestsurl='https://www.bilibili.com/video/av7036891?from=search&seid=909423272451002266'
video_url='https://upos-hz-mirrorks3u.acgvideo.com/upgcxcode/13/25/11472513/11472513-1-15.flv?e=ig8euxZM2rNcNbeBhwdVtWeBhwdVNEVEuCIv29hEn0lqXg8Y2ENvNCImNEVEUJ1miI7MT96fqj3E9r1qNCNEtodEuxTEtodE9EKE9IMvXBvE2ENvNCImNEVEK9GVqJIwqa80WXIekXRE9IMvXBvEuENvNCImNEVEua6m2jIxux0CkF6s2JZv5x0DQJZY2F8SkXKE9IB5QK==&uipk=5&nbs=1&deadline=1566354810&gen=playurl&os=ks3u&oi=3028936899&trid=be744bda13c9450e8dd0beb3757fdf52u&platform=pc&upsig=323259bae6b5fe9296659c1447c693bc&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0'
Dwonheaders = {
                "Accept": "*/*",
                "Accept- ": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Host": "upos-hz-mirrorwcsu.acgvideo.com",
                "Origin": "https://www.bilibili.com",
                "Referer": f"{requestsurl}",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
                #'User-agent':'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
            }
try:
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-agent',
         'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10'),
        ("Accept", "*/*"),
        ("Accept-Encoding", "gzip, deflate, br"),
        ("Accept-Language","zh-CN,zh;q=0.9"),
        ("Host","upos-hz-mirrorwcsu.acgvideo.com"),
        ("Origin","https://www.bilibili.com"),
        ("Referer",f"{requestsurl}"),
        ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"),
    ]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(video_url, '1.flv', Dwonprogress)  # path为本地保存路径
    opener.close()
except Exception as resultException:
    print(resultException)
    pass