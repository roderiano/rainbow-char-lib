from setuptools import setup

setup(
    name='rainbowchar',
    packages=['rainbowchar'],
    version='1.1',
    description='RainbowChar is a lib that stylizes text by formatting in ANSI escape code. It only supports true color terminals.',
    author='Gabriel da Rosa Silveira',
    author_email='gabrielsilveirapro@gmail.com',
    url='https://github.com/roderiano/rainbow-char-lib',
    download_url='https://github.com/roderiano/rainbow-char-lib/archive/refs/tags/v1.1.tar.gz',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner==4.4'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
