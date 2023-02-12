#!/usr/bin/python3
import models.base_model
import models.user
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
