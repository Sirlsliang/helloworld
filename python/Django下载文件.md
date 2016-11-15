Django中的文件下载
---------

> 文章主要参考了[Django 实现下载文件功能](http://www.jianshu.com/p/2ce715671340)

首先应该找到django文件的位置。
路径相关的操作：

  -  \_\_file\_\_是指当前文件的名称，这个会包括路径。
  - 利用os.path.abspath(\_\_file\_\_)属性获取当前文件的绝对路径
  - os.path.dirname(fileName) 获取当前文件的上一级路径
  - os.path.join(path1,[path2],[path2]...) 将多个路径组合后返回

字符串相关的操作
  - 直接利用“+”可以进行字符串的拼接操作
  - 查找字符串：
    1. str.find('str'): 查找字符里第一个出现的子串，从左到右查找，从下标0开始
    2. str.rfind('str'): 查找字符串里右边第一个出现的子串
    3. str.index('s') : 在字符串里查找子串第一次出现的位置，类似字符串的find()方法，不过比find方法好的是，
        查找不到子串，会抛出异常，而不是返回-1
    4. str.rindex('s'): 与index的特性类似，不过是从右边开始查找
  - str.join('seq'):利用seq分割符(可以为空)将str(可以为序列、字符串、元组、字典)所有的元素合并成一个新的字符串，返回合并后的字符串
  - "{0}".format(str) : 字符串的格式化输出

### 文件下载相关
   直接文件下载

    with open(file\_name) as f:#打开file\_\_name文件， 
      f.read()
    return HttpResponse(c)
  这种下载方式比较简单，先将文件全部读取到内存中再进行下载，不适合大文件的下载。

  HttpResponse对象允许将迭代器作为传入参数，利用迭代器对大小文件均可下载，Django中推荐使用
  StreamingHttpResponse对象取代Httpresponse对象

    def file_download(request):
      #do sth
      def file_iterator(file_name,chunk_size=512):
        with open(file_name) as f:
          while True:
            c = f.read(chunk_size)
            if c:
              yield c
            else:
              break
      response = StreamingHttpResponse(file_iterator("file"))
      return response
   直接利用文件流的方式，文件流会以乱码的形式显示到浏览器上，而非下载到硬盘上，因此需要为StreamingHttpResponse对象
           添加一些参数，以优化代码。
    为StreamingHttpResponse对象的Content-Type 和 Content-Dispositon字段赋值即可
    
             response['Content-type']='application/octet-stream'
             response['Content-Disposition']='attachment;filename="testFile"'

  完整代码：
    
    from django.http import StreamingHttpResponse

    def big\_file\_download(request):
      # do sth
      def file_download(request):
        #do sth
        def file_iterator(file_name,chunk_size=512):
          with open(file_name) as f:
            while True:
              c = f.read(chunk_size)
              if c:
                yield c
              else:
                break
        file_name = "sdfsfs.pdf"
        response = StreamingHttpResponse(file_iterator(file_name))
        response['Content-type']='application/octet-stream'
        response['Content-Disposition']='attachment;filename="{0}"'.format(file_name)
        return response

  ### Content-Type 和 Content-Disposition
  两个都是MIME协议里面的内容，具体看[MIME协议](Mime协议.md)

  **Content-Type**内容域类型，用来说明传输的内容的类型。**Content-Type**域由“主类型/子类型”构成，主
  类型，有text，image，audio，video，application，multiparty，message等，分别表示文本、图片、音频、
  视频、应用、分段、消息等。每个主类型都可能包含有多个子类型，如text类型包含plain、html、xml、css、
  等子类型。
  
  **Content-Disposition**是MIME(Multipurpose Internet Mail Extensions)协议的扩展,MIME协议是指示MIME
  用户代理如何显示附加的文件。服务端向客户端浏览器发送文件时，如果是浏览器支持的文件类型，一般会默认
  使用浏览器打开，比如txt、jpg等，会直接在浏览器中显示，如果需要提示用户保存，就要利用
  **Content-Disposition**进行一下处理，关键在于一定要加上attachment：

      Response.AppendHeader("Content-Disposition","attachment;filename=FileName.txt");

  这样浏览器会提示保存还是打开，即使选择打开，也会使用相关联的程序比如记事本打开，而不是直接利用浏览
  器打开了。
  **Content-Disposition**就是当用户想把请求所得的内容存为一个文件的时候提供一个默认的文件名。当在响
  应类型为application/octet-stream情况下使用了这个头信息的话，那就意味着不想直接显示内容，而是弹出一
  个“文件下载”的对话框。

  
