# -*- coding: utf-8 -*-

#### @Author   : liang
#### @Date     : 2016-11-15
#### @Descript : Use this script to copy png files and modify json files for LuaLobby package.

import sys
import json
import time
import os.path
import shutil
### 读写带有中文的json数据的时候，需要引入utf-8
reload(sys)
sys.setdefaultencoding('utf8')


##################  read and write json files
## 从SourceData.json取数据，分别写入到需要被修改的json文件中
JsonFileSrc = "./SourceData.json"
## ********* 需要被修改的json文件目录 *********
JsonFileDes_lobby = "../res/config/lobby.json"
JsonFileDes_login = "../res/config/login.json"
JsonFileDes_options = "../res/config/options.json"
JsonFileDes_loadPreamblecfg = "../res/loadPreamble/loadPreambleCfg.json"

## 读取函数
def load(JsonFile):
 with open(JsonFile) as json_file:
  data = json.load(json_file)
  return data

## 保存函数
def store(js_data, str_filePath):
 with open(str_filePath, 'w') as json_file:
  json_file.write(json.dumps(js_data, sort_keys=True, ensure_ascii=False, indent=4))



#################  copy png(include .html,.mp4) files to another path
### 定义 N 个需要替换的文件（带路径）...
fileNeedReplaceNum = 7
SrcDict = {
 "pngFileSrc_0" : "./res/html/fuwuxieyi.html",
 "pngFileSrc_1" : "./res/image/ui/login/gameTitle.png",
 "pngFileSrc_2" : "./res/image/ui/login/lobbyWelcom2.png",
 "pngFileSrc_3" : "./res/image/ui/mainScene/7pmi.png",
 "pngFileSrc_4" : "./res/image/ui/mainScene/topTitle_01.png",
 "pngFileSrc_5" : "./res/loadPreamble/loading--donghua/gameTitle.png",
 "pngFileSrc_6" : "./res/loadPreamble/startVideo.mp4"
}

DesDict = {
 "pngFileDes_0" : "../res/html/fuwuxieyi.html",
 "pngFileDes_1" : "../res/image/ui/login/gameTitle.png",
 "pngFileDes_2" : "../res/image/ui/login/lobbyWelcom2.png",
 "pngFileDes_3" : "../res/image/ui/mainScene/7pmi.png",
 "pngFileDes_4" : "../res/image/ui/mainScene/topTitle_01.png",
 "pngFileDes_5" : "../res/loadPreamble/loading--donghua/gameTitle.png",
 "pngFileDes_6" : "../res/loadPreamble/startVideo.mp4"
}



## 从某个目录 拷贝文件 到 另一个目录
def myCopyFile(sourFile, destFile):
 shutil.copyfile(sourFile, destFile)






if __name__ == "__main__":

#### 判断路径放置的是否正确
 if os.path.exists("../res"):
  print "目标文件夹 res存在."
 else:
  print "【error】: 上级目录文件夹res 不存在 ***** 请先检查路径配置."
 if os.path.exists("./res"):
  print "同级目录文件夹 res存在."
 else:
  print "【error】: 同级目录文件夹res 不存在 ***** 请先检查路径配置."
    

## ================================ 修改json文件
## ---- 先读取这几个json文件
 dataJsonSrc = load(JsonFileSrc)
 dataJson_lobby = load(JsonFileDes_lobby)
 dataJson_login = load(JsonFileDes_login)
 dataJson_options = load(JsonFileDes_options)
 dataJson_loadPreamblecfg = load(JsonFileDes_loadPreamblecfg)

## ------ lobby.json 大厅站点,大厅服务器域名,跳转链接,活动链接
 dataJson_lobby["iLobbySiteID"] = dataJsonSrc["lobby"]["iLobbySiteID"]
 dataJson_lobby["lobbyServer"][0]["ip"] = dataJsonSrc["lobby"]["ip"]
 dataJson_lobby["domain"] = dataJsonSrc["lobby"]["domain"]
 dataJson_lobby["activityDomain"] = dataJsonSrc["lobby"]["activityDomain"]

## ------ login.json 登录服务器域名，站点，跳转链接，渠道号
 dataJson_login["socket"]["server"][0]["ip"] = dataJsonSrc["login"]["ip0"]
 dataJson_login["socket"]["server"][1]["ip"] = dataJsonSrc["login"]["ip1"]
 dataJson_login["socket"]["iSiteID"] = dataJsonSrc["login"]["iSiteID"]
 dataJson_login["domain"] = dataJsonSrc["login"]["domain"]
 dataJson_login["http"]["channelID"] = dataJsonSrc["login"]["channelID"]

## ------ options.json 微信登录的appid,秘钥，iOS购买的id
 dataJson_options["sWxAppId"] = dataJsonSrc["options"]["sWxAppId"]
 dataJson_options["sWxSecret"] = dataJsonSrc["options"]["sWxSecret"]
 dataJson_options["sIosProductId"] = dataJsonSrc["options"]["sIosProductId"]

## ------ loadPreambleCfg.json
 dataJson_loadPreamblecfg["sChannelId"] = dataJsonSrc["loadPreambleCfg"]["sChannelId"]
 dataJson_loadPreamblecfg["sVerifyChannelId"] = dataJsonSrc["loadPreambleCfg"]["sVerifyChannelId"]
 dataJson_loadPreamblecfg["iSiteId"] = dataJsonSrc["loadPreambleCfg"]["iSiteId"]
 dataJson_loadPreamblecfg["sUrl"] = dataJsonSrc["loadPreambleCfg"]["sUrl"]

## ------ 保存json
 store(dataJson_lobby, JsonFileDes_lobby)
 store(dataJson_login, JsonFileDes_login)
 store(dataJson_options, JsonFileDes_options)
 store(dataJson_loadPreamblecfg, JsonFileDes_loadPreamblecfg)
 print "%s : Write Json files finished! " %(time.strftime("%Y%m%d"))


## =============================== 替换若干ui资源
 for num in range(0, fileNeedReplaceNum):
  tempKeySrc = "%s" %("pngFileSrc_" + "%d" %(num))
  tempKeyDes = "%s" %("pngFileDes_" + "%d" %(num))
  tempPathSrc = "%s" %(SrcDict[tempKeySrc])
  tempPathDes = "%s" %(DesDict[tempKeyDes])
  print "tempPathSrc=%s,  tempPathDes=%s" %(tempPathSrc, tempPathDes)
  myCopyFile(tempPathSrc, tempPathDes)
  print "%s : copy success! DestFileName=%s " %(time.strftime("%Y%m%d"), tempPathDes)


#### 全部执行完成
 print "%s : ****************** FINISHED !!! ******************" %(time.strftime("%Y%m%d"))




