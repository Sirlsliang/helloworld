## 利用组件创建VR 场景
利用entity-component-system 创建虚拟场景。本文主要介绍了3个方面
1. A-Frame框架中标准组件的使用
2. 在系统中添加第三方组件
3. 书写自定义的组件
将要创建的场景是一个全景图想集，在场景中有3个可以让用户点击的面板，点击之后，背景便会消失，取而代之
的是全景图。

#### 基本框架

    <a-scene>
      <a-assets>
        <audio id="click-sound" src="audio/click.ogg"></audio>
        <!-- images -->
        <img id="city" src="img/city.jpg">
        <img id="city-thumb" src="img/thumb-city.png">
        <img id="cubes" src="img/cubes.jpg">
        <img id="cubes-thumb" src="img/thumb-cubes.png">
        <img id="sechelt" src="img/sechelt.jpg">
        <img id="sechelt-thumb" src="img/thumb-sechelt.png">
      </a-assets>
      <!-- 全景图像 -->
      <a-sky id="image-360" radius="10" src="#city"></a-sky>
      <!-- 链接 -->
      <a-plane class="link" height="1" width="1"></a-plane>
      <!--摄像机与光标-->
      <a-camera>
        <a-cursor id="cursor">
          <a-animation begin="click" easing="ease-in" attribute="scale"
                        fill="backwards" from="0.1 0.1 0.1" to="1 1 1" dur="150">
          </a-animation>
          <a-animation begin="cursor-fusing" easing="ease-in" attribute="scale"
                        from="1 1 1" to="0.1 0.1 0.1" dur="150">
          </a-animation>
        </a-cursor>
      </a-camera>
    </a-scene>
在上面我们提前定义了一些元素：
* 在Asset Management System 中的\<a-assets\>标签中定义了几个图片
* 全景图放置在\<a-sky\>标签中
* 一个利用事件驱动动画系统实现的具有视觉反馈效果的光标,该光标固定在摄像机上面。

#### 使用标准组件
标准组件是A-Frame中的组件，就像标准库一样。在这里将会展示如何将component附加到entities当中，并利用
html对他们进行配置。
使用material component向\<a-plane\>链接中添加图像贴图。
material component 是一个多属性的component。为了向plane附加一个material component， 将组件的名称设置
成一个HTML属性。
  
    <a-plane class="link" height="1" width="1" material></a-plane>
然后利用inline CSS 的句法样式指定组件的属性。将**shader**设置为**flat**这样图像就不会受到光照的影响
(the image isn't affected negatively by lighting).将**src**设置为**#cubes-thumb**,在资源管理系统中提
前定义的图像缩略图。

    <a-plane class="link" height="1" width="1" 
            material="shader:flat;src:#cubes-thumb"></a-plane>
可以添加更多的组件，例如声音组件。希望当点击链接或者注视到链接上时播放声音。语法与先前的相同，但是现
在需要使用声音组件属性。将**on**属性设置为click，这样当点击时播放声音。将**src**属性设置为
**#click-sound**，前面在资源管理系统中声音资源的id
  
    <a-plane class="link" height="1" width="1" 
            material="shader:flat;src:#cubes-thumb"
            sound="on:click;src:#click-sound"></a-plane>
现在就是实现了一个可以点击就播放声音且具有贴图的面板了。

#### 使用第三方组件
可以在从 [ecosystem](https://github.com/aframevr/awesome-aframe#components)选择第三方组件，并将它们
整合进我们的场景中，并在HTML中使用。组件可以做任何事，通过使用他人的组件可以帮我们做很多事。
本文会大致浏览下使用该第三方组件：模板、布局和事件集合。[K-frame](https://github.com/ngokevin/kframe/)是由
A-Frame的主要贡献者Kevin Ngo创建的一个组件包，可以非常方便地将三种组件装入一个Bundle中。
下载k-frame.min.js并将其放入\<head\>标签当中\<A-Frame\>框架之后。
    
        <html>
          <head>
            <title>360度 Image Browsers</title>
            <script scr="lib/aframe.min.js"></script>
            <script scr="lib/k-frame.min.js"></script>
          </head>
          <body>
            <a-scene>
              <!----........-->
            </a-scene>
          </body>
        </html>
#### 模板组件
现在已经有一个连接，现在想创建3个链接，每个都链接到一个全景图像当中。
模板组件整将模板引擎整合进A-Frame当中。这可以帮助我们封装一组实体、利用数据生成实体、或者对其遍历。
如果我们不对HTML使用复制粘贴而想将已有的一个实体变为三个的话，那就要使用模板组件。
如果已经读过 [模板组件文档](https://github.com/ngokevin/aframe-template-component)的话，就会知道创建
一个模板是通过\<a-assets\>中的一个脚本标签。下面展示了链接到模板的链接并使用id给它一个名称。

        <a-assets>
        <!--...-->
        <script id="plane">
          <a-plane class="link" height="1" width="1"
            material ="shader:flat;src:#cubes-thumb"
            sound="on:click;src:#click-sound"></a-plane>
        </script>
        </a-assets>

然后我们就可以使用该模板创建多个plane而无需做更多的工作。

      <a-entity template="src:#plane"></a-entity>
      <a-entity template="src:#plane"></a-entity>
      <a-entity template="src:#plane"></a-entity>
这样的话所有的模板都会显示同一个图像贴图，看起来都一样。需要一个可以使用变量的模板系统使用

     <script type="text/nunjucks">
指定使用流行的 [Nunjucks](https://mozilla.github.io/nunjucks/)
模板引擎。组件对模板引擎的加载属于lazy-load。利用Nunjucks,可以在模板中定义一个变量，该变量可利用data
attributes 来向该变量传值。
  
      <a-assets>
      <script id="plane" type="text/nunjucks">
        <a-plane class="link" height="1" width="1"
            material="shader:flat;src:{{thumb}}"
            sound="on:click;src:#click-sound"></a-plane>
      </script>
      </a-assets>

      <a-entity template="src:#plane" data-thumb="#city-thumb"></a-entity>
      <a-entity template="src:#plane" data-thumb="#cubes-thumb"></a-entity>
      <a-entity template="src:#plane" data-thumb="#sechelt-thumb"></a-entity>

使用模板可以保持scene整洁，不需要多写代码

#### 布局组件
entity默认的默认位置是0 0 0，entity之间会相互覆盖。尽管我们可以手动为每个link设定位置，我们也可以利
用布局组件代替我们做这件事。布局组件会自动的将子元素放置在指定的布局位置。
需要创建一个实体将link包裹，然后将**line**布局附加给布局组件。

      <a-entity id="links" layout="type:line;margin:0.75" position="-3 -1 -4">
          <a-entity template="src: #plane" data-thunmb="#city-thumb"></a-entity>
          <a-entity template="src: #plane" data-thunmb="#cubes-thumb"></a-entity>
          <a-entity template="src: #plane" data-thunmb="#sechelt-thumb"></a-entity>
      </a-entity>
现在所有的link不再重叠在一块了，也不必不断地调整以寻找合适的位置了。
#### 事件集组件
最后，我们将要为我们的links添加一些视觉上的反馈。我们想让它们当光标覆盖或点击时会
放大或缩小。这涉及到制作一个事件监听器，相当于在scale component 上利用setAttributes响应光标事件。这时相当普遍的，因
此需要一个event-set component 来响应事件。
让我们在links上写一个事件监听函数，当他们被盯着时会放大，当点击时会缩小，不在被盯着时，就将
将它们置为原来的大小。我们模仿CCS的特性**：hover**状态。可以利用\_event属性指定事件的名称，属性剩下
的部分就是setAttribute方法调用的，注意event-set组件可以有多个实例。

    <a-assets>
      <script id="link" type="text/nunjucks">
        <a-plane class="link" height="1" width="1"
            material="shader:flat;src={{thumb}}"
            sound="on:click;src:#click-sound"
            <!-- 鼠标点击 -->
            event-set__1="_event:mousedown;scale:1 1 1"
            <!-- 鼠标抬起 -->
            event-set__2="_event:mousedup;scale:1.2 1.2 1"
            <!-- 鼠标进入 -->
            event-set__3="_event:mouseenter;scale:1.2 1.2 1"
            <!-- 鼠标离开 -->
            event-set__4="_event:mouseleave;scale:1 1 1"
       </script>
    </a-assets>
掌握了组件可以利用很少的HTML代码做很多事情，尽管社区中已经有很多提供者了，我们仍然需要在自己的场景中
制作属于自己的组件。

#### 组件的制作
[组件文档](https://aframe.io/docs/0.3.0/core/component.html)中已经有详细的关于制作组件的方法，最基本
的组件制作格式为

    AFRAME.registerComponent('component-name',{
        //定义组件属性
        schema:{},
        /**当组件被附加到实体上时被调用，
        * @member {element} el- 实体
        * @member data--- 组件的数据
        */
        init:function(){
          //使用this.el 和 this.data
        }
    });

#### 升级射线组件
首先，需要设置光标射线可以相交的实体白名单。这样设置了之后，光标只会点击可以被点击的物体，这样会提升
性能。光标在raycaster组件中的上面，我们可以配置射线，我们使用选择器升级了射线组件实体的属性。

    <a-cursor id="cursor" raycaster="objects:.link">

一单附加了射线组件，这个列表就会被填充。不过，links是模板制作的，那是还不能被发现。我们能做的就只有
当link 附加了之后能够刷新raycaster的组件。组件的框架如下所示。

      AFRAME.registerComponent('update-raycaster',{
        schema:{
          //....
        },
        init:function(){
        //...
        }
      });
首先，需要指定schema属性，这样我们就可以传入需要更新的射线。使用选择器作为schema的属性这样我们非常方
便的 **update-raycaster="#cursor"**

    AFRAME.registerComponent('update-raycaster',{
          schema:{
            type:'selector'
          },
          init:function(){
            //..
          }
    
        });
接下来我们就在init方法(当组件附加到实体上时会调用该方法)中升级射线,更新射线的函数为

    AFRAME.registerComponent('update-raycaster',{
          schema:{
            type:'selector'
          },
          init:function(){
            var raycasterEL = this.data;
            this.data.components.raycaster.refreshObjects();
          }
        });
#### 设置图像组件
> 查看[set-image component on Github](https://github.com/aframevr/360-image-viewer-boilerplate/blob/master/components/set-image.js)
    
最后我们写一个当点击link时sky会显示一个新的全景图的组件，组件的基本框架为：

      AFRAME.registerComponent('set-image',{
         schema:{
         //....
         },
         init:function(){
         //....
         }
      });
下面我们来看一下图像设置组件的所需的API，我们需要
* 事件的监听名称
* 确定需要改变贴图的实体
* 贴图文件
* 消隐动画
下面为具体实现：
  
      AFRAME.registerComponent('set-image',{
          schema:{
            on:{type:'string'},
            target:{type:'selector'},
            src:{type:'string'},
            dur:{type:'number',default:300}
          },
          init:function(){
          //..
          },
          setupFadeAnimation:function(){
          //添加一个消隐至黑色的动画
          }
      });
现在我们设置一个当贴图逐渐变为黑色时以改变图像的事件监听器,当事件一触发，那么这个组件就会触发动画，
等待一段时间后，切换图像

      AFRAME.registerComponent('set-image',{
          schema:{
            on:{type:'string'},
            target:{type:'selector'},
            src:{type:'string'},
            dur:{type:'number',default:300}
          },
          init:function(){
            var data = this.data;
            var el = this.el;
            this.setupFadeAnimation();
            el.addEventListener(data.on,function(){
                data.target.emit('set-image-fade');
                setTimeout(function(){
                    data.target.setAttribute('material','src',data.src);
                    },data.dur);
                });
          },
          setupFadeAnimation:function(){
          //添加一个消隐至黑色的动画
          }
      })   

