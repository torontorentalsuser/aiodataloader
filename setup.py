from setuptools import setup

vendor_version = "rentals.0"
version_prefix = "0.2.2"

def get_version():
    import subprocess
    commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf8").strip()[:12]
    label = subprocess.check_output(["git", "describe"]).decode("utf8").strip()
    last_tag = subprocess.check_output(["git", "describe", "--abbrev=0"]).decode("utf8").strip()
    
    version = version_prefix + "." + vendor_version
    if last_tag != label:
        version += "+git." + commit_hash

    return version


version = get_version()

tests_require = [
    'pytest>=3.6', 'pytest-cov', 'coveralls', 'mock', 'pytest-asyncio'
]

setup(
    name='aiodataloader',
    version=version,
    description='Asyncio DataLoader implementation for Python',
    long_description=open('README.rst').read(),
    url='https://github.com/syrusakbary/aiodataloader',
    download_url='https://github.com/syrusakbary/aiodataloader/releases',
    author='Syrus Akbary',
    author_email='me@syrusakbary.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='concurrent future deferred aiodataloader',
    py_modules=['aiodataloader'],
    extras_require={
        'test': tests_require,
    },
    tests_require=tests_require, )
