# 基于StyleGAN2的新版人脸生成器
<i>Read English Introduction：<a href='https://github.com/a312863063/generators-with-stylegan2/blob/master/README_EN.md'>Here</a></i><br />
<br />
&emsp;&emsp;这儿是一批基于StyleGAN2制作的新版人脸生成器，既包含基于旧版重制的<a href='https://github.com/a312863063/seeprettyface-generator-wanghong'>网红脸</a>，<a href='https://github.com/a312863063/seeprettyface-generator-star'>明星脸</a>，<a href='https://github.com/a312863063/seeprettyface-generator-model'>超模脸</a>，<a href='https://github.com/a312863063/seeprettyface-generator-babies'>萌娃脸</a>和<a href='https://github.com/a312863063/seeprettyface-generator-yellow'>黄种人脸</a>生成器，也新增了两款更具美学意义的<a href='#'>混血脸</a>和<a href='#'>亚洲美人脸</a>生成器，并附赠有通配的人脸属性编辑器。做了这么多款生成器已经足够用，我将不再尝试做人脸生成器相关的新内容，而是去探索更实用、更能满足用户需求的生成技术，以更好地服务人民。<br />
&emsp;&emsp;生成器的作用是可提供我们各种样式的人脸素材，供我们在多种场景下应用并有助于节省寻找真人（人脸）的成本，值得注意的是，<b>每张人脸都是不存在于这个世界上的AI虚拟人物，他们独特且永不重复。</b>

<br /><br /><br />
## 新版的提升与价值何在？
&emsp;&emsp;基于StyleGAN2制作的版本消除了图片中水滴斑点和扭曲/损坏现象的出现，使生成的成功率接近100%（可参见下方随机生成的数据集），能被应用于大批量生成任务之中；另外图片的质量进一步提升，清晰度已逼近于官方训练所采用的数据集。<b>我希望，这个项目能为影视、广告、游戏和医美工作者们助力，同时为普通爱好者们赋能。</b><br />
&emsp;&emsp;此项目已大部分免费开源，希望能帮助到有需要的朋友。模型仅供玩耍和研究使用，未获得授权不允许用作商业用途。模型版权所有为：www.seeprettyface.com ，若对您有帮助欢迎在底部赞助~ <br />

<br /><br />
# 效果预览

## 网红脸生成器
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/wanghong.png)<br/><br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/example_wanghong.jpg)<br/><br/>
&emsp;&emsp;纯随机生成(无筛选)的一万张生成图片数据集：<a href='https://pan.baidu.com/s/1AqlNlTY0-tbEORPuKLdkqg'>https://pan.baidu.com/s/1AqlNlTY0-tbEORPuKLdkqg</a>  提取码：c7v9<br /><br />

## 明星脸生成器
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/star.png)<br/><br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/example_star.jpg)<br/><br/>
&emsp;&emsp;纯随机生成(无筛选)的一万张生成图片数据集：<a href='https://pan.baidu.com/s/1LabQMFLsKkYK3hLgRCQ-0A'>https://pan.baidu.com/s/1LabQMFLsKkYK3hLgRCQ-0A</a>  提取码：p43h<br /><br />

## 超模脸生成器
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/model.png)<br/><br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/example_model.jpg)<br/><br/>
&emsp;&emsp;纯随机生成(无筛选)的一万张生成图片数据集：<a href='https://pan.baidu.com/s/1AT4q1JkMvAxWrHMs4Af1wg'>https://pan.baidu.com/s/1AT4q1JkMvAxWrHMs4Af1wg</a>  提取码：vxf4<br /><br />

## 萌娃脸生成器
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/kid.png)<br/><br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/example_kids.jpg)<br/><br/>
&emsp;&emsp;纯随机生成(无筛选)的一万张生成图片数据集：<a href='https://pan.baidu.com/s/1CQYQFiIdXxCSjJwSUo_tvw'>https://pan.baidu.com/s/1CQYQFiIdXxCSjJwSUo_tvw</a>  提取码：4bd0<br /><br />

## 黄种人脸生成器
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/yellow.png)<br/><br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/example_yellow.jpg)<br/><br/>
&emsp;&emsp;纯随机生成(无筛选)的一万张生成图片数据集：<a href='https://pan.baidu.com/s/1uC5fQ4UTALA1uU36Cgnnnw'>https://pan.baidu.com/s/1uC5fQ4UTALA1uU36Cgnnnw</a>  提取码：rqvq <br/><br/>

## 混血人脸生成器（非开源）
&emsp;&emsp;你知道长得最好看的人脸是什么样吗？我将中国明星脸生成器与世界超模脸生成器按精心调制的比例融合起来，制作出了此混血人脸生成器。<b>此生成器合成的人脸具备独特且卓绝的美学风格（用户的评价是“马夸特面具融入了东方人的韵味”），是我认为目前AI画出的最好看的人脸生成器</b>。然而此生成器已被买断属于非卖品。<br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/mixed-blood.png)<br/><br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/example_mixed-blood.jpg)<br/><br/><br/>

## 亚洲美人脸生成器（非开源）
&emsp;&emsp;有趣的事情是，在我开源完上述生成器后，一名视觉杂志社的主编找到我，说想一起探讨是否能做出更有辨识度和“惊艳感”的人脸生成器——<b>因为只有在美学上AI能超越人类的话，这种技术才能有效冲击传统的视觉行业——因为这意味着人们能够花最低的成本获取最优质的资源</b>。更有利的一点是，杂志社有优质的图像素材资源，而我有多变的训练技巧，于是我们合作，做出了这一款“亚洲美人脸”生成器，下面展示一些生成器合成的人脸素材。

## 港式美人脸
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/hongkong-style.jpg)<br/>

## 日式美人脸
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/japanese-style.jpg)<br/><br/>


## 总结
&emsp;&emsp;上述这么多生成器看着有点可怕，但其实它离真正的商用之路还早着很呢。。如果真想冲击传统视觉行业的话，至少有两个问题亟待解决：1.相关配套技术有待完善，譬如人脸植入、妆容精细控制、动画及全身合成等等；2.如何围绕精细的用户群构建特定的生成技术服务体系也有待探索。

# 环境配置
&emsp;&emsp;· Both Linux and Windows are supported. Linux is recommended for performance and compatibility reasons.<br/>
&emsp;&emsp;· 64-bit Python 3.6 installation. We recommend Anaconda3 with numpy 1.14.3 or newer.<br/>
&emsp;&emsp;· TensorFlow 1.14 or 1.15 with GPU support. The code does not support TensorFlow 2.0.<br/>
&emsp;&emsp;· On Windows, you need to use TensorFlow 1.14 — TensorFlow 1.15 will not work.<br/>
&emsp;&emsp;· One or more high-end NVIDIA GPUs, NVIDIA drivers, CUDA 10.0 toolkit and cuDNN 7.5. To reproduce the results reported in the paper, you need an NVIDIA GPU with at least 16 GB of DRAM.<br/>
&emsp;&emsp;· Docker users: use the provided <a href='https://github.com/NVlabs/stylegan2/blob/master/Dockerfile'>Dockerfile</a> to build an image with the required library dependencies.<br/>
&emsp;&emsp;- On Windows, the compilation requires Microsoft Visual Studio to be in PATH. We recommend installing <a href='https://visualstudio.microsoft.com/vs/'>Visual Studio Community Edition</a> and adding into PATH using "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat".<br/>
&emsp;&emsp;我的测试环境配置为：Win10,1050Ti,CUDA 10.0,CuDNN 7.6.5,tensorflow-gpu 1.14.0，VS2017可完美运行。<br/><br/>

## Windows下常见问题 ：Could not find MSVC/GCC/CLANG installation on this computer如何解决？
&emsp;&emsp;在安装VS2017/VS2019时一定要将‘使用C++的桌面开发’选上（如下图所示）
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/SMVC_solution/solution1.png)
&emsp;&emsp;装好之后进入C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/ 目录下会有一个版本号的文件夹，将版本替换为dnnlib/tflib/custom_ops.py 29行的对应版本号（那是我安装的版本），如下图所示。
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/SMVC_solution/solution2.png)

# 运行步骤
&emsp;&emsp;1.在networks文件夹中按照txt地址下载对应模型，放在该位置<br/>
&emsp;&emsp;2.在main.py中选择对应的模型和生成数量(另如果觉得生成的多样性不够可以尝试调高truncation_psi，不过成功率会下降)，并运行main.py<br/>
<br /><br /><br />

# 赠品：基于StyleGAN2的属性编辑器
&emsp;&emsp;基于StyleGAN2的属性编辑器(edit_photo.py)包含了与<a href='https://github.com/a312863063/seeprettyface-face_editor'>旧版属性编辑器</a>基本相同的内容，含有21种可调整的方向，可实现简单的人脸属性编辑。此属性编辑器适用于此项目的所有生成器（即黄种人、网红脸、明星脸、超模脸、萌娃脸、混血脸和亚洲美人脸）以及官方生成器。<br /><br />

## 调整样例
<br /><b>下述样例均采用黄种人脸生成器。</b><br />
## 1.调整笑容
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_smile.jpg)<br /><br /><br />

## 2.调整年龄
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_age.jpg)<br /><br /><br />

## 3.调整水平角度
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_horizontal.jpg)<br /><br /><br />

## 4.调整竖直角度
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_vertical.jpg)<br /><br /><br />

## 5.调整性别
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_gender.jpg)<br /><br /><br />

## 6.调整颜值
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_beauty.jpg)<br /><br /><br />

## 7.调整脸型
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_face_shape.jpg)<br /><br /><br />

## 8.调整眼睛开合
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_eyes_open.jpg)<br /><br /><br />

## 9.调整是否佩戴眼镜
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_glasses.jpg)<br /><br /><br />

## 10.增添/减弱一些生气的情绪
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_angry.jpg)<br /><br /><br />

## 11.增添/减弱一些厌恶的情绪
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_disgust.jpg)<br /><br /><br />

## 12.增添/减弱一些害怕的情绪
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_fear.jpg)<br /><br /><br />

## 13.增添/减弱一些开心的情绪
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_happy.jpg)<br /><br /><br />

## 14.增添/减弱一些沮丧的情绪
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_sad.jpg)<br /><br /><br />

## 15.增添/减弱一些惊讶的情绪
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_surprise.jpg)<br /><br /><br />

## 16.增添/减弱一些平静的情绪
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_easy.jpg)<br /><br /><br />

## 17.调整脸的宽度
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_width.jpg)<br /><br /><br />

## 18调整脸的高度
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_height.jpg)<br /><br /><br />

## 19.调整向黑种人衍变
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_race_black.jpg)<br /><br /><br />

## 20.调整向黄种人衍变
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_race_yellow.jpg)<br /><br /><br />

## 21.调整向白种人衍变
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_race_white.jpg)<br /><br /><br /><br /><br /><br />


# 了解技术原理 & 获取训练集：[点此进入](http://www.seeprettyface.com/)
<p>
	<img src="https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/virtual-model.gif" alt="Sample"  width="512">
</p>
<br/><br/><br/><br/>

## 小小的赞助~
<p align="center">
	<img src="https://github.com/a312863063/seeprettyface/blob/master/sponsor.jpg" alt="Sample"  width="324" height="504">
	<p align="center">
		<em>若对您有帮助可给予小小的赞助~</em>
	</p>
</p>
<br/><br/><br/>

