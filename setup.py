from setuptools import setup, find_packages

setup(
    name='pyqt-chat-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt widget for chatting app',
    url='https://github.com/yjg30737/pyqt-chat-widget.git',
    install_requires=[
        'PyQt5'
    ]
)