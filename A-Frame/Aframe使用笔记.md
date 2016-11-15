## Aframe 使用笔记

#### 确定自己使用的版本正确
正确的版本是可以支持音频播放的，直接将要播放的音频给audio 组件即可不用转化成为流的方式。

#### AFRAME.registerComponents() 方法
    
      AFRAME.registerComponents('updatename',{
        schema:{
            type:'selector'
        },
        //data: 表示数据
        //el ：表示实体
        init:function(){
         //在这里this.data就等于selector
        }
      });
  //使用方法
    <a-entity id="saa"  updatename="#saa" ></a-entity>

      AFRAME.registerComponents('updatename',{
        schema:{
          val:{type:'int'}
        },
        //data: 表示数据
        //el ：表示实体
        init:function(){
          //引用数据的话使用。
          this.data.val
        }
      });
      <!-- 可以发现， this.data 引用的是schema中的数据，而this.el代表的是整个实体对象-->

#### AFRAME中用到的几个方法小记
* this.el.object3D.position.set(x,y,z); //设置某个实体对象的位置

