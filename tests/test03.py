# coding:utf-8
"""
    测试python调用java
"""

from jpype import *

startJVM(getDefaultJVMPath(), "-ea")
java.lang.System.out.println("hello world")
shutdownJVM()