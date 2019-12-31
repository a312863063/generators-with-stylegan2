# New version of face generators based on StyleGAN2

<br />
&emsp;&emsp;Here is a series of new face generators based on StyleGAN2.I reworked the old version of the <a href='https://github.com/a312863063/seeprettyface-generator-yellow'>yellow face generator</a>，<a href='https://github.com/a312863063/seeprettyface-generator-wanghong'>chinese internet-celebrity face generator</a>，<a href='https://github.com/a312863063/seeprettyface-generator-star'>chinese pop-star face generator</a>，<a href='https://github.com/a312863063/seeprettyface-generator-model'>world supermodel face generator</a> and <a href='https://github.com/a312863063/seeprettyface-generator-babies'>cute baby face generator</a> based on StyleGAN2, which greatly improved the generation effect. The function of the generator is to provide various styles of face materials for us to use at will, and we don't have to worry about the copyright of the faces because each face is virtual and unique.

<br /><br /><br />
## What is the enhancement and value of the new version?
&emsp;&emsp;The new version based on StyleGAN2 eliminates the occurrence of artifacts and distortion / damage in the picture, making the generation success rate close to 100% (see the randomly generated dataset below), which can be used in mass generation tasks; in addition The quality of the pictures has been further improved, and the clarity has approached the dataset used in official training. <b>I hope that this project will help film, television, advertising, games, and medical & aesthetic workers, and at the same time empower ordinary enthusiasts.</b><br />
&emsp;&emsp;This project is all free and open source for everyone to play. Note that the copyright owner of the model is: www.seeprettyface.com, Please do not use it for commercial purposes without permission.<br />

<br /><br />
# Effect preview

## Chinese Internet-celebrity Face Generator
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/wanghong.png)<br/><br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/example_wanghong.jpg)<br/><br/>

## Chinese Pop-star Face Generator
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/star.png)<br/><br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/example_star.jpg)<br/><br/>

## World Supermodel Face Generator
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/model.png)<br/><br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/example_model.jpg)<br/><br/>

## Cute Baby Face Generator
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/kid.png)<br/><br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/example_kids.jpg)<br/><br/>

## Yellow Face Generator
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/yellow.png)<br/><br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/example_yellow.jpg)<br/><br/>

## Mixed-blood Face Generator（Not available）
&emsp;&emsp;Do you know what the best looking human face looks like? I combined the Chinese pop-star face generator with the world's supermodel face generator in a carefully modulated ratio to create this mixed-blood face generator. <b>The face synthesized by this generator has a unique and outstanding aesthetic style (the customer's evaluation is "Maquatte mask blends with the charm of Orientals"), which in my opinion is the best-looking face currently drawn by AI Generator </b>. However, this generator has been bought out and is not for sale.<br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/mixed-blood.png)<br/><br/>
&emsp;&emsp;![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/example_mixed-blood.jpg)<br/><br/><br/><br/>

# Environment configuration
&emsp;&emsp;· Both Linux and Windows are supported. Linux is recommended for performance and compatibility reasons.<br/>
&emsp;&emsp;· 64-bit Python 3.6 installation. We recommend Anaconda3 with numpy 1.14.3 or newer.<br/>
&emsp;&emsp;· TensorFlow 1.14 or 1.15 with GPU support. The code does not support TensorFlow 2.0.<br/>
&emsp;&emsp;· On Windows, you need to use TensorFlow 1.14 — TensorFlow 1.15 will not work.<br/>
&emsp;&emsp;· One or more high-end NVIDIA GPUs, NVIDIA drivers, CUDA 10.0 toolkit and cuDNN 7.5. To reproduce the results reported in the paper, you need an NVIDIA GPU with at least 16 GB of DRAM.<br/>
&emsp;&emsp;· Docker users: use the provided <a href='https://github.com/NVlabs/stylegan2/blob/master/Dockerfile'>Dockerfile</a> to build an image with the required library dependencies.<br/>
&emsp;&emsp;- On Windows, the compilation requires Microsoft Visual Studio to be in PATH. We recommend installing <a href='https://visualstudio.microsoft.com/vs/'>Visual Studio Community Edition</a> and adding into PATH using "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat".<br/>
&emsp;&emsp;<b>My test environment configuration is: Win10, 1050Ti, CUDA 10.0, CuDNN 7.6.5, tensorflow-gpu 1.14.0, VS2017 can run perfectly.</b><br/><br/>

## Common problem under Windows: "Could not find MSVC/GCC/CLANG installation on this computer" How to solve it?
&emsp;&emsp;When installing VS2017/VS2019, be sure to select ‘Desktop development using C ++’ (shown below)
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/SMVC_solution/solution1.png)
&emsp;&emsp;After installation, enter C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/. There will be a folder with a version number. Replace the version written in dnnlib/tflib/custom_ops.py line 29 with the corresponding version number of the line (that is the version I installed), as shown in the figure below.
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/SMVC_solution/solution2.png)

# Operation steps
&emsp;&emsp;1.Download the corresponding model according to the .txt address in the networks folder and place it in this location<br/>
&emsp;&emsp;2.Select the corresponding model and generation number in main.py and run it.<br/>
<br /><br /><br />

# Giveaway: Attribute Editor based on StyleGAN2
&emsp;&emsp;The StyleGAN2-based attribute editor (edit_photo.py) contains the same content as <a href='https://github.com/a312863063/seeprettyface-face_editor'> legacy attribute editor </a>, containing 21 Adjustable orientation for simple face attribute editing. This property editor applies to all generators of this project (ie yellow, internet-celebrity face, star face, supermodel face, cute baby face and mixed-blood face) as well as official generators.<br /><br />

## Adjustment example
<br /><b>The following examples use the yellow face generator.</b><br />
## 1.Adjust smile
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_smile.jpg)<br /><br /><br />

## 2.Adjust age
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_age.jpg)<br /><br /><br />

## 3.Adjust horizontal angle
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_horizontal.jpg)<br /><br /><br />

## 4.Adjust vertical angle
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_vertical.jpg)<br /><br /><br />

## 5.Adjust gender
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_gender.jpg)<br /><br /><br />

## 6.Adjust beauty
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_beauty.jpg)<br /><br /><br />

## 7.Adjust face shape
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_face_shape.jpg)<br /><br /><br />

## 8.Adjust eyes opening
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_eyes_open.jpg)<br /><br /><br />

## 9.Adjust whether to wear glasses
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_glasses.jpg)<br /><br /><br />

## 10.Add / reduce some angry emotions
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_angry.jpg)<br /><br /><br />

## 11.Add / reduce some disgust emotions
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_disgust.jpg)<br /><br /><br />

## 12.Add / reduce some fear emotions
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_fear.jpg)<br /><br /><br />

## 13.Add / reduce some happy emotions
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_happy.jpg)<br /><br /><br />

## 14.Add / reduce some upset emotions
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_sad.jpg)<br /><br /><br />

## 15.Add / reduce some surprise emotions
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_surprise.jpg)<br /><br /><br />

## 16.Add / reduce some calm emotions
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_emotion_easy.jpg)<br /><br /><br />

## 17.Adjust width of the face
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_width.jpg)<br /><br /><br />

## 18.Adjust height of the face
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_height.jpg)<br /><br /><br />

## 19.Adjusting to the black race
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_race_black.jpg)<br /><br /><br />

## 20.Adjusting to the yellow race
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_race_yellow.jpg)<br /><br /><br />

## 21.Adjusting to the white race
![Image text](https://github.com/a312863063/generators-with-stylegan2/blob/master/examples/edit_photo/change_race_white.jpg)<br /><br /><br /><br /><br />

## More Attempts: Synthesizing Talking Face Videos
&emsp;&emsp;Recommend Few Shot Vid-to-vid (<a href='https://github.com/NVlabs/few-shot-vid2vid'> Click here to jump </a>) method (the effect is shown in the figure below). <br /> <br /> <br />
![Image text](https://github.com/NVlabs/few-shot-vid2vid/raw/master/imgs/mona_lisa.gif)<br /><br /><br/><br/>

# Learn technical principles & Get training set: [click here to enter](http://www.seeprettyface.com/)
![Image text](https://github.com/a312863063/seeprettyface/blob/master/EP001-01.png)<br/><br/><br/>

## What next:
&emsp;&emsp;There are three steps that the virtual person take to replace the real person:<br/>
1.The virtual person has an attractive appearance that makes people fall in love at first sight.
2.The Virtual person has various postures that make people feel natural and comfortable.
3.The virtual person has a lovely character that makes people feel warm and cute.
<br/><br/><br/>
