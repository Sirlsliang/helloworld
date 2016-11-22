## Docker
> Docker是一个开源的容器引擎，可以轻松的为任何应用创建一个轻量级的、可移植的、自给自足的容器。

### Docker应用场景
1. web应用的自动化打包和发布
2. 自动化测试和持续集成、发布
3. 在服务型环境中部署和调整数据库或其它后台应用
4. 从头编译或者扩展现有的OpenShit或Cloud Foundry平台来搭建自己的PaaS环境

### Docker工作流程
1. 将代码和依赖配置到容器中
  - 在Dockerfile中配置运行环境和要执行的代码
  - 如果应用程序需要依赖外部程序如Redis或MySQL，可在Composefile中引入它们
  - 利用Docker Machine 运行Docker 容器
2. 如果需要配置网络和存储
3. 将配置上传至仓库
4. 利用Swarm跨主机部署

### 命令翻译

- attach  : 附加到一个正在运行中的容器
- build   : 根据Dockerfile创建容器的镜像文件
- commit  : 根据修改后的容器创建一个镜像文件
- cp      : 在容器和主机之间拷贝文件,
- create  : 创建一个新的容器
- diff    : 查看容器的改变
- events  : 从服务器中获取实时的事件
- exec    : 在运行中的容器中执行命令
- export  : 将容器的文件系统导出为tar文件包
- history : 显示镜像文件的历史记录
- images  : 显示镜像文件
- import  : 从tar文件包中导入内容
- info    : 现实系统级别的信息
- inspect : 显示关于镜像文件、容器或task的低一级的信息
- kill    : 关闭正在运行的容器
- load    : 从一个tar文件中或标准输入中加载镜像
- login   : 登入docker 仓库
- logout  : 登出
- logs    : 获取容器的日志信息
- network : 管理docker的网络
- node    : 管理Docker Swarm 节点
- pause   : 暂停一个或多个容器中所有的进程
- port    : 显示或配置容器的端口映射
- ps      : 显示容器
- pull    : 从docker仓库中获取镜像
- push    : 将仓库中推送容器
- rename  : 重命名一个容器
- restart : 重新启动一个容器
- rm      : 移除一个或多个容器
- rmi     : 移除一个或多个镜像文件
- run     : 在新容器中运行一个命令
  - d     : 后台运行
  - it    : 交互式的前台运行
  - rm    : 利用该参数标记之后，container停止之后就会被自动删除
- save    : 将一个或多个镜像保存到tar文档中去
- serach  : 在docker 中心寻找Docker
- service : 管理Docker 服务
- start   : 启动一个或多个容器
- stats   : 显示容器资源的使用信息
- stop    : 停止正在运行的容器
- swarm   : 管理Docker Swarm
- tag     : 为仓库中的镜像添加标签
- top     : 显示容器中正在运行的进行
- unpause : 在一个或者多个容器中恢复所有线程
- update  : 更新一个或多个容器的配置
- version : 显示Docker 的版本信息
- volume  : 管理docker 的卷
- wait    : 阻塞直到容器停止，然后打印退出信息

### Dockerfile 的书写
Dockerfile描述了软件是如何成为镜像文件的，Dockerfile中描述了软件的运行环境以及软件需要运行的命令。
- Dockerfile的命令格式为：** INSTRUCTION arguments**(命令不区分大小写)

1. 创建一个名称为Dockerfile的文件

        FROM docker/whalesay:latest  # 指定基础的镜像文件
        RUN apt-get -y update && apt-get install -y forunes  #在镜像文件中执行命令
        # 执行命令的格式为:
        #   RUN <command>  或 RUN ["executable","param1","param2"……] (exec form) 
        # run 命令等价于 docker run image command docker commit container_id
        CMD /usr/games/fortune -a | cowsay  # 运行软件
        # 一个Dockerfile 里面只能有一个CMD，如果有多个，只有最后一个生效。
        # CMD ["executable","param1","param2"](exec form) 运行一个可执行文件并提
        供参数
        # CMD [param1","param2"] (as default parameters to ENTRYPOINT) 为ENTRYPOINT指定参数
        # CMD ["executable","param1","param2"](shell form) 以"/bin/sh -c"的方法执行命令
        # docker run 命令指定了参数就会把CMD里的参数覆盖

2. Dockerfile 中的其他命令
    - MAINTAINER ：指定维护者的姓名和联系方式
      MAINTAINER helllo hello@166.com
    - ENTRYPOINT : 设置容器在启动时执行命令
    有两种格式
      - ENTRYPOINT cmd param1 param2
      - ENTRYPOINT ["cmd","param1","param2"……] 
    eg：ENTRYPOINT ["echo","hello world"]
    - USER：指定运行用户
      eg: 指定memcached的用户
          ENTRYPOINT ["memecached","-u","daemon"]

      更好的方式:
          ENTRYPOINT["memcached"]
          USER daemon

    - EXPOSE : 设置一个端口在运行的镜像中暴露在外
      格式：EXPOSE <PORT>[<port>……]

          eg:
          # memcached 使用端口11211,可以把这个端口暴露在外，这样容器外就可以看到这个端口并与其通信
          FROM　ubuntu
          MAINTAINER lsl lsl@111.com
          RUN　echo "deb http://*********" > /etc/apt/sources.list
          RUN apt-get update
          RUN apt-get install -y memcached
          ENTRYPOINT ["memcached"]
          USER daemon
          EXPOSE 11211

    - ENV： 设置环境变量
      格式：ENV <key> <value>
      设置了之后，后续的RUN 命令都可使用

    - ADD 从SRC复制文件到container的dest路径
      格式：ADD <src> <dest>
      - src :是相对被构建的源目录的相对路径，可以是文件或目录的路径，也可以是一个远程的文件url
      - dest ：container 中的绝对路径

    - VOLUME  创建一个挂载点用于共享目录,可在container 之间利用该目录共享数据
      格式：VOLUME ["<mountpoint>"]

    - WORKDIR ： 设置当前工作路径
      相对目录则是相对前一个WORKDIR命令
      
          eg:
          WORKDIR /a WORKDIR b WORKDIR c WORKDIR c RUN pwd
          # 上面的代码是指在/a/b/c目录下执行pwd
#### Compose file
  Compose 是定义和运行多个docker容器的docker应用程序，使用compose时，利用compose file 配置应用程序
  的服务，
      





