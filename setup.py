from setuptools import setup

setup(name='job_snapshotting',
      version='0.1',
      description='Snapshot job stages to Google Cloud Storage',
      url='https://github.com/justinholmes/job_snapshotting',
      author='Justin Holmes',
      author_email='justin@nascency.co.uk',
      license='apache2',
      packages=['job_snapshotting'],
      install_requires=[
          'marshmallow==3.0.0rc1',
          'google-cloud-storage==1.13.1'
      ],
      zip_safe=True)
