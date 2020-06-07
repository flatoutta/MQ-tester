#!usr/bin/env python
# -*- coding: utf-8 -*- 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbox
import paho.mqtt.client as mqtt
from time import sleep
import datetime

dt_now = datetime.datetime.now()
date_now = dt_now.strftime('%Y-%m-%d %H:%M:%S')


# keep alive設定
global MQTT_KEEP_ALIVE
MQTT_KEEP_ALIVE = 60

# ブローカーに接続できたときの処理
def on_connect(pub_client, userdata, flag, rc):
  print('@"Connected with result code "' + str(rc))
  pub_client.isConnect = True

# ブローカーが切断したときの処理
def on_disconnect(pub_client, userdata, flag, rc):
  if rc != 0:
     print('#"Unexpected disconnection."')
     pass


# publishが完了したときの処理
def on_publish(pub_client, userdata, mid):
  print('@"publish: {0}"'.format(mid) + '\n@Published at :['+ date_now +'] \n')
  pub_client.loop_stop()
  pass

# publish本体
def main_pub(mqttServer, portNum, userName, passWord, topicContent, payloadContent, qosNum, retainBool):
  # if pub_client.isConnect == False:
  pub_client = mqtt.Client()                      # クラスのインスタンス(実体)の作成
  pub_client.on_connect = on_connect                                # 接続時に実行するコールバック関数設定
  pub_client.on_disconnect = on_disconnect                             # 切断時のコールバックを登録
  pub_client.on_publish = on_publish                                   # メッセージ送信時のコールバック
  print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
  print('@"mqttServer":' + mqttServer)
  print('@"portNum":' + str(portNum))
  print('@"MQTT_KEEP_ALIVE":' + str(MQTT_KEEP_ALIVE))
  pub_client.connect(mqttServer, portNum, MQTT_KEEP_ALIVE)             # MQTT broker接続
  pub_client.loop_start()                                              # 処理開始
  pub_client.publish(topicContent, payloadContent, qosNum, retainBool) # 送信
  sleep(3)
  pub_client.loop_stop()
  print('#"Pub-connection has been closed..."')


