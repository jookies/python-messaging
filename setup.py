from setuptools import setup, find_packages
import sys
from messaging import VERSION

setup(
    name="python-messaging",
    version='%s.%s.%s' % VERSION,
    description='SMS/MMS encoder/decoder',
    license=open('COPYING').read(),
    packages=find_packages(exclude=["tests"]),
    py_modules=["messaging"],
    include_package_data=True,
    package_data={'messaging': ['README.md']},
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Communications :: Telephony',
    ],
)
