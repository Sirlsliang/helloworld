## 在Tomcat中配置Servlet
> 运行servlet需要servlet容器。
1. 找到Tomcat安装目录中conf目录下的server.xml文件
  - server  : Tomcat实例的顶层元素，代表整个容器。一个Server自身不是一个容器,可有多个service
  - service : 顶层类元素，可包含一个Engine，多个connector
  - connector :
  - engine
  - host ： 一个engine可以有多个host，每个host定义了一个虚拟主机，包含了一个或多个web应用。
2. 修改Host的appBase属性，将该属性指到web程序的目录中。
3. web程序目录结构。
  ROOT
    |-WEB-INF
        |- web.xml
        |- classes(目录，存放编译后的servlet)
    |- 
4. 修改web.xml文件，指定servlet 及 servlet-mapping 属性。
