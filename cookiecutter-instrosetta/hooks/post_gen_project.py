import os
import sys

try:
    package_hierarchy = "{{cookiecutter.package_name}}".split(".")
    package_path = os.path.join(*package_hierarchy)
    interface_path = os.path.join("{{cookiecutter.project_slug}}", "interfaces", package_path)
    clients_path = os.path.join("{{cookiecutter.project_slug}}","clients", package_path)
    client_path = os.path.join(clients_path, "{{cookiecutter.interface_name}}_client.py")
    servers_path = os.path.join("{{cookiecutter.project_slug}}","servers", "{{cookiecutter.manufacturer_name}}")
    server_path = os.path.join(servers_path, "{{cookiecutter.device_name}}")
    protos_path = os.path.join("{{cookiecutter.project_slug}}","{{cookiecutter.project_slug}}-proto","interfaces")
    proto_path = os.path.join(protos_path, package_path, "{{cookiecutter.interface_name}}.proto")
   
    os.renames("{{cookiecutter.project_slug}}/{{cookiecutter.interface_name}}_client.py", client_path)
    os.renames("{{cookiecutter.project_slug}}/{{cookiecutter.device_name}}", server_path)
    os.renames("{{cookiecutter.project_slug}}/{{cookiecutter.interface_name}}.proto", proto_path)
    if os.path.isfile("./generate_stubs.py"):
        ret = os.system("python ./generate_stubs.py")
        sys.exit(ret)
    else:
        raise Exception("Cant find stub generator script.")
except Exception as e:
    sys.exit(e)