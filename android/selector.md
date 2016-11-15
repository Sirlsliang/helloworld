## Android 中的selector

本文主要摘抄自[Android 中的Selector 的用法](http://blog.csdn.net/shakespeare001/article/details/7788400)
>Android中的selector主要是用来改变ListView 和 Button控件的默认背景。是在drawable/xxx.xml中配置的。

在drawable 文件夹中新建一个xx.xml文件，其内部代码结构为：

     <?xml version="1.0" encoding="utf-8" ?>
     <selector xmlns:android="http://schemas.android.com/apk/res/android">
     </selector>
下面就可以根据需求定义想要的样式,其主要属性为：

     <?xml version="1.0" encoding="utf-8" ?>
     <selector xmlns:android="http://schemas.android.com/apk/res/android">
        <!-- 默认的背景图片 -->
        <item android:drawable="@drawable/pic1" />

        <!-- 没有焦点时的背景图片 -->
        <item android:drawable="@drwable/pic1" 
              android:state_window_focused="false"/>

        <!-- 非触摸模式下获得焦点并单击时的背景图片 -->
        <item android:drawable="@drwable/pic2" 
              android:state_focused="true"
              android:state_pressed="true"/>

        <!-- 触摸模式下单击时的背景图片 -->
        <item android:drawable="@drwable/pic3" 
              android:state_focused="false"
              android:state_pressed="true"/>

        <!-- 选中时的背景图片 -->
        <item android:drawable="@drwable/pic4" 
              android:state_selected="true"/>

        <!-- 获得焦点时的背景图片 -->
        <item android:drawable="@drwable/pic5" 
              android:state_focused="true"/>
      </selector>

      android:state_pressed:布尔值，如果要求这个项目在对象被按下时使用，那么就设置为true(比如按钮被
          触摸或点击时，)false用于默认的非按下状态。
      android:state_focused:布尔值，如果该项目是在对象获取焦点时使用，那么使用true(比如，选项标签被
          打开时)
      android:state_checkable:布尔值，如果该项目是要用于对象的可选择状态，那么就要设置为true，如果这
      个项目要用于不可选状态，那么就要设置为false(用于对象在可选和不可选之间转换)
      android:state_checked:布尔值，如果这个项目用于对象被勾选的时候
      android:state_enabled:布尔值，如果这个项目用于对象可用状态(接受触摸或点击事件的能力),那么就设
      置为true.

文件的引用：
  1. 在ListView中添加如下属性代码：
    
          android:listSelector="@drawable/xxx.xml"
  2. 在ListView的item界面中添加如下属性代码：
    
          android:background="@drawable/xxx.xml"
  3. 利用JAVA代码直接编写
    
          Drwable drawable = getResource().getDrawable(R.drawable.xxx);
          listView.setSelector(drawable);
    为防止列表拉黑的情况发生，需要在listView中添加以下属性代码:
          
          android:cacheColorHint="@android:color/transparent"

