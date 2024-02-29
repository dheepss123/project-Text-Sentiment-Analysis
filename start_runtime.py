# Standard
from os import path
import sys
import alog

# Here we assume that `start_runtime` file is at the same level of the `text_sentiment` package
sys.path.append(
   path.abspath(path.join(path.dirname(__file__), "../"))
)
# Local Library
import text_sentiment
alog.configure(default_level="debug")

# Local Library
from caikit.runtime import grpc_server

# Start the gRPC Caikit runtime server
grpc_server.main()