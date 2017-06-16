from setuptools import setup
import os

setup(name='adsmsg',
      version='0.0.1',
      packages=['adsmsg'],
      install_requires=[
          'protobuf==3.3.0',
      ],
      entry_points={
            'kombu.serializers': [
                'adsmsg_serializer = adsmsg.serializer:register_args'
            ]
        }
  )