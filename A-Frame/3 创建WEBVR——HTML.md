## 利用HTML创建 WEB VR
使用A-Frame 框架中基本的HTML元素创建VR场景。
#### 添加一个BOX

      <a-scene>
        <a-box color="#6173F4" width="4" height="10" depth="2"></a-box>
      </a-scene>
就像使用普通的html元素一样，可以利用HTML元素的属性来配置元素。
平面的显示，默认使用左键按住拖拽的鼠标的方式来移动场景，利用WASD键来移动。
VR模式下，默认是通过虚拟头盔的转动来移动场景,如果空间足够大，可以自由的走动
###### 移动BOX
A-Frame 使用的是右手坐标系
* 右方是坐标系中X轴的正轴方向
* 上方是坐标系中Y轴的Y正轴方向
* 屏幕朝向我们的方向是Z轴正方向
系统中最基本的距离单位是米。为VR设计场景时，考虑物体在现实世界中的缩放是非常重要的，屏幕中将一个Box
的高度设置为100可能看起来非常普通，但是放到VR BOX中就可能显得一团糟。
系统中最基本的旋转单位是度。旋转正方向的确定依靠右手定则。将右手拇指沿着轴的正方向，其余手指卷曲的方
向就是正方向。可直接在组件使用position、rotation、和scale属性

    <a-scene>
        <a-box color="#6173F4" width="4" height="10" depth="2"
                position="-10 2 -5" rotation="0 0 45" scale="2 0.5 3"></a-box>
    </a-scene>   

###### 给BOX设置贴图
可以利用BOX的src属性将图像或者视频设置为BOX的贴图。为了保证颜色与视频不会混肴，将背景颜色修改为全白
。

    <a-scene>
        <a-box color="#6173F4" width="4" height="10" depth="2"
                position="-10 2 -5" rotation="0 0 45" scale="2 0.5 3"
                src="texture.png"></a-box>
    </a-scene>   
最好将贴图缓存下来，直到贴图下载下来再渲染贴图。
贴图缓存需要使用资源管理系统(asset management system),使用步骤：
  * 利用img 标签定义资源
  * 为资源添加一个ID
  * 利用ID选择器将资源赋给物体

    <a-scene>
        <a-assets>
          <img id="texture" src="texture.jpg" >
        </a-assets>
        <a-box color="#FFF" width="4" height="10" depth="2"
                position="-10 2 -5" rotation="0 0 45" scale="2 0.5 3"
                src="#texture"></a-box>
    </a-scene>
###### 为BOX设置动画
可以使用内建的animation system为BOX添加动画。可以将\<a-animation\>元素作为一个插入值设置成entity的子
元素，让BOX无限旋转为例。


    <a-scene>
        <a-assets>
          <img id="texture" src="texture.jpg" >
        </a-assets>
        <a-box color="#FFF" width="4" height="10" depth="2"
                position="-10 2 -5" rotation="0 0 45" scale="2 0.5 3"
                src="#texture">
            <a-animation attribute="rotation" repeat="indefinite" to="0 360 0"></a-animation>
        </a-box>
    </a-scene>
###### 与BOX交互
  让BOX可以支持点击或者聚焦的方式进行交互，可以利用Camera元素的子元素Cursor，使其固定在屏幕上。没有
  定义Camera元素时，scene 会自动插入一个默认的camera。为了使用cursor，必须先插入一个camera。
  接下来，利用animation的begin属性，让box当被光标点击时，开始播放动画，光标会触发box上的click事件，
  animation会监听该事件。

    <a-scene>
        <a-assets>
          <img id="texture" src="texture.jpg" >
        </a-assets>
        <a-box color="#FFF" width="4" height="10" depth="2"
                position="-10 2 -5" rotation="0 0 45" scale="2 0.5 3"
                src="#texture">
            <a-animation attribute="rotation" begin="click" repeat="indefinite" to="0 360 0"></a-animation>
        </a-box>
        <a-camera position="0 1.8 0">
            <a-cursor color="#2E3A87"></a-cursor>
        </a-camera>
    </a-scene>
还有另一种实现方式，一种更高级的方法就是写一个能够监听某个事件的组件，可以利用该组件实现任何方法。将
写完的组件直接给box即可。(AFRAME是写在JS的脚本声明中的，即\<script language="javascript" type="text/javascript"\>\<\/script\>)
      
      AFRAME.registerComponent('scale-on-click',{
          schema:{
            to:{default:'2 2 2'}
          },
          init:function(){
            var data = this.data;
            this.el.addEventListener('click',function(){
                  this.setAttribute('scale',data.to);
                });
          }
          });
        <a-box color="#FFF" width="4" height="10" depth="2"
                position="-10 2 -5" rotation="0 0 45" scale="2 0.5 3"
                src="#texture" scale-on-click="to:3 3 3">
            <a-animation attribute="rotation" begin="click" repeat="indefinite" to="0 360 0"></a-animation>
        </a-box>

###### BOX的光照
可以利用\<a-light\>组件来改变场景的光照，默认情况下，场景中是会自动添加环境光及平行光的。一旦添加了
自己的光源，默认的灯光便会被移除。
      
      <a-scene>
        <a-assets>
          <img id="texture" src="texture.jpg" >
        </a-assets>
        <a-box color="#FFF" width="4" height="10" depth="2"
                position="-10 2 -5" rotation="0 0 45" scale="2 0.5 3"
                src="#texture">
            <a-animation attribute="rotation" begin="click" repeat="indefinite" to="0 360 0"></a-animation>
        </a-box>
        <a-light type="spot" color="#333" position="-20 0 0 " look-at="a-box"></a-light>
        <a-light type="point" color="#AAA" position="0 5 0"></a-light>
        <a-camera position="0 1.8 0">
            <a-cursor color="#2E3A87"></a-cursor>
        </a-camera>
    </a-scene>
###### 为场景添加背景
  使用\<a-sky\>组件为场景添加背景，背景可以是颜色、全景图甚至是全景视频
  
       <a-scene>
        <a-assets>
          <img id="texture" src="texture.jpg" >
        </a-assets>
        <a-box color="#FFF" width="4" height="10" depth="2"
                position="-10 2 -5" rotation="0 0 45" scale="2 0.5 3"
                src="#texture">
            <a-animation attribute="rotation" begin="click" repeat="indefinite" to="0 360 0"></a-animation>
            <a-event name="mouseenter" scale="4 1 6"></a-event>
        </a-box>
        <a-light type="spot" color="#333" position="-20 0 0 " look-at="a-box"></a-light>
        <a-light type="point" color="#AAA" position="0 5 0"></a-light>
        <a-sky color="#73F7DD"></a-sky>
        <a-camera position="0 1.8 0">
            <a-cursor color="#2E3A87"></a-cursor>
        </a-camera>
    </a-scene> 
