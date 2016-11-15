## MIME协议

**MIME(Multipurpose Internet Mail Extensions,多用途Internet邮件扩展)**。MIME被用在电子邮件系统中，也
应用在Http当中

**消息头**

|头域                   | 说明                 |
|-----------------------|----------------------|
|MIME-Version           |MIME版本，1.0         |
|Content-Description    |消息内容描述          |
|Content-Id             |唯一标识              |
|Content-Transfer-Encoding|为了传输，如何包装消息体，如B/Q编码，7bit/8bit,base64等|
|Content-Type           | 内容的类型和格式，分主次类型|
|Content-Disposition    |内容的位置，可以是内嵌的或附件|

**MIME Content-Type**:
主要包含消息体的类型和子类型
常见的类型/子类型：

|类型                     |说明                                     |
|-------------------------|-----------------------------------------|
|Text/Plain               |未格式化的文本                           |
|Text/html                |Web页面                                  |
|Text/xml                 |XML内容                                  |
|Application/octet-stream |二进制数据                               |
|Message/RFC822           |MIME RFC822消息                          |
|Multipart/Mixed          |按特定顺序的独立部分                     |
|Multipart/alternative    |可选的。如同时提供文本/Html格式的消息    |
|Multipart/relater        |相关的，多个相关部分组成一个消息整体     |

## Http请求和响应
**Http**请求由三部分组成：
- **请求行**
- **消息报头**
- **请求正文**

**请求行（格式）：**Method Request-URI HTTP-Version CRLF
  - Method:
    GET   :请求获取由Request-URI所标识的资源
    POST  :在Request-URI所标识的资源后面附加新的数据
    HEAD  :请求获取由Request-URI所标识的资源的响应消息报头
    PUT   :请求服务器存储一个资源，并用Request-URI作为其标识
    DELETE:请求服务器删除由Request-URI所标识的资源
    TRACE :请求服务器会送收到的请求信息，主要用于测试和诊断
    CONNECT：保留字
    OPTIONS:请求查询服务器的性能，或查询与资源相关的选项和需求
  - Requst-URI: 统一资源标识符
  - Http-Versio：Http的版本
  - CRLF：回车换行

**Http响应**也是由三个部分组成：
- 状态行
- 消息报头
- 响应正文

**状态行**
状态行由协议版本、数字形式的状态代码、及相应的状态描述组成，各元素之间以空格分隔：
eg：`HTTP/1.1 200 OK \r\n ` 
**消息报头**消息报头有4种：
- 普通报头
- 请求报头
- 响应报头
- 消息报头

MIME类型就是服务器再把输出结果传送到浏览器上的时候，浏览器必须启动适当的应用程序来处理这个输出文档。
这可以通过多种类型MIME(多功能网际邮件协议)来完成。在Http中，MIME类型被定义在Content-Type header当中
。最早的Http协议当中，并没有附加的数据类型信息，所有传送的数据都被客户程序解释为超文本标记语言HTML文
档，*为了支持多媒体数据类型，HTTP协议中就使用了附加在文档之前的MIME数据类型信息来标识数据类型*。
MIME设计最初的目的是为了在发电子邮件时附加多媒体数据，让邮件客户程序能够根据其类型进行处理。然而当它
被Http协议支持以后，它的意义就更为显著了。使得Http传输的不仅是普通的文本，可以传送更多的数据。
每个MIME类型由两部分组成，前面是数据的大类别，例如声音audio、image后面是具体类型。
常见的MIME类型

|类型              |文件后缀    |       MIME类型          |
|------------------|------------|-------------------------|
|超文本标记语言    |.html       |text/html                |
|普通文本          |.txt        |text/plain               |
|RTF文本           |.rtf        |application/rtf          |
|GIF图形           |.gif        |image/gif                |
|JPEG图形          |.jpeg,.jpg  |image/jpeg               |
|au声音文件        |.au         |audio/basic              |
|MIDI声音文件      |.mid,.midi  |audio/midi,audio/x-midi  |
|RealAudio音乐文件 |.ra,.ram    |audio/x-pn-realaudio     |
|MPEGE文件         |.mpg,.mpeg  |video/mpeg               |
|AVI文件           |.avi        |video/x-msvideo          |
|GZIP文件          |.gz         |application/x-zip        |
|TAR文件           |.tar        |application/x-tar        |
|二进制数据        |            |application/octet-stream |

类型中以x为开头的方法标识这个类别还没有成为标准，只要客户机和服务器共同承认这个MIME类型，客户程序就
能根据MIME类型，采用具体的处理手段来处理数据。Web服务器和浏览器中,*缺省都设置了标准的和常见的MIME类
型,对于不常见的MIME类型，需要同时设置服务器和客户端浏览器，以进行识别.*
由于MIME类型与文档的后缀相关，因此服务器使用文档的后缀来区分不同的MIME类型，服务器中必须定义文档后缀
和MIME类型之间的对应关系。客户程序接受数据时，**只从服务器上接受数据流，并不了解文档的名字**，因此服
务器必须使用附加信息来告诉客户数据的MIME类型。服务器在发送真正的数据之前，就要先发送标志数据的MIME类
型的信息，这个信息使用Content-Type关键字进行定义。

