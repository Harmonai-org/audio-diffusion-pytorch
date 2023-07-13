from setuptools import find_packages, setup

setup(
    name="audio-diffusion-pytorch-fork",
    packages=find_packages(exclude=[]),
    version="0.0.101",
    license="MIT",
    description="A fork of Flavio Schneider's Audio Diffusion - PyTorch",
    long_description_content_type="text/markdown",
    author="Harmonai",
    url="https://github.com/harmonai-org/audio-diffusion-pytorch-fork",
    keywords=["artificial intelligence", "deep learning", "audio generation"],
    install_requires=[
        "tqdm",
        "torch>=1.6",
        "data-science-types>=0.2",
        "einops>=0.4",
        "einops-exts>=0.0.3",
        "audio-encoders-pytorch",
        "descript-audio-codec"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)
