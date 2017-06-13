
all: ../adsmsg/protobuf/bibrecord_pb2.py ../adsmsg/protobuf/denormalized_record_pb2.py

../adsmsg/protobuf/bibrecord_pb2.py: bibrecord.proto
	protoc --python_out=../adsmsg/protobuf/ bibrecord.proto

../adsmsg/protobuf/denormalized_record_pb2.py: denormalized_record.proto
	protoc --python_out=../adsmsg/protobuf/ denormalized_record.proto

clean:
	rm -f ../adsmsg/protobuf/bibrecord_pb2.py
	rm -f ../adsmsg/protobuf/denormalized_record_pb2.py
