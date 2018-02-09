import os.path
from setuptools import setup, find_packages


# single source of truth for package version
version_ns = {}
with open(os.path.join('globus_portal_framework', 'version.py')) as f:
    exec(f.read(), version_ns)

install_requires = []
with open('requirements.txt') as reqs:
    for line in reqs.readlines():
        req = line.strip()
        if not req or req.startswith('#'):
            continue
        install_requires.append(req)


setup(name='django-globus-portal-framework',
      version=version_ns['__version__'],
      description='A framework for collating Globus Search data for use with '
                  'various Globus services. ',
      long_description=open('README.md').read(),
      author='Globus Team',
      author_email='support@globus.org',
      url='https://github.com/globusonline/django-globus-portal-framework',
      packages=find_packages(),
      install_requires=install_requires,
      dependency_links=[
          'git+https://github.com/globus/globus-sdk-python.git@cbab7728d87c4b14977b8781f4ec7f231467fd4d#egg=globus_sdk'
      ],
      include_package_data=True,
      keywords=['globus', 'file transfer', 'django'],
      license='apache 2.0',
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Communications :: File Sharing',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      )
