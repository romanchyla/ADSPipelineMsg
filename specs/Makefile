
all: ../adsmsg/protobuf/bibrecord_pb2.py ../adsmsg/protobuf/denormalized_record_pb2.py ../adsmsg/protobuf/metrics_pb2.py ../adsmsg/protobuf/nonbibrecord_pb2.py

../adsmsg/protobuf/bibrecord_pb2.py: bibrecord.proto
	protoc --python_out=../adsmsg/protobuf/ bibrecord.proto 

../adsmsg/protobuf/denormalized_record_pb2.py: denormalized_record.proto
	protoc --python_out=../adsmsg/protobuf/ denormalized_record.proto

../adsmsg/protobuf/metrics_pb2.py: metrics.proto
	protoc --python_out=../adsmsg/protobuf/ metrics.proto 

../adsmsg/protobuf/nonbibrecord_pb2.py: nonbibrecord.proto
	protoc --python_out=../adsmsg/protobuf/ nonbibrecord.proto 
	
clean:
	rm -f ../adsmsg/protobuf/bibrecord_pb2.py
	rm -f ../adsmsg/protobuf/denormalized_record_pb2.py
	rm -f ../adsmsg/protobuf/metrics_pb2.py
	rm -f ../adsmsg/protobuf/nonbibrecord_pb2.py
	