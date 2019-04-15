from setuptools import setup
import setuptools

setup(
    name='zendesk_sell',
    packages=setuptools.find_packages(),
    version='1.0.0',
    description='Python wrapper for the Zendesk Sell API',
    license='MIT',
    author='John Faucett',
    author_email='john.faucett@studitemps.de',
    url='git@github.com:johnfaucette/py-zendesk_sell.git',
    download_url='https://github.com/johnfaucette/py-zendesk_sell/releases/tag/1.0.0',
    install_requires=[
        'requests>=2.21.0'
    ],
    keywords=['zendesk', 'api', 'wrapper'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English'
    ]
)