#!usr/bin/env python
# -*- coding: utf-8 -*- 

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbox
from mq_pub import main_pub
from mq_sub import main_sub, stopSub

subscribedMessage = '777'
if __name__ == '__main__':
#以下メインコンテンツ部分###############################################
    root = Tk()
    root.title('MQ-tester ver1.0.0')
    root.resizable(True, False)
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()
    
    label1 = ttk.Label(frame1, text='Publish Setting ', padding=(5,2))
    label1.grid(row=0,column=1,sticky=W)
    
    label2 = ttk.Label(frame1, text='MQTT Server', padding=(5,2))
    label2.grid(row=1,column=0,sticky=E)
    
    label3 = ttk.Label(frame1, text='Port', padding=(5,2))
    label3.grid(row=2,column=0,sticky=E)
    
    label4 = ttk.Label(frame1, text='Username', padding=(5,2))
    label4.grid(row=3,column=0,sticky=E)
    
    label5 = ttk.Label(frame1, text='Password', padding=(5,2))
    label5.grid(row=4,column=0,sticky=E)
    
    label6 = ttk.Label(frame1, text='Topic', padding=(5,2))
    label6.grid(row=5,column=0,sticky=E)
    
    label7 = ttk.Label(frame1, text='Payload', padding=(5,2))
    label7.grid(row=6,column=0,sticky=E)
    
    label8 = ttk.Label(frame1, text='QoS', padding=(5,2))
    label8.grid(row=7,column=0,sticky=E)
    
    label9 = ttk.Label(frame1, text='Retain', padding=(5,2))
    label9.grid(row=8,column=0,sticky=E)
    
####################################################################
# 以下入力部分
    # MQTT_Server_entry
    mqtt_server = StringVar()
    mqtt_server.set('localhost')
    mqtt_server_entry = ttk.Entry(
        frame1,
        textvariable=mqtt_server,
        width=50 )
    mqtt_server_entry.grid(row=1,column=1,sticky=W)
    
    # Port Entry
    port = IntVar()
    port.set(1883)
    port_entry = ttk.Entry(
        frame1,
        textvariable=port,
        width=50 )
    port_entry.grid(row=2,column=1,sticky=W)
    
    # Username Entry
    username = StringVar()
    username_entry = ttk.Entry(
        frame1,
        textvariable=username,
        width=50 )
    username_entry.grid(row=3,column=1,sticky=W)
    
    # Password Entry
    password = StringVar()
    password_entry = ttk.Entry(
        frame1,
        textvariable=password,
        width=50,
        show='*' )
    password_entry.grid(row=4,column=1,sticky=W)

    # Topic Entry
    topic = StringVar()
    topic.set('topic')
    topic_entry = ttk.Entry(
        frame1,
        textvariable=topic,
        width=100 )
    topic_entry.grid(row=5,column=1,sticky=W)
    
    # Payload Entry
    payload = StringVar()
    payload.set('payload')
    payload_entry = ttk.Entry(
        frame1,
        textvariable=payload,
        width=100 )
    payload_entry.grid(row=6,column=1,sticky=W)

    # QoS Entry
    qosList = [0,0,1,2] 
    qos = IntVar()
    qos.set(qosList[0])
    qos_entry = ttk.Entry(
        frame1,
        textvariable=qos,
        width=50 )
    qos_entry = ttk.OptionMenu(frame1, qos, *qosList)
    qos_entry.config(width=5)
    qos_entry.grid(row=7,column=1,sticky=W)

    # Retain Entry
    retainList = ["False","False","True"] 
    retain = BooleanVar()
    retain.set(retainList[0])
    retain_entry = ttk.Entry(
        frame1,
        textvariable=retain,
        width=50 )
    retain_entry = ttk.OptionMenu(frame1, retain, *retainList)
    retain_entry.config(width=5)
    retain_entry.grid(row=8,column=1,sticky=W)


#############################################
#　以下ボタン行

    frame2 = ttk.Frame(frame1, padding=(0,5))
    frame2.grid(row=9,column=1,sticky=W)

        # Go!!ボタンを押した時 --- (*3)
    
        # mbox.showinfo(print(mqttServer,port,username,password,topic,payload,qos,retain))

    def button1_click():
        # テキストボックスの内容を得る
        topicContent = topic.get()
        payloadContent = payload.get()
        qosNum = qos.get()
        retainBool = retain.get()
        mqttServer = mqtt_server.get()
        portNum = port.get()
        userName = username.get()
        passWord = password.get()

        if mqttServer and portNum and topicContent and payloadContent:
            main_pub(mqttServer, portNum, userName, passWord, topicContent, payloadContent, qosNum, retainBool)

    def button2_click():
        # サブスクライブ開始
        userName = username.get()
        passWord = password.get()
        mqttServer = mqtt_server.get()
        portNum = port.get()
        targetTopicContent = targetTopic.get()
        if mqttServer and portNum and targetTopicContent:
            subscribedMessage = str(main_sub(mqttServer, portNum, userName, passWord, targetTopicContent))
            # print('3' + subscribedMessage)
            # subMessageBox.insert(END, subscribedMessage)

    def button3_click():
        # サブスクライブ処理を初期化
        stopSub()

    button1 = ttk.Button(frame2, text='Pub!!!!!!!', command=button1_click)
    button1.pack(side=LEFT)

    button2 = ttk.Button(frame2, text='Sub!!!!!!!', command=button2_click)
    button2.pack(side=LEFT)
  
    button3 = ttk.Button(frame2, text='Sub-Stop',command=button3_click)
    button3.pack(side=LEFT)


#################################################
# 以下Sub部分
#ToDo sub機能の実装

    label10 = ttk.Label(frame1, text='Subscribe Setting', padding=(5,2))
    label10.grid(row=10,column=1,sticky=W)

    label11 = ttk.Label(frame1, text='Target-Topic', padding=(5,2))
    label11.grid(row=11,column=0,sticky=E)

    # label12 = ttk.Label(frame1, text='Sub-Message', padding=(5,2))
    # label12.grid(row=12,column=0,sticky=E)

    # サブスクライブトピック設定入力
    targetTopic = StringVar()
    targetTopic.set('target_topic')
    targetTopic_entry = ttk.Entry(
        frame1,
        textvariable=targetTopic,
        width=100 )
    targetTopic_entry.grid(row=11,column=1,sticky=W)

    # サブスクライブしたメッセージの表示
    # sub_M_tuple = []
    # M_list = StringVar(value=sub_M_tuple)
    # subMessageBox = Listbox(frame1, listvariable=M_list, width=100, height=20)
    # subMessageBox.grid(row=12,column=1,sticky=W)
    
    root.mainloop()