import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='World'))
        print("Greeter client received: " + response.message)
        
        void_response = stub.VoidFunction(helloworld_pb2.VoidRequest())
        print("Void function called")
        
        long_operation_request = helloworld_pb2.LongOperationRequest(arg1=1, arg2=2, arg3=3, arg4=4, arg5=5, arg6=6, arg7=7, arg8=8)
        long_operation_response = stub.LongFunction(long_operation_request)
        print("Long operation result:", long_operation_response.result)
        
        string_operation_request = helloworld_pb2.StringOperationRequest(input_string="string teste")
        string_operation_response = stub.StringOperation(string_operation_request)
        print("String operation result:", string_operation_response.output_string)
        
        complex_object = helloworld_pb2.ComplexType(
            id=123,
            name="complex",
        )
        
        complex_operation_request = helloworld_pb2.ComplexOperationRequest(input_complex=complex_object)
        complex_operation_response = stub.ComplexOperation(complex_operation_request)
        print("Complex operation result:", complex_operation_response.output_complex)
        
        

if __name__ == '__main__':
    run()
