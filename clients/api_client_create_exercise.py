from clients.courses.courses_client import get_courses_client, CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestSchema
from clients.files.files_client import get_files_client, CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema()

# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)
print("Create user data:", create_user_response)

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Инициализируем клиент FilesClient
files_client = get_files_client(authentication_user)

# Инициализируем запрос на создание файла
create_file_request = CreateFileRequestSchema(
    upload_file="/Users/nadzhanaev/Downloads/Тестовый файл.txt"
)

# Отправляем POST запрос на загрузку файла
create_file_response = files_client.create_file(create_file_request)
print("Create file data:", create_file_response)

# Инициализируем клиент CoursesClient
create_courses_client = get_courses_client(authentication_user)

# Инициализируем запрос на создание курса
create_course_request = CreateCourseRequestSchema(
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)

# Отправляем POST запрос на создание курса
create_course_response = create_courses_client.create_course(create_course_request)
print("Create course data:", create_course_response)

# Инициализируем клиент ExercisesClient
create_exercises_client = get_exercises_client(authentication_user)

# Инициализируем запрос на создание задания
create_exercise_request = CreateExerciseRequestSchema(
    courseId=create_course_response.course.id
)

# Отправляем POST запрос на создание задания
create_exercise_response = create_exercises_client.create_exercise(create_exercise_request)
print("Create exercise data:", create_exercise_response)
