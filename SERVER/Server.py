import socket
import threading, struct, json, os,rsa, pymysql

from Cryptodome.Cipher import AES

#打开数据库连接
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='admin', db='SecureFileTransfer', charset='utf8')
#使用cursor方法创建一个游标
cursor = db.cursor()
#查询数据库版本
cursor.execute("select version()")
data = cursor.fetchone()
print(" Database Version:%s" % data)

class server_ssl:
    def server_listen(self):
        # 监听端口
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as ssock:
            ssock.bind(('127.0.0.1', 6666))
            ssock.listen(5)
            while True:
                
                print("Lisening!!!")
                # 接收客户端连接
                connection, addr = ssock.accept()   # conn 是一个新的socket对象
                print('Connected by ', addr)
                #开启多线程,这里arg后面一定要跟逗号，否则报错
                thread = threading.Thread(target=self.conn_thread, args=(connection,))
                thread.start()
    def conn_thread(self,connection):
        while True:
            try:
                connection.settimeout(100)
                fileinfo_size = struct.calcsize('1024s')
                buf = connection.recv(fileinfo_size)
                if buf:  # 如果不加这个if，第一个文件传输完成后会自动走到下一句
                    header_json = str(struct.unpack('1024s', buf)[0], encoding='utf-8').strip('\00')
                    print(header_json)
                    header = json.loads(header_json)
                    Command = header['Command']
                    if Command == 'Login':
                        # 查询数据表数据
                        username = header['user']
                        password = header['password']
                        time = header['time']
                        sql = "select authority from ft_user where username = '%s' and password = '%s'"%(username,password)
                        cursor.execute(sql)
                        data1 = cursor.fetchone()
                        sql = "select attribute from ft_user where username = '%s' " % (
                            username)
                        cursor.execute(sql)
                        data2 = cursor.fetchone()
                        # print(data)
                        if data1:
                            # listResult = os.path.dirname(__file__)+'/result.txt'
                            # 定义文件头信息，包含文件名和文件大小
                            header = {
                                'Feedback': 'Login',
                                'stat': 'Success',
                                'user': username,
                                'authority': data1[0],
                                'permission':data2[0],
                            }
                            header_hex = bytes(json.dumps(header).encode('utf-8'))
                            fhead = struct.pack('128s', header_hex)
                            connection.send(fhead)

                            print('%s login successfully')

                            loginlog = '\n%s try to login at "%s" , Stat: Success ' % \
                                        (username, time)
                            with open(os.path.dirname(__file__)+'/Serverlog.txt', 'a', encoding='utf-8') as list:
                                list.write(loginlog)
                        else:
                            # listResult = os.path.dirname(__file__)+'/result.txt'
                            header = {
                                'Feedback': 'Login',
                                'stat': 'Fail',
                                'user': username,
                                'authority': data1[0]
                            }
                            header_hex = bytes(json.dumps(header).encode('utf-8'))
                            fhead = struct.pack('128s', header_hex)
                            connection.send(fhead)
                            loginlog = '\n%s try to login at "%s" , Stat: Fail ' % \
                                        (username, time)
                            with open(os.path.dirname(__file__)+'/Serverlog.txt', 'a', encoding='utf-8') as list:
                                list.write(loginlog)
                            #connection.close()
                    elif Command == 'Upload':
                        fileName = header['fileName']
                        fileSize = header['fileSize']
                        fileSize1 = header['fileSize1']
                        fileSize2 = header['fileSize2']
                        fileSize3 = header['fileSize3']
                        fileSize4 = header['fileSize4']
                        fileSize5 = header['fileSize5']
                        useAES=header['useAES']
                        time = header['time']
                        user = header['user']
                        filenewname = os.path.join(os.path.dirname(__file__)+f'/SeverCache/', fileName)
                        print('Upload: file new name is %s, filesize is %s' % (filenewname, fileSize))
                        
                        if useAES==1:
                            recvd_size = 0  # 定义接收了的文件大小
                            path1=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'file_encrypted')
                            file1 = open(path1, 'wb')
                            print('start receiving...')
                            while not recvd_size == fileSize1:
                                if fileSize1 - recvd_size > 1024:
                                    rdata = connection.recv(1024)
                                    recvd_size += len(rdata)
                                else:
                                    rdata = connection.recv(fileSize1 - recvd_size)
                                    recvd_size = fileSize1
                                file1.write(rdata)
                            file1.close()

                            recvd_size = 0  # 定义接收了的文件大小
                            path2=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'AES_key_encrypted')
                            file2 = open(path2, 'wb')
                            print('start receiving...')
                            while not recvd_size == fileSize2:
                                if fileSize2 - recvd_size > 1024:
                                    rdata = connection.recv(1024)
                                    recvd_size += len(rdata)
                                else:
                                    rdata = connection.recv(fileSize2 - recvd_size)
                                    recvd_size = fileSize2
                                file2.write(rdata)
                            file2.close()

                            recvd_size = 0  # 定义接收了的文件大小
                            path3=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'file_iv_encrypted')
                            file3 = open(path3, 'wb')
                            print('start receiving...')
                            while not recvd_size == fileSize3:
                                if fileSize3 - recvd_size > 1024:
                                    rdata = connection.recv(1024)
                                    recvd_size += len(rdata)
                                else:
                                    rdata = connection.recv(fileSize3 - recvd_size)
                                    recvd_size = fileSize3
                                file3.write(rdata)
                            file3.close()

                            recvd_size = 0  # 定义接收了的文件大小
                            path4=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'file_signature_encrypted')
                            file4 = open(path4, 'wb')
                            print('start receiving...')
                            while not recvd_size == fileSize4:
                                if fileSize4 - recvd_size > 1024:
                                    rdata = connection.recv(1024)
                                    recvd_size += len(rdata)
                                else:
                                    rdata = connection.recv(fileSize4 - recvd_size)
                                    recvd_size = fileSize4
                                file4.write(rdata)
                            file4.close()

                            recvd_size = 0  # 定义接收了的文件大小
                            path5=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'fill_number')
                            file5 = open(path5, 'wb')
                            print('start receiving...')
                            while not recvd_size == fileSize5:
                                if fileSize5 - recvd_size > 1024:
                                    rdata = connection.recv(1024)
                                    recvd_size += len(rdata)
                                else:
                                    rdata = connection.recv(fileSize5 - recvd_size)
                                    recvd_size = fileSize5
                                file5.write(rdata)
                            file5.close()

                            file_aes_key_encrypted=open(path2,'rb')
                            aes_key_encrypted=file_aes_key_encrypted.read()
                            file_iv_encrypted=open(path3,'rb')
                            iv_encrypted=file_iv_encrypted.read()

                            print("开始解密AES秘钥")
                            path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'Bob_private_key.pem')
                            aes_key=rsa_private_decrypt(aes_key_encrypted, path)
                            print("AES秘钥解密完成！")
                            print("开始解密AES初始化向量")
                            iv=rsa_private_decrypt(iv_encrypted,path)
                            print("AES初始化向量解密完成！")
                            file_encrypted=open(path1,'rb') 
                            file_encrypted_msg=file_encrypted.read()

                            file_fill_number=open(path5,'rb')
                            fill_number=file_fill_number.read()
                            print("开始对加密文件进行AES解密")
                            file_msg=aes_decrypt(file_encrypted_msg,aes_key,iv)
                            file_msg=file_msg[0:len(file_msg)-int(fill_number)]
                            print("加密文件AES解密完成！")
                            file_fill_number.close()
                            path=os.path.join(os.path.dirname(__file__)+f'/{username}/', fileName)
                            file_decrypted=open(path,'wb')
                            file_decrypted.write(file_msg)
                            md5_file_msg=md5_encrypt(file_msg)
                            file_decrypted.close()
                            file_encrypted.close()

                            file_signature_encrypted=open(path4,'rb')
                            signature_encrypted=file_signature_encrypted.read()
                            print("加密签名文件AES解密")
                            file_signature=aes_decrypt(signature_encrypted,aes_key,iv)
                            print("加密签名文件AES解密完成！")
                            file_signature_encrypted.close()
                            file_aes_key_encrypted.close()         # AES解密完成，关闭相关文件
                            file_iv_encrypted.close()

                            path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'Alice_public_key.pem')
                            print("开始签名文件RSA解密")
                            with open(path,'r') as f:
                                pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
                            rsa.verify(md5_file_msg.encode(), file_signature, pubkey)
                            print("MD5值校验成功！")
                            print("解密程序运行完毕，请提取解密文件，并删除此程序所在路径下导入及生成的文件，谢谢！")
                        else:
                            recvd_size = 0  # 定义接收了的文件大小
                            file = open(filenewname, 'wb')
                            print('start receiving...')
                            while not recvd_size == fileSize:
                                if fileSize - recvd_size > 1024:
                                    rdata = connection.recv(1024)
                                    recvd_size += len(rdata)
                                else:
                                    rdata = connection.recv(fileSize - recvd_size)
                                    recvd_size = fileSize
                                file.write(rdata)
                            file.close()
 
                        #在这里接受那些和加密有关的签名文件等
                        #解密和验签
                        #删除和接收到的和加密有关的签名文件等

                        print('receive done')

                        fileSize = float(fileSize)
                        if fileSize<1024.0:
                            fileSize = "%s bytes"%(int(fileSize))
                        elif fileSize/1024.0 <= 1024.0:
                            fileSize = "%.2f Kb"%(fileSize/1024.0)
                        elif fileSize/1024.0/1024.0 <= 1024.0:
                            fileSize = "%.2f Mb"%(fileSize/1024.0/1024.0)
                        else:
                            fileSize = "%.2f Gb"%(fileSize/1024.0/1024.0/1024.0)

                        # uploadmsg = '{"文件名": "%s", "上传者": "%s", "上传时间": "%s", "大小": "%s"}\n'%\
                        #             (fileName,user,time,fileSize)
                        # with open(os.path.dirname(__file__)+'/result.txt','a',encoding='utf-8') as list:
                        #     list.write(uploadmsg)

                        uploadlog = '\n%s upload a file "%s" at %s' % \
                                        (user, fileName, time)
                        with open(os.path.dirname(__file__)+'/Serverlog.txt', 'a', encoding='utf-8') as list:
                            list.write(uploadlog)
                        #connection.close()
                    elif Command == 'Register':
                        # 注册用户，默认为普通用户
                        '''
                        实现简介：若可以从数据库中查询到当前用户的信息则不进行注册，反之注册一个普通用户，且属性为public
                        '''
                        username = header['user']
                        password = header['password']
                        time = header['time']
                        sql = "select ID from ft_user where username = '%s'" % (username)
                        cursor.execute(sql)
                        data = cursor.fetchone()
                        if data:
                            # 定义文件头信息，包含文件名和文件大小
                            header = {
                                'Feedback': 'Register',
                                'stat': 'Exist',
                                'fileSize': '',
                                'user': username
                            }
                            header_hex = bytes(json.dumps(header).encode('utf-8'))
                            fhead = struct.pack('128s', header_hex)
                            connection.send(fhead)
                            loginlog = '\n%s try to register at "%s" , Stat: Fail ' % \
                                       (username, time)
                            with open(os.path.dirname(__file__)+'/Serverlog.txt', 'a', encoding='utf-8') as list:
                                list.write(loginlog)
                        else:
                            try:
                                path = os.getcwd()
                                create_dir = os.path.join(path, username)
                                os.makedirs(create_dir , exist_ok=True)
                                path_created = path+"\\"+username
                                if os.path.exists(path_created):
                                    print("Having created a folder for user: ", username)
                                else:
                                    ex = Exception('Failed created folder for user:'+username)
                            except Exception as re:
                                print(re)
                            
                            sql = "insert into ft_user (username, password) values ('%s','%s')" % (username,password)
                            # sql = "insert into user_ft (username, password) values ('%s','%s')" % (username,password)
                            cursor.execute(sql)
                            db.commit()
                            # 定义文件头信息，包含文件名和文件大小
                            header = {
                                'Feedback': 'Register',
                                'stat': 'Success',
                                'fileSize': '',
                                'user': username
                            }
                            header_hex = bytes(json.dumps(header).encode('utf-8'))
                            fhead = struct.pack('128s', header_hex)
                            connection.send(fhead)
                            loginlog = '\n%s try to register at "%s" , Stat: Success ' % \
                                       (username, time)
                            with open(os.path.dirname(__file__)+'/Serverlog.txt', 'a', encoding='utf-8') as list:
                                list.write(loginlog)

                    elif Command == 'Check' :
                        # 查看当前所有可见用户文件
                        '''
                        实现简介：  如果是管理员用户则可以查看所有用户，如果是普通用户则只能查询自己的文件以及属性为public的用户。
                        '''
                        username = header['user']
                        password = header['password']
                        time = header['time']
                        sql = "select authority from ft_user where username = '%s' and password = '%s'"%(username,password)
                        cursor.execute(sql)
                        data = cursor.fetchone()
                        print(data[0])
                        if data:
                            if data[0] == 'admin':
                                sql = 'select username from ft_user'
                            else:
                                sql = "select username from ft_user where attribute = 'public'"
                            cursor.execute(sql)
                            user_list = cursor.fetchall()
                            userList = []
                            # 将所有的用户存入user_list
                            for dat in user_list:
                                print(dat)
                                userList.append(dat)
                            # 将便利所有用户的文件夹，将其文件存入数据结构
                            path = os.getcwd()

                            for i in range(len(user_list)):
                                fileSize = []
                                pathh = path+'\\'+ user_list[i][0]
                                if os.path.exists(pathh):
                                    file_list = os.listdir(pathh)
                                    print(pathh)
                                    print(file_list)
                                    if file_list:
                                        for i_file in file_list:
                                            path_file = os.path.join(pathh, i_file)
                                            fileSize.append(os.stat(path_file).st_size) 
                                    else:
                                        file_list = ''
                                    print(len(userList))
                                    sql = "select attribute from ft_user where username = '%s' " % (
                                        user_list[i][0])
                                    cursor.execute(sql)
                                    data = cursor.fetchone()
                                    # print(data)
                                    userList[i] = {
                                        'usrName' : user_list[i][0],
                                        'permission':data[0],
                                        'fileName' : file_list,
                                        'fileSize' : fileSize

                                    }
                                    print(userList)
                                else:
                                    print("No Folder!")



                            header = {
                                'Command': 'Check',
                                'checkList' : userList,
                                'stat' : 'Success',
                                'username': username,
                            }
                            header_hex = bytes(json.dumps(header).encode('utf-8'))
                            fhead = struct.pack('1024s', header_hex)
                            print(fhead)
                            connection.send(fhead)


                            print('%s check successfully')

                            loginlog = '\n%s try to check at "%s" , Stat: Success ' % \
                                        (username, time)
                            with open(os.path.dirname(__file__)+'/Serverlog.txt', 'a', encoding='utf-8') as list:
                                list.write(loginlog)
                        else:
                            print("NO PERMISSION")
                            header = {
                                'Command': 'Check',
                                'checkList' : '',
                                'stat' : 'Fail',
                                'user': username,
                            }
                            header_hex = bytes(json.dumps(header).encode('utf-8'))
                            fhead = struct.pack('1024s', header_hex)
                            connection.send(fhead)

                            fo = open(listResult, 'rb')
                            while True:
                                filedata = fo.read(1024)
                                if not filedata:
                                    break
                                connection.send(filedata)
                            fo.close()
                    
                    elif Command == 'Change':
                        # 改变当前属性
                        username = header['user']
                        password = header['password']
                        time = header['time']
                        sql = "select attribute from ft_user where username = '%s' and password = '%s'"%(username,password)
                        cursor.execute(sql)
                        data = cursor.fetchone()
                        print(data)
                        if data[0]=='public':
                            beforeAtt = 'public'
                            afterAtt = 'private'
                            sql = "update ft_user SET attribute='private' where username='%s'"%(username)
                        else:
                            beforeAtt = 'private'
                            afterAtt = 'public'
                            sql = "update ft_user SET attribute='public' where username='%s'"%(username)
                        cursor.execute(sql)
                        db.commit()
                        sql = "select attribute from ft_user where username='%s'" % (username)
                        cursor.execute(sql)
                        data = cursor.fetchone()
                        if data[0] == afterAtt:
                            print("Successful changing")
                            header = {
                                'Command': 'Change',
                                'stat' : 'Success',
                                'username': username,
                                'afterAtt':afterAtt,
                                'beforeAtt':beforeAtt
                            }
                            header_hex = bytes(json.dumps(header).encode('utf-8'))
                            fhead = struct.pack('128s', header_hex)
                            connection.send(fhead)

                            print('%s change successfully')

                            loginlog = '\n%s try to change at "%s" , Stat: Success ' % \
                                        (username, time)
                            with open(os.path.dirname(__file__)+'/Serverlog.txt', 'a', encoding='utf-8') as list:
                                list.write(loginlog)
                        else:
                            print('%s change failing')
                            loginlog = '\n%s try to change at "%s" , Stat: Fail ' % \
                                        (username, time)
                            with open(os.path.dirname(__file__)+'/Serverlog.txt', 'a', encoding='utf-8') as list:
                                list.write(loginlog)
                    
                    elif Command == 'Download':
                            # 查询数据表数据
                        # username = header['user']
                        # password = header['password']
                        username = header['fileowner']   # fileowner
                        time = header['time']
                        # sql = "select * from ft_user where username = '%s' and password = '%s'" % (username, password)
                        # cursor.execute(sql)
                        # data = cursor.fetchone()
                        filename = header['fileName']

                        #接收到来自客户端的下载请求后要将这个文件进行AES加密和RSA签名生成一堆签名信息加密的文件
                        filepath = os.path.join(os.path.dirname(__file__)+f'/{username}/', filename)
                        file=open(filepath,'rb')
                        file_msg=file.read()
                        aes_key_path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'AES_key')
                        file_aes_key=open(aes_key_path,'rb')   # 打开AES秘钥文件
                        aes_key=file_aes_key.read()
                        from Cryptodome.Cipher import AES
                        from Cryptodome import Random
                        # iv用来记录AES随机生成的一个16字节初始向量
                        iv = Random.new().read(AES.block_size)   # 使用Cryptodome中Random模块,读取16字节数据作为iv的值，AES分块大小固定为16字节
                        print("开始对原文件进行AES加密......")
                        file_encrypted_msg,fill_number=aes_encrypt(file_msg,aes_key,iv)
                        path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'file_encrypted')
                        file_encrypted=open(path,'wb')
                        file_encrypted.write(file_encrypted_msg)
                        file_encrypted.close()
                        print("原文件AES加密完成！")
                        path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'fill_number')
                        file_fill_number=open(path,'w')
                        file_fill_number.write(str(fill_number))
                        file_fill_number.close()

                        print("开始对原文件进行MD5摘要")
                        md5_msg=md5_encrypt(file_msg)
                        print("MD5摘要完成！")
                        file.close()

                        print("开始对MD5摘要签名")
                        path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'Bob_private_key.pem')
                        signature_msg=rsa_private_encrypt(md5_msg,path)
                        print("MD5摘要签名完成！")
                        print("对签名进行AES加密")
                        signature_encrypted_msg,number=aes_encrypt(signature_msg,aes_key,iv) 
                        path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'file_signature_encrypted')
                        file_signature_encrypted=open(path,'wb')
                        file_signature_encrypted.write(signature_encrypted_msg)
                        file_signature_encrypted.close()
                        print("签名AES加密完成！")

                        print("开始对AES秘钥进行RSA加密")
                        path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'Alice_public_key.pem')
                        print("开始对AES秘钥进行RSA加密")
                        aes_key_encrypted=rsa_public_encrypt(aes_key,path)
                        path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'AES_key_encrypted')
                        file_aes_key_encrypted=open(path,'wb')
                        file_aes_key_encrypted.write(aes_key_encrypted)
                        file_aes_key_encrypted.close()
                        print("AES秘钥RSA加密完成！")
                        print("开始对iv进行RSA加密")
                        path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'Alice_public_key.pem')
                        iv_encrypted=rsa_public_encrypt(iv,path)
                        path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'file_iv_encrypted')
                        file_iv_encrypted=open(path,'wb')
                        file_iv_encrypted.write(iv_encrypted)
                        file_iv_encrypted.close()
                        print("对iv的RSA加密完成！")
                        file_aes_key.close()

                        print("加密过程结束！")
                        print("你需要发送给接收者的文件有：")
                        print("1.已加密文件：file_encrypted")
                        print("2.加密后的AES秘钥文件：AES_key_encrypted")
                        print("3.AES加密后的初始化向量文件：file_iv_encrypted")
                        print("4.加密后的签名文件：file_signature_encrypted")
                        print("5.填充位数文件：fill_number")
                        print("\n最后请删除程序所在路径下加入和生成的文件，谢谢！")

                        path1=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'file_encrypted')
                        path2=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'AES_key_encrypted')
                        path3=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'file_iv_encrypted')
                        path4=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'file_signature_encrypted')
                        path5=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'fill_number')


                        if data:

                            filepath = os.path.join(os.path.dirname(__file__)+f'/{username}/', filename)
                            # 定义文件头信息，包含文件名和文件大小
                            header = {
                                'Feedback': 'Download',
                                'stat': 'Success',
                                'fileSize': os.stat(filepath).st_size,
                                'fileSize1': os.stat(path1).st_size,
                                'fileSize2': os.stat(path2).st_size,
                                'fileSize3': os.stat(path3).st_size,
                                'fileSize4': os.stat(path4).st_size,
                                'fileSize5': os.stat(path5).st_size,
                                'user': username
                            }
                            header_hex = bytes(json.dumps(header).encode('utf-8'))
                            fhead = struct.pack('1024s', header_hex)
                            connection.send(fhead)

                            path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'file_encrypted')
                            f1=open(path,'rb')
                            while True:
                                filedata = f1.read(1024)
                                if not filedata:
                                    break
                                connection.send(filedata)
                            f1.close()
                            path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'AES_key_encrypted')
                            f2=open(path,'rb')
                            while True:
                                filedata = f2.read(1024)
                                if not filedata:
                                    break
                                connection.send(filedata)
                            f2.close()
                            path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'file_iv_encrypted')
                            f3=open(path,'rb')
                            while True:
                                filedata = f3.read(1024)
                                if not filedata:
                                    break
                                connection.send(filedata)
                            f3.close()
                            path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'file_signature_encrypted')
                            f4=open(path,'rb')
                            while True:
                                filedata = f4.read(1024)
                                if not filedata:
                                    break
                                connection.send(filedata)
                            f4.close()
                            path=os.path.join(os.path.dirname(__file__)+f'/SeverCache/', 'fill_number')
                            f5=open(path,'rb')
                            while True:
                                filedata = f5.read(1024)
                                if not filedata:
                                    break
                                connection.send(filedata)
                            f5.close()

                            #在这里将那些和加密文件有关的签名文件发送过去
                            #删除这些文件

                            print('send file over...')
                            downloadlog = '\n%s download a file "%s" at %s' % \
                                          (username, filename, time)
                            with open(os.path.dirname(__file__)+'/Serverlog.txt', 'a', encoding='utf-8') as list:
                                list.write(downloadlog)
                            # connection.close()
                        else:
                            header = {
                                'Feedback': 'Download',
                                'stat': 'LoginFail',
                                'fileSize': '',
                                'user': username
                            }
                            header_hex = bytes(json.dumps(header).encode('utf-8'))
                            fhead = struct.pack('128s', header_hex)
                            connection.send(fhead)
                    
                    elif Command == 'Audit':
                        username = header['user']
                        password = header['password']
                        time = header['time']
                        sql = "select authority from ft_user where username = '%s' and password = '%s'"%(username,password)
                        cursor.execute(sql)
                        data = cursor.fetchone()
                        if data[0] == 'admin':
                            listResult = os.path.dirname(__file__)+'/Serverlog.txt'
                            # 定义文件头信息，包含文件名和文件大小
                            header = {
                                'Feedback': 'Audit',
                                'stat': 'Success',
                                'fileSize': os.stat(listResult).st_size,
                                'user': username
                            }
                            header_hex = bytes(json.dumps(header).encode('utf-8'))
                            fhead = struct.pack('128s', header_hex)
                            connection.send(fhead)

                            fo = open(listResult, 'rb')
                            while True:
                                filedata = fo.read(1024)
                                if not filedata:
                                    break
                                connection.send(filedata)
                            fo.close()
                            # logResult = os.path.dirname(__file__)+'/Serverlog.txt'
                            # print(os.stat(logResult).st_size)
                            # 定义文件头信息，包含文件名和文件大小
                            # header = {
                            #     'Feedback': 'Audit',
                            #     'stat': 'Success',
                            #     'fileSize': os.stat(logResult).st_size,
                            #     'user': username
                            # }
                           

                            # auditlog = '\n%s try to audit at "%s" , Stat: Success ' % \
                            #             (username, time)
                            # with open(os.path.dirname(__file__)+'/Serverlog.txt', 'a', encoding='utf-8') as list:
                            #     list.write(auditlog)
                        else:
                            header = {
                                'Feedback': 'Login',
                                'stat': 'Fail',
                                'fileSize': '',
                                'user': username
                            }
                            header_hex = bytes(json.dumps(header).encode('utf-8'))
                            fhead = struct.pack('128s', header_hex)
                            connection.send(fhead)
                            print('%s audit Faid!')

                            auditlog = '\n%s try to audit at "%s" , Stat: Fail ' % \
                                        (username, time)
                            with open(os.path.dirname(__file__)+'/Serverlog.txt', 'a', encoding='utf-8') as list:
                                list.write(auditlog)
                        

            except socket.timeout:
                connection.close()
                break
            except ConnectionResetError:
                connection.close()
                break

def aes_encrypt(aes_file, key,iv):  # aes_file 文件，key 16-bytes 对称秘钥
    from Cryptodome.Cipher import AES
    from Cryptodome import Random
    cipher = AES.new(key, AES.MODE_OFB,iv)   # 生成了加密时需要的实际密码,这里采用OFB模式
    # if fs is a multiple of 16
    x = len(aes_file) % 16
    print("要加密文件的长度是： %d"%len(aes_file))
    print("需要填充的数据长度 : %d"%((16- x)%16))
    if x != 0:
        aes_file_pad = aes_file + b'0'*(16 - x) # It should be 16-x
    else:
        aes_file_pad=aes_file
    msg = cipher.encrypt(aes_file_pad)
    return msg,(16- x)%16                

def aes_decrypt(aes_file, key,iv):
    from Cryptodome.Cipher import AES
    cipher = AES.new(key, AES.MODE_OFB,iv)   # 生成了解密时需要的实际密码,这里采用OFB模式
    msg=cipher.decrypt(aes_file)
    return msg

# 计算MD5值
def md5_encrypt(md5_file):
    from Cryptodome.Hash import MD5
    msg = MD5.new()
    msg.update(md5_file)
    return msg.hexdigest()

# RSA私钥加密
def rsa_private_encrypt(msg,file_rsa_private_key_name):
    # from M2Cryptodome import RSA    # 用M2Cryptodome下的RSA模块
    # rsa_private_key=RSA.load_key(file_rsa_private_key_name)
    # msg_encrypted=rsa_private_key.private_encrypt(msg,RSA.pkcs1_padding)
    # return msg_encrypted
    with open (file_rsa_private_key_name,'r') as f:
        rsa_private_key=rsa.PrivateKey.load_pkcs1(f.read().encode())
    msg_encrypted=rsa.sign(msg.encode(), rsa_private_key, 'SHA-1')
    return msg_encrypted

# RSA公钥加密
def rsa_public_encrypt(msg,file_rsa_public_name):
    # from M2Cryptodome import RSA    # 用M2Cryptodome下的RSA模块
    # rsa_public_key=RSA.load_pub_key(file_rsa_public_name)
    # msg_encrypted=rsa_public_key.public_encrypt(msg,RSA.pkcs1_padding)
    # return msg_encrypted
    with open(file_rsa_public_name,'r') as f:
        rsa_public_key=rsa.PublicKey.load_pkcs1(f.read().encode())
    msg_encrypted=rsa.encrypt(msg, rsa_public_key)
    return msg_encrypted
#  RSA私钥解密
def rsa_private_decrypt(msg,file_rsa_private_key_name):
    # from M2Cryptodome import RSA    # 用M2Cryptodome下的RSA模块
    # rsa_private_key=RSA.load_key(file_rsa_private_key_name)
    # msg_decrypted=rsa_private_key.private_decrypt(msg,RSA.pkcs1_padding)
    # return msg_decrypted
    with open(file_rsa_private_key_name,'r') as f:
        rsa_private_key=rsa.PrivateKey.load_pkcs1(f.read().encode())
    msg_decrypted=rsa.decrypt(msg, rsa_private_key)
    return msg_decrypted

#  RSA公钥解密
def rsa_public_decrypt(msg,file_rsa_public_name):
    # from M2Cryptodome import RSA    # 用M2Cryptodome下的RSA模块
    # rsa_public_key=RSA.load_pub_key(file_rsa_public_name)
    # msg_decrypted=rsa_public_key.public_decrypt(msg,RSA.pkcs1_padding)
    # return msg_decrypted
    with open(file_rsa_public_name,'r') as f:
        rsa_public_key=rsa.PublicKey.load_pkcs1(f.read().encode())
    msg_decrypted=rsa.decrypt(msg, rsa_public_key)
    return msg_decrypted

if __name__ == "__main__":
    server = server_ssl()
    server.server_listen()
    
    