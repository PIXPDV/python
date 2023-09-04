from setuptools import setup, find_packages

setup(
    name='PIXPDV',
    version='1.0.1',
    description='Uma biblioteca para interagir com o serviço PIXPDV.',
    author='PIXPDV',
    author_email='sac@pixpdv.com.br',
    url='https://github.com/PIXPDV/python',
    packages=find_packages(),
    install_requires=[
        'requests',  # Adicione quaisquer dependências necessárias aqui
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
