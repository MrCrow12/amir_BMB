from setuptools import setup, find_packages

setup(
    name='amir_sms_bomber',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='amir',
    author_email='amirrobot64@gmail.com',
    description='please do not try on others',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MrCrow12/amir_BMB', 
)
