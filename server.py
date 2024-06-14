from concurrent import futures
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)
    
    def VoidFunction(self, request, context):
        return helloworld_pb2.VoidReply()
    
    def LongFunction(self, request, context):
        result = sum(getattr(request, f'arg{i}') for i in range(1, 9))
        return helloworld_pb2.LongOperationReply(result=result)
    
    def StringOperation(self, request, context):
        input_str = request.input_string
        output_str = input_str[::-1]  # Inverte a string
        return helloworld_pb2.StringOperationReply(output_string=output_str)
    
    def ComplexOperation(self, request, context):
        input_complex = request.input_complex
        output_complex = helloworld_pb2.ComplexType(
            id=input_complex.id + 1,
            name=input_complex.name.upper(),
        )
        return helloworld_pb2.ComplexOperationReply(output_complex=output_complex)
    
    def MultipleString(self, request, context):
        return helloworld_pb2.MultipleStringReply(s1=request.s1, s2=request.s2, s3=request.s3, s4=request.s4, s5=request.s5, s6=request.s6)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
