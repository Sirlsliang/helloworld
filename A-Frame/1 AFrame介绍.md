## A-Frame 简单介绍

#### A-Frame
>A-Frame是一个开源的创建虚拟现实的WebVr框架,可以创建在智能手机，电脑，Oculus Rift和HTC Vive中
>是使用的VR场景,。

#### Entity-Component-System
底层A-Frame使用了tree.js框架对DOM实现了entity-component-system(实体-组件-系统)的映射。场景中所有的物
体都是entity,entity 由混合的components 来实现外观的展现、行为等作用。

    <a-entity geometry="primitive:box;depth:2" material="color:#6173F4;opacity:0.8"></a-entity>

`<a-entity>`代表一个entity。属性代表components,属性值代表component的属性。利用component可以做任何事
。也就是说可以制作一个physics(物理)component 也可以制作一个 explode(爆炸) component。可以将他们组合
到一个entity当中并添加爆炸时的行为。

    <a-entity geometry="primitive:box; depth:2"
              material="color:#6173F4; opacity: 0.8"
              physics ="mass: 5;boundingBox: 1 1 2"
              explode ="on: physics-collide;indensity： 3"><a-entity>
#### 为什么要用A-Frame
#### 设备和平台的支持情况
设备与平台的支持取决于设备对浏览器支持的好坏。A-Frame框架支持平面3D和WebVR的体验
###### 平面3D的支持
这个取决于设备对WebGL的支持情况
###### VR设备的体验
除了要看设备对WebGL的支持情况外,还取决于浏览器对WebVR API的支持情况，
###### 硬件配置信息
IOS：最低iphone 6;Android Galaxy s6
help create

q
:q
