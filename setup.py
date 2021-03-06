from distutils.core import setup
setup(
  name = 'convertify',
  packages = ['convertify'],
  version = '0.6',
  license='MIT',
  description = 'Convert images to a different format',
  author = 'Faton Sopa',
  author_email = 'faton.sopa@manaferra.com',
  url = 'https://github.com/fatonsopa/convertify',
  download_url = 'https://github.com/fatonsopa/convertify/blob/master/dist/convertify-0.6.tar.gz',
  keywords = ['pythonforseo', 'convert-image', 'image-to-webp','images','page-speed'],
  install_requires=[
          'Pillow'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
  entry_points={
    'console_scripts': ['convertify = convertify.command_line:main']
  },
)