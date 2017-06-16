
files = $(shell find . -iname '*.proto')
all:
	python -c "import os,glob; [os.system('protoc --python_out=../adsmsg/protobuf {file}'.format(file=x)) for x in glob.glob('*.proto')]"
clean:
	python -c "import os,glob; [os.system('rm -fr ../adsmsg/protobuf/{file}_pb2.py*'.format(file=x.split('.proto')[0])) for x in glob.glob('*.proto')]"
