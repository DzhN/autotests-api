import grpc

import course_service_pb2
import course_service_pb2_grpc

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

# Отправляем запрос
response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="1"))
print(f"Id курса: {response.course_id}\nЗаголовок курса: {response.title}\nОписание: {response.description}")
