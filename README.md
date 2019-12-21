# 基于StyleGAN2的新版人脸生成器

<br />
&emsp;&emsp;这儿是一批基于StyleGAN2制作的新版人脸生成器，即对于旧版的<a href='https://github.com/a312863063/seeprettyface-generator-yellow'>黄种人脸生成器</a>，<a href='https://github.com/a312863063/seeprettyface-generator-wanghong'>网红脸生成器</a>，<a href='https://github.com/a312863063/seeprettyface-generator-star'>明星脸生成器</a>，<a href='https://github.com/a312863063/seeprettyface-generator-model'>超模脸生成器</a>和<a href='https://github.com/a312863063/seeprettyface-generator-babies'>萌娃脸生成器</a>进行了基于StyleGAN2的重制，使生成效果得到大幅提升。

<br /><br />
## 新版的提升与价值何在？
&emsp;&emsp;基于StyleGAN2制作的版本消除了图片中水滴斑点和扭曲/损坏现象的出现，使生成的成功率接近100%（可参见下方随机生成的数据集），能被应用于大批量生成任务之中；另外图片的质量进一步提升，清晰度已逼近于官方训练所采用的数据集。<b>我希望，这个项目能为影视工作者、广告工作者和艺术工作者们助力，同时为普通爱好者们赋能。</b><br />
&emsp;&emsp;注意，由于模型的训练成本高，因此除了黄种人脸生成器可免费使用外，其他生成器暂时需要付费购买。此项目并非为了盈利，而是研究生成模型需要更多的显卡，所有的收入都会被用在科研当中。模型版权拥有者为：www.seeprettyface.com 。

<br /><br />
# 效果预览

## 网红脸生成器
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/wanghong.png)<br/><br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/example_wanghong.jpg)<br/><br/>
&emsp;&emsp;纯随机生成(无筛选)的一万张生成图片数据集：<a href='https://pan.baidu.com/s/1AqlNlTY0-tbEORPuKLdkqg' target='_blank'>https://pan.baidu.com/s/1AqlNlTY0-tbEORPuKLdkqg</a>  提取码：c7v9<br /><br />

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

# 环境配置
&emsp;&emsp;· Both Linux and Windows are supported. Linux is recommended for performance and compatibility reasons.<br/>
&emsp;&emsp;· 64-bit Python 3.6 installation. We recommend Anaconda3 with numpy 1.14.3 or newer.<br/>
&emsp;&emsp;· TensorFlow 1.14 or 1.15 with GPU support. The code does not support TensorFlow 2.0.<br/>
&emsp;&emsp;· On Windows, you need to use TensorFlow 1.14 — TensorFlow 1.15 will not work.<br/>
&emsp;&emsp;· One or more high-end NVIDIA GPUs, NVIDIA drivers, CUDA 10.0 toolkit and cuDNN 7.5. To reproduce the results reported in the paper, you need an NVIDIA GPU with at least 16 GB of DRAM.<br/>
&emsp;&emsp;· Docker users: use the provided <a href='https://github.com/NVlabs/stylegan2/blob/master/Dockerfile'>Dockerfile</a> to build an image with the required library dependencies.<br/>
&emsp;&emsp;- On Windows, the compilation requires Microsoft Visual Studio to be in PATH. We recommend installing <a href='https://visualstudio.microsoft.com/vs/'>Visual Studio Community Edition</a> and adding into PATH using "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat".<br/>
&emsp;&emsp;我的测试环境配置为：Win10,1050Ti,CUDA 10.0,CuDNN 7.6.5,tensorflow-gpu 1.14.0，VS2017可完美运行。<br/><br/>

# 运行步骤
&emsp;&emsp;1.在networks文件夹中按照txt地址下载对应模型，放在该位置<br/>
&emsp;&emsp;2.在main.py中选择对应的模型和生成数量，并运行main.py<br/>
<br /><br /><br />

# 了解技术原理 & 获取训练集：[点此进入](http://www.seeprettyface.com/)
![Image text](https://github.com/a312863063/seeprettyface/blob/master/EP001-01.png)<br/><br/><br/>
