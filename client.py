import grpc
import time
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        
        def measure_time(callable, *args):
            start_time = time.perf_counter()
            result = callable(*args)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            return result, elapsed_time
    

        # Chama a função SayHello
        response, elapsed_time = measure_time(stub.SayHello, helloworld_pb2.HelloRequest(name='Alice'))
        print(f"Greeter client received: {response.message} (Time taken: {elapsed_time:.9f} seconds)")

        # Chama a função VoidFunction
        void_response, elapsed_time = measure_time(stub.VoidFunction, helloworld_pb2.VoidRequest())
        print(f"Void function called (Time taken: {elapsed_time:.9f} seconds)")

        # Chama a função LongFunction
        long_function_request = helloworld_pb2.LongOperationRequest(
            arg1=1245123123, arg2=1245123123, arg3=1245123123, arg4=1245123123, arg5=1245123123, arg6=1245123123, arg7=1245123123, arg8=1245123123
        )
        long_function_response, elapsed_time = measure_time(stub.LongFunction, long_function_request)
        print(f"Long function result: {long_function_response.result} (Time taken: {elapsed_time:.9f} seconds)")

        # Chama a função StringOperation
        test_string = "hello"
        string_operation_request = helloworld_pb2.StringOperationRequest(input_string=test_string)
        string_operation_response, elapsed_time = measure_time(stub.StringOperation, string_operation_request)
        print(f"String operation result: {string_operation_response.output_string} (Time taken: {elapsed_time:.9f} seconds)")

        # Chama a função ComplexOperation
        complex_object = helloworld_pb2.ComplexType(
            id=123,
            name="complex",
        )
        complex_operation_request = helloworld_pb2.ComplexOperationRequest(input_complex=complex_object)
        complex_operation_response, elapsed_time = measure_time(stub.ComplexOperation, complex_operation_request)
        print(f"Complex operation result (Time taken: {elapsed_time:.9f} seconds)")
        
        multiple_string_request = helloworld_pb2.MultipleStringRequest(s1="Hello", s2="World", s3="HelloWorld", s4="HelloWorld", s5="HelloWorld", s6="HelloWorld")
        multiple_string_response, elapsed_time = measure_time(stub.MultipleString, complex_operation_request)
        print(f"Multiple string operation result (Time taken: {elapsed_time:.9f} seconds)")
        

if __name__ == '__main__':
    run()
