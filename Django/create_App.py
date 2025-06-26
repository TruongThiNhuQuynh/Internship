import os
import sys

def create_django_app(project_name, app_name):
    # Tạo project Django mới
    os.system(f'django-admin startproject {project_name}')
    # Di chuyển vào thư mục project
    os.chdir(project_name)
    # Tạo app mới
    os.system(f'python manage.py startapp {app_name}')
    print(f"Đã tạo project '{project_name}' và app '{app_name}' thành công.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Cách dùng: python create_App.py <tên_project> <tên_app>")
    else:
        project_name = sys.argv[1]
        app_name = sys.argv[2]
        create_django_app(project_name, app_name)