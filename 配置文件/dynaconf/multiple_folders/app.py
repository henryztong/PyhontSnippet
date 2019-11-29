import sys
import os
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir,os.pardir))
sys.path.append(parent_dir)

from dynaconf import settings

print("development")
print(settings.VAR1)
print(settings.VAR2)

print("production")
settings.setenv("production")
print(settings.VAR1)
print(settings.VAR2)