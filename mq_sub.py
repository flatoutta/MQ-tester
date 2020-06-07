#!usr/bin/env python
# -*- coding: utf-8 -*- 

import paho.mqtt.client as mqtt
from time import sleep
import datetime

dt_now = datetime.datetime.now()
date_now = dt_now.strftime('%Y-%m-%d %H:%M:%S')

MQTT_KEEP_ALIVE = 60

sub_client = mqtt.Client()                 # クラスのインスタンス(実体)の作成

subscribedMessage = '888'
# メイン
def main_sub(mqttServer, portNum, userName, passWord, targetTopicContent):
  global subscribedMessage
  sub_client.on_connect = on_connect              # 接続時に実行するコールバック関数設定
  sub_client.on_disconnect = on_disconnect        # 切断時のコールバックを登録
  sub_client.on_message = on_message
  subscribedMessage = str(sub_client.on_message)
  sub_client.connect(mqttServer, portNum, MQTT_KEEP_ALIVE)       # MQTT broker接続
  sub_client.subscribe(targetTopicContent)  # subするトピックを設定 
  sub_client.loop_start()                         # 処理開始
  # print('1' + subscribedMessage)
  return subscribedMessage

def stopSub():
  sub_client.loop_stop()
  print('#"Sub-connection has been closed..."')

# ブローカーに接続できたときの処理
def on_connect(sub_client, userdata, flag, rc, t_TopicContent):
  print("Connected with result code " + str(rc))
  return

# メッセージが届いたときの処理
def on_message(sub_client, userdata, msg):
  global subscribedMessage
  subscribedMessage = print("*************************************************** \n* Received message :[" + str(msg.payload) + "] \n* on topic :[" + msg.topic + "] \n* with QoS [" + str(msg.qos) + "]  \n* Retain :[" + str(msg.retain) + "]\n* Subscribed at :["+ date_now +"] \n")
  return subscribedMessage

# 切断時
def on_disconnect(sub_client, userdata, flag, rc):
  if rc != 0:
     print("Unexpected disconnection.")

