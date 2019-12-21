# Thanks to StyleGAN2 provider —— Copyright (c) 2019, NVIDIA CORPORATION.
# This work is trained by Copyright(c) 2018, seeprettyface.com, BUPT_GWY.

import numpy as np
import PIL.Image
import dnnlib
import dnnlib.tflib as tflib
import pretrained_networks
import os

def text_save(file, data):  # save generate code, which can be modified to generate customized style
    for i in range(len(data[0])):
        s = str(data[0][i])+'\n'
        file.write(s)

def generate_images(network_pkl, num, truncation_psi=0.5):
    print('Loading networks from "%s"...' % network_pkl)
    _G, _D, Gs = pretrained_networks.load_networks(network_pkl)
    noise_vars = [var for name, var in Gs.components.synthesis.vars.items() if name.startswith('noise')]

    Gs_kwargs = dnnlib.EasyDict()
    Gs_kwargs.output_transform = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
    Gs_kwargs.randomize_noise = False
    if truncation_psi is not None:
        Gs_kwargs.truncation_psi = truncation_psi
    for i in range(num):
        print('Generating image %d/%d ...' % (i, num))

        # Generate random latent
        z = np.random.randn(1, *Gs.input_shape[1:])  # [minibatch, component]

        # Save latent
        txt_filename = 'results/generate_codes/' + str(i).zfill(4) + '.txt'
        with open(txt_filename, 'w') as f:
            text_save(f, z)

        # Generate image
        tflib.set_vars({var: np.random.randn(*var.shape.as_list()) for var in noise_vars})  # [height, width]
        images = Gs.run(z, None, **Gs_kwargs)  # [minibatch, height, width, channel]

        # Save image
        PIL.Image.fromarray(images[0], 'RGB').save(dnnlib.make_run_dir_path('results/'+str(i)+'.png'))


def main():
    os.makedirs('results/', exist_ok=True)
    os.makedirs('results/generate_codes/', exist_ok=True)

    network_pkl = 'networks/generator_yellow-stylegan2-config-f.pkl'  # 模型位置
    generate_num = 20  # 生成数量

    generate_images(network_pkl, generate_num)

if __name__ == "__main__":
    main()
